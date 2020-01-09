import os
import tensorflow as tf
from keras import backend as K

os.environ['CUDA_VISIBLE_DEVICES'] = '1'
trained_checkpoint_prefix = '/hdd/disk4/jiapf/model_file/chk/vgg_epoch=55_test_loss=0.1707.ckpt-55'
export_dir = os.path.join("/hdd/disk4/jiapf/model_file/ocr2/", '0')

graph = tf.Graph()
with tf.compat.v1.Session(graph=graph) as sess:
    # Restore from checkpoint
    loader = tf.compat.v1.train.import_meta_graph(trained_checkpoint_prefix + '.meta')
    loader.restore(sess, trained_checkpoint_prefix)

    # input tensor info! NOTE: Please specify your own input shape and num
    serialized_tf_example = tf.placeholder(tf.string, name='tf_example')
    feature_configs = {'x': tf.FixedLenFeature(shape=[56, 56, 3], dtype=tf.float32), }
    tf_example = tf.parse_example(serialized_tf_example, feature_configs)
    input_tensor = tf.identity(tf_example['x'], name='x')  # use tf.identity() to assign name

    # output tensor info! NOTE:Please specify your own input shape and num
    feature_configs_out = {'y': tf.FixedLenFeature(shape=[10], dtype=tf.float32), }
    tf_example = tf.parse_example(serialized_tf_example, feature_configs_out)
    output_tensor = tf.identity(tf_example['y'], name='y')  # use tf.identity() to assign name

    tensor_info_input = tf.saved_model.utils.build_tensor_info(input_tensor)
    tensor_info_output = tf.saved_model.utils.build_tensor_info(output_tensor)

    # Please set your own signature according to your number of input and output
    prediction_signature = (
        tf.saved_model.signature_def_utils.build_signature_def(
            inputs={'images': tensor_info_input},
            outputs={'result': tensor_info_output},
            method_name=tf.saved_model.signature_constants.PREDICT_METHOD_NAME))


    # Export checkpoint to SavedModel
    builder = tf.compat.v1.saved_model.builder.SavedModelBuilder(export_dir)

    builder.add_meta_graph_and_variables(
        # tags:SERVING,TRAINING,EVAL,GPU,TPU
        sess=K.get_session(),
        tags=[tf.saved_model.tag_constants.SERVING],
        signature_def_map={'serving_default': prediction_signature, },
    )

    builder.save()