import argparse
import sys
import numpy as np
from builtins import range
from tensorrtserver.api import *

FLAGS = None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action="store_true", required=False, default=False,
                        help='Enable verbose output')
    parser.add_argument('-u', '--url', type=str, required=False, default='localhost:8000',
                        help='Inference server URL. Default is localhost:8000.')
    parser.add_argument('-i', '--protocol', type=str, required=False, default='http',
                        help='Protocol ("http"/"grpc") used to '
                        'communicate with inference service. Default is "http".')

    FLAGS = parser.parse_args()
    protocol = ProtocolType.from_str(FLAGS.protocol)

    # We use a simple model that takes 2 input tensors of 16 integers
    # each and returns 2 output tensors of 16 integers each. One
    # output tensor is the element-wise sum of the inputs and one
    # output is the element-wise difference.
    model_name = "simple"
    model_version = -1
    batch_size = 1

    # Create the inference context for the model.
    ctx = InferContext(FLAGS.url, protocol, model_name, model_version, FLAGS.verbose)

    # Create the data for the two input tensors. Initialize the first
    # to unique integers and the second to all ones.
    input0_data = np.arange(start=0, stop=16, dtype=np.int32)
    input1_data = np.ones(shape=16, dtype=np.int32)

    # Send inference request to the inference server. Get results for
    # both output tensors.
    result = ctx.run({ 'INPUT0' : (input0_data,),
                       'INPUT1' : (input1_data,)},
                     { 'OUTPUT0' : InferContext.ResultFormat.RAW,
                       'OUTPUT1' : InferContext.ResultFormat.RAW},
                     batch_size)

    # We expect there to be 2 results (each with batch-size 1). Walk
    # over all 16 result elements and print the sum and difference
    # calculated by the model.
    output0_data = result['OUTPUT0'][0]
    output1_data = result['OUTPUT1'][0]

    for i in range(16):
        print(str(input0_data[i]) + " + " + str(input1_data[i]) + " = " + str(output0_data[i]))
        print(str(input0_data[i]) + " - " + str(input1_data[i]) + " = " + str(output1_data[i]))
        if (input0_data[i] + input1_data[i]) != output0_data[i]:
            print("error: incorrect sum");
            sys.exit(1)
        if (input0_data[i] - input1_data[i]) != output1_data[i]:
            print("error: incorrect difference");
            sys.exit(1)
