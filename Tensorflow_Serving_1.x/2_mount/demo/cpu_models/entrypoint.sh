#!/bin/sh
#/bin/bash
tensorflow_model_server --port=19000 --model_config_file=/data/xray_models.conf&> /data/tf_cpu_log
