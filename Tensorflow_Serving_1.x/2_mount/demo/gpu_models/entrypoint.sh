#!/bin/sh
export CUDA_VISIBLE_DEVICES=4
#/bin/bash
tensorflow_model_server --port=19001 --model_config_file=/data/gpu_models.conf&> /data/tf_gpu_log
