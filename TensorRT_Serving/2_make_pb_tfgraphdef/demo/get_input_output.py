import os
from utils.saved_model_cli import show


def get_input_output(model_name):
    ori_gpu_model_dir = "/data/jiapf/3.6.0.5/model/gpu_models/"
    model_path = os.path.join(ori_gpu_model_dir, model_name, "1")
    show(model_path)


get_input_output("25d_retinanet")
