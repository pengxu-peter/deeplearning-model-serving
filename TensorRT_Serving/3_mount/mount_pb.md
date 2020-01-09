# 1 引言
## 1.1 目的和范围
将pb模型挂载，便于其他工程直接调用。

## 1.2 文档约定


# 2 环境要求

1. 本地已经安装如下程序：
    - docker
    - docker-compose
    - nvidia-docker

2. 本地已经加载以下镜像 ```sudo docker images```：
    - nvcr.io/nvidia/tensorrtserver:19.06-py3

# 3 挂载流程
## 3.1 将模型拷贝到待挂载目录

模型挂载主要是将转换好的模型以及模型config文件按统一格式放在一个文件夹下。

## 3.3 执行挂载

### 3.3.1 运行指令挂载：

```bash
cd ..
sudo docker-compose up    #开启 serving
```

### 3.3.2 检测是否挂载成功：

通过文件夹中的tf log察看启动成功没

```bash
docker logs <container id>
```


# 4 参考文件
