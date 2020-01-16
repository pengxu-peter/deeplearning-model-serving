<p align="center">
  <img alt="vscode logo" src="imgs/logo.jpg" width="100px" />
  <h1 align="center">Integrated Development Environment Documentation</h1>
</p>

本项目用于汇总深度学习模型做Serving的配置，主要包括Tensorflow Serving 1.x, TensorRT Serving。


## 目录
   
1. Tensorflow Serving 1.x [tensorflow/serving:1.13.0-gpu]
    - 1 [生成TF模型](Tensorflow_Serving_1.x/1_make_pb/make_pb.md)
    - 2 [挂载TF模型](Tensorflow_Serving_1.x/2_mount/mount_pb.md)
    - 3 [python代码验证TF模型是否正常挂载](Tensorflow_Serving_1.x/3_python_check/pb_python_check.md)
    - 4 [cpp代码验证TF模型是否正常挂载](Tensorflow_Serving_1.x/4_cpp_check/pb_cpp_check.md)

2. TensorRT Serving [nvcr.io/nvidia/tensorrtserver::19.06-py3]
    - 1 [生成TRT模型-tensorflow_savedmodel](TensorRT_Serving/1_make_pb_tfsavedmodel/make_pb.md)
    - 2 [生成TRT模型-tensorflow_graphdef](TensorRT_Serving/2_make_pb_tfgraphdef/make_pb.md)
    - 3 [挂载pb模型](TensorRT_Serving/3_mount/mount_pb.md)
    - 4 [python代码验证TRT模型是否正常挂载](TensorRT_Serving/4_python_check/pb_python_check.md)

  
## 参考资料
[TensorFlow 2.0 部署：TensorFlow Serving](https://mp.weixin.qq.com/s?src=11&timestamp=1579152232&ver=2099&signature=TmY2z14SJ31LGwNig9*mHTjow8ui7OlhN3KLVt-qVmvwmhnBjX2it-htz2fWackJiQZPJzdyEhLKUzV*NyUby4uXeNYjCaYm*hBiUffP87H*WxjcjSqLHaKVkSUW2CvI&new=1)


