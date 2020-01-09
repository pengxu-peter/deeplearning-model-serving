# 1 引言
## 1.1 目的和范围
直接将pb模型转为tensorRT_serving调用的“.graphdef”模型。   

## 1.2 文档约定


# 2 环境要求

1. 完成模型加载
2. 本地有以下python第三方库：
    - tensorflow
    - keras

- 推荐镜像: 

# 3 生成pb文件流程

## 3.1 修改文件get_input_output.py

获取pb文件的input和output。

## 3.2 修改文件get_graphdef_model.py

获取最终的.graphdef文件

## 3.3 准备config文件

每一个模型会对应一个config文件。config文件包含了模型的最基本信息，主要有name、platform、max_batch_size、input和output。   
name:与模型文件夹名称一致   
platform: tensorflow_graphdef   
max_batch_size: 最大可以接受的batch_size   
input:模型输入节点的名称   
output:模型输出节点的名称   

# 4 示例
输入的pb文件：[detector_3d](2_model_transfer_TF/2_mount/demo/gpu_models/detector_3d)
输出的graphdef文件：[detector_3d](3_model_transfer_TRT/3_mount/demo/trt_gpu_models/detector_3d)

# 5 参考文件
[TRT官方文档](https://docs.nvidia.com/deeplearning/sdk/inference-server-archived/tensorrt_inference_server_130/tensorrt-inference-server-guide/docs/model_configuration.html?highlight=tensorflow_savedmodel)   
[TRT官方GitHub](https://github.com/NVIDIA/tensorrt-inference-server)