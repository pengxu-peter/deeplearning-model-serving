# 1 引言
## 1.1 目的和范围
生成tensorRT_serving调用的pb模型。直接由h5文件生成pb文件，供TensorRT Serving调用。   

## 1.2 文档约定


# 2 环境要求

1. 完成模型加载
2. 本地有以下python第三方库：
    - tensorflow
    - keras

# 3 生成pb文件流程

## 3.1 修改文件convert_h5_to_pb.py

1. H5模型转PB里面的convert_h5_to_pb.py将h5文件转换成pb文件。
注意
- 将prediction_signature设置为你自己模型的名字以及输入输出个数。
- signature_def_map必须指定为serving_default，以免不识别

## 3.2 准备config文件

每一个模型会对应一个config文件。config文件包含了模型的最基本信息，主要有name、platform、max_batch_size、input和output。   
name:与模型文件夹名称一致   
platform: tensorflow_savedmodel   
max_batch_size: 最大可以接受的batch_size   
input:模型输入节点的名称   
output:模型输出节点的名称   

# 4 示例
输出pb文件目录：[cardiac_seg](3_model_transfer_TRT/3_mount/demo/trt_gpu_models/cardiac_seg)

# 5 参考文件
[TRT官方文档](https://docs.nvidia.com/deeplearning/sdk/inference-server-archived/tensorrt_inference_server_130/tensorrt-inference-server-guide/docs/model_configuration.html?highlight=tensorflow_savedmodel)   
[TRT官方GitHub](https://github.com/NVIDIA/tensorrt-inference-server)
