import grpc
import tensorflow as tf
import numpy as np
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc



def main():
    #make connection
    channel = grpc.insecure_channel(CHANNEL_ADDRESS,options=[('grpc.enable_retries', True), 
                                                            ('grpc.keepalive_timeout_ms',30000),
                                                            ('grpc.max_connection_age_ms',60000),
                                                            ('grpc.max_receive_message_length',100*1024*1024)])
    stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

    #config the serving request
    request = predict_pb2.PredictRequest()
    request.model_spec.name = MODEL_NAME
    request.model_spec.signature_name = 'predict'

    #if you have two inputs (nodule detector)
    data_input,coord_input =(np.ones((1,1,128,128,128)),np.ones((1,3,32,32,32)))
    request.inputs['data_input'].CopyFrom(
    tf.contrib.util.make_tensor_proto(data_input, dtype='float32'))
    request.inputs['coord_input'].CopyFrom(
    tf.contrib.util.make_tensor_proto(coord_input, dtype='float32'))

    #for one input
    # request.inputs['inputs'].CopyFrom(tf.contrib.util.make_tensor_proto(input, dtype='float32'))

    result = stub.Predict(request, 20)
    output = tf.make_ndarray(result.outputs['output'])
#    channel.close()
    return output
if __name__=='__main__':
    MODEL_NAME='3d_nodule_detector'
    GPU = True

    if GPU:
        CHANNEL_ADDRESS = '0.0.0.0:19001'
    else:CHANNEL_ADDRESS = '0.0.0.0:19000'
    out = main()
    print(out)
    
