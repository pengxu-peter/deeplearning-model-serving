#include <iostream>
#include <memory>
#include <string>
#include<string.h>

#include <grpcpp/grpcpp.h>

#include "grpcpp/create_channel.h"
#include "grpcpp/security/credentials.h"
#include "google/protobuf/map.h"

#include "tensorflow/core/framework/types.grpc.pb.h"
#include "tensorflow/core/framework/tensor.grpc.pb.h"
#include "tensorflow/core/framework/tensor_shape.grpc.pb.h"
#include "tensorflow/core/util/command_line_flags.h"

#include "predict.grpc.pb.h"  // "tensorflow_serving/apis/predict.grpc.pb.h"
#include "prediction_service.grpc.pb.h"  // "tensorflow_serving/apis/prediction_service.grpc.pb.h"

using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;

using tensorflow::TensorProto;
using tensorflow::TensorShapeProto;
using tensorflow::serving::PredictRequest;
using tensorflow::serving::PredictResponse;
using tensorflow::serving::PredictionService;

typedef google::protobuf::Map<std::string, tensorflow::TensorProto> OutMap;

class ServingClient {
public:
	ServingClient(std::shared_ptr<Channel> channel)
		: stub_(PredictionService::NewStub(channel)) {}

	// Assembles the client's payload, sends it and presents the response back
	// from the server.
	std::string callPredict(const std::string& model_name, float * data_input, float * coord_input) {

		// Data we are sending to the server.
		std::cout << "start call predict !!!" << std::endl;
		PredictRequest request;
		request.mutable_model_spec()->set_name(model_name);
		request.mutable_model_spec()->set_signature_name("predict");  //not use default model

		// Container for the data we expect from the server.
		PredictResponse response;

		// Context for the client. It could be used to convey extra information to
		// the server and/or tweak certain RPC behaviors.
		ClientContext context;

		google::protobuf::Map<std::string, tensorflow::TensorProto>& inputs =
			*request.mutable_inputs();

		tensorflow::TensorProto proto_data;
		proto_data.set_dtype(tensorflow::DataType::DT_FLOAT);
		//proto_data.add_float_val(data_input);
		for (uint32_t i = 0; i < (1 * 1 * 128 * 128 * 128); i++) {
			proto_data.add_float_val(*data_input++);
			//data_input++;
		}
		//proto_data.add_float_val(data_input);
		proto_data.mutable_tensor_shape()->add_dim()->set_size(1);
		proto_data.mutable_tensor_shape()->add_dim()->set_size(1);
		proto_data.mutable_tensor_shape()->add_dim()->set_size(128);
		proto_data.mutable_tensor_shape()->add_dim()->set_size(128);
		proto_data.mutable_tensor_shape()->add_dim()->set_size(128);
		inputs["data_input"] = proto_data;

		tensorflow::TensorProto proto_coord;
		proto_coord.set_dtype(tensorflow::DataType::DT_FLOAT);
		for (uint32_t i = 0; i < (1 * 3 * 32 * 32 * 32); i++) {
			proto_coord.add_float_val(*coord_input++);
			//coord_input++;
		}
		//proto_coord.add_float_val(coord_input);
		proto_coord.mutable_tensor_shape()->add_dim()->set_size(1);
		proto_coord.mutable_tensor_shape()->add_dim()->set_size(3);
		proto_coord.mutable_tensor_shape()->add_dim()->set_size(32);
		proto_coord.mutable_tensor_shape()->add_dim()->set_size(32);
		proto_coord.mutable_tensor_shape()->add_dim()->set_size(32);
		inputs["coord_input"] = proto_coord;

		// The actual RPC.
		Status status = stub_->Predict(&context, request, &response);

		// Act upon its status.
		if (status.ok()) {
			std::cout << "call predict ok" << std::endl;
			std::cout << "outputs size is " << response.outputs_size() << std::endl;

			OutMap& map_outputs = *response.mutable_outputs();
			OutMap::iterator iter;
			int output_index = 0;

			for (iter = map_outputs.begin(); iter != map_outputs.end(); ++iter) {
				tensorflow::TensorProto& result_tensor_proto = iter->second;
				std::string section = iter->first;
				std::cout << std::endl << section << ":" << std::endl;

				if ("output" == section) {
					std::cout << "result_tensor_proto size:" << result_tensor_proto.float_val_size() << std::endl;
					int titer;
					for (titer = 0; titer != result_tensor_proto.float_val_size(); ++titer) {
						std::cout << result_tensor_proto.float_val(titer) << ", ";
					}
				}
				std::cout << std::endl;
				++output_index;
			}
			return "Done.";
		}
		else {
			std::cout << "gRPC call return code: " << status.error_code() << ": "
				<< status.error_message() << std::endl;
			return "RPC failed";
		}
	}

private:
	std::unique_ptr<PredictionService::Stub> stub_;
};

int main(int argc, char** argv) {
	std::cout << "start test case !!!" << std::endl;
	const int data_length = 1 * 1 * 128 * 128 * 128;
	std::shared_ptr<float> spData_input(new float[data_length](), [](float* pD) { delete[] pD; });
	memset(spData_input.get(), 1.0, sizeof(float)*data_length);
	const int coord_length = 1 * 3 * 32 * 32 * 32;
	std::shared_ptr<float> spCoord_input(new float[coord_length](), [](float* pD) { delete[] pD; });
	memset(spCoord_input.get(), 1.0, sizeof(float)*coord_length);

	std::string server_port = "10.100.37.2:19001";
	std::string model_name = "3d_nodule_detector";
	
	std::cout << "start grpc connect !!!" << std::endl;
	ServingClient sclient(grpc::CreateChannel(server_port, grpc::InsecureChannelCredentials()));

	std::string reply = sclient.callPredict(model_name, spData_input.get(), spCoord_input.get());
	std::cout << "Predict received: " << reply << std::endl;

	return 0;
}



