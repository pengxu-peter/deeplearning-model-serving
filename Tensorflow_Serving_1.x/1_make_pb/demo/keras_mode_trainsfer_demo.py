import keras
import keras.backend as K
from utils import server_model_converter
from utils.gpu_allocation import set_gpu
num_gpu = 1
set_gpu(num_gpu)

mal_model = keras.models.load_model('/data/model_weights/20181208/001_classification/epoch_49_acc_0.95_val_acc_0.92.hdf5')

server_model_converter.save_model_for_production(mal_model, version=1, path='/data/model_weights/publish/2d_classification')


