# 1 引言
## 1.1 目的和范围
使用python脚本检查模型是否正常调用。

## 1.2 文档约定


# 2 环境要求

1. 完成模型加载
2. 本地有python环境，并安装以下第三方库：
    - grpc
    - numpy
    - tensorrtserver

# 3 测试流程
## 3.1 修改文件simple_client.py

a. 设置通信接口
```bash
  tensorRT Inference Server的通信接口包括http和gRPC
  
  protocol_type = "http"  # or "gRPC"  
  protocol = ProtocolType.from_str(protocol_type)
```

b.创建inference接口  
```bash
  ctx = InferContext(url, protocol, model_name, model_version, verbose)  
  
  args:  
  url: 格式为ip:端口（如果通信接口为http，则端口为8000；gRPC端口为8001）  
  protocol：上一步得到的通信接口  
  model_name：模型仓库中模型的名称  
  model_version:模型版本号。如果不指定，默认使用最新版本  
  verbose：是否打印模型详细信息  
```

c.将本地inference请求发送到server端进行推理，得到输出结果 
```bash
  此处需要输入signature name、输入数据，输出signature name、输出数据以及batch_size   
  result = ctx.run({ 'INPUT0' : (input0_data,)},   
                   { 'OUTPUT0' : InferContext.ResultFormat.RAW},  
                   batch_size)  
```

# 4 参考文件
