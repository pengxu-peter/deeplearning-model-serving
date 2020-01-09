import grpc
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import model_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc
from tensorflow_serving.apis import get_model_metadata_pb2


CHANNEL_ADDRESS = r'172.16.104.25:19001'
MODEL_NAME = r'3d_nodule_detector'

channel = grpc.insecure_channel(CHANNEL_ADDRESS)
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

request = get_model_metadata_pb2.GetModelMetadataRequest(
    model_spec=model_pb2.ModelSpec(name=MODEL_NAME),
    metadata_field=["signature_def"])

response = stub.GetModelMetadata(request)
sigdef_str = response.metadata["signature_def"].value

print ("Name:", response.model_spec.name)
print ("Version:", response.model_spec.version.value)
print (get_model_metadata_pb2.SignatureDefMap.FromString(sigdef_str))

