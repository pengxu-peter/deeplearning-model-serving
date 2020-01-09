import os
import keras
import tensorflow as tf
import keras.backend as K


def h5_to_serving_model(model_path, export_model_dir, model_version):
    model = keras.models.load_model(model_path)
    with tf.get_default_graph().as_default():
        tensor_info_input = tf.saved_model.utils.build_tensor_info(model.input)
        tensor_info_output = tf.saved_model.utils.build_tensor_info(model.output)

        # Please set your own signature according to your number of input and output
        prediction_signature = (
            tf.saved_model.signature_def_utils.build_signature_def(
                inputs={'images': tensor_info_input},
                outputs={'result': tensor_info_output},
                method_name=tf.saved_model.signature_constants.PREDICT_METHOD_NAME))
        print('step1 => prediction_signature created successfully')

        # set-up a builder
        export_path_base = export_model_dir
        export_path = os.path.join(
            tf.compat.as_bytes(export_path_base),
            tf.compat.as_bytes(str(model_version)))
        builder = tf.saved_model.builder.SavedModelBuilder(export_path)
        builder.add_meta_graph_and_variables(
            # tags:SERVING,TRAINING,EVAL,GPU,TPU
            sess=K.get_session(),
            tags=[tf.saved_model.tag_constants.SERVING],
            signature_def_map={'serving_default': prediction_signature,},
            )

        print('step2 => Export path(%s) ready to export trained model' % export_path, '\n starting to export model...')
        builder.save(as_text=True)

        print('Done exporting!')


h5_to_serving_model("/data/model_weights/20181208/001_classification/epoch_49_acc_0.95_val_acc_0.92.h5",
                    '/data/model_weights/publish/2d_classification',
                    1)
