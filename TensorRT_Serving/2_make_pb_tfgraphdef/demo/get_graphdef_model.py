import os
import shutil
from utils.tf_freeze_graph import run_main
from utils.saved_model_cli import show


def get_graph(model_name):
    ori_gpu_model_dir = "/data/jiapf/3.6.0.5/model/gpu_models_bak/"
    saved_graph_model_dir = "/data/jiapf/3.6.0.5/model/gpu_models/"

    input_model_path = os.path.join(ori_gpu_model_dir, model_name, "1")

    saved_graph_model_path = os.path.join(saved_graph_model_dir, model_name, "1")
    if not os.path.exists(saved_graph_model_path):
       os.makedirs(saved_graph_model_path)

    # Please set the output node name according to 2.2.1 step
    output_node = "dense_1/Softmax"
    output_graph = os.path.join(saved_graph_model_path, 'model.graphdef')
    shutil.copyfile("/data/jiapf/3.6.0.5/model/gpu_models/3d_nodule_detector_temp/config.pbtxt",
                    os.path.join(saved_graph_model_dir, model_name, "config.pbtxt"))
    show(input_model_path)
    run_main(input_model_path, output_node, output_graph)


get_graph("sypotom_normal")