#!/bin/sh
export CUDA_VISIBLE_DEVICES=0
#/bin/bash
trtserver --model-store=/data/&> /data/trt_run.log
