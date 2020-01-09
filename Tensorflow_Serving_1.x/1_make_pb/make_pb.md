# 1 引言
## 1.1 目的和范围
生成tensorflow_serving调用的pb模型。

## 1.2 文档约定


# 2 环境要求

1. 完成模型加载
2. 本地有以下python第三方库：
    - tensorflow
    - keras

# 3 生成pb文件流程

## 3.1 修改文件keras_mode_trainsfer_demo.py

1. 指定模型路径
2. 指定生成路径及version文件夹名称

## 3.2 运行程序

```bash
python keras_mode_trainsfer_demo.py
```

# 4 示例
输出pb文件目录：[detector_3d](2_model_transfer_TF/2_mount/demo/gpu_models/detector_3d)

# 5 参考文件
