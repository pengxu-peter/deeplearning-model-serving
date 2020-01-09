import os
import tensorflow as tf
import keras.backend as K

def save_model_for_production(model, version, path='prod_models'):
    ''' A function that convert keras model to tensorflow server model
    Input:
        model: keras model need to be converted
        version: The version of the model
        path: Export path
    Return: 
        None (converted model has been saved to the path)
    '''
    tf.reset_default_graph()
    # Set the learning phase to 0 for model testing
    K.set_learning_phase(0)
    if not os.path.exists(path):
        os.makedirs(path)
    
    # Create export path for the converted model
    export_path = os.path.join(
        tf.compat.as_bytes(path),
        tf.compat.as_bytes(str(version)))
    
    # start the server model builder and define the prediction signature
    builder = tf.saved_model.builder.SavedModelBuilder(export_path)
    model_input = tf.saved_model.utils.build_tensor_info(model.input)
    model_output = tf.saved_model.utils.build_tensor_info(model.output)
    
    #Note inputs and ouput are the names you should use later when making request to predict.
    prediction_signature = (
        tf.saved_model.signature_def_utils.build_signature_def(
            inputs={'inputs': model_input},
            outputs={'output': model_output},
            method_name=tf.saved_model.signature_constants.PREDICT_METHOD_NAME))
   
    # save the graph and meta data into the model 
    with K.get_session() as sess:
        builder.add_meta_graph_and_variables(
            sess=sess, tags=[tf.saved_model.tag_constants.SERVING],
            signature_def_map={
                'predict':
                    prediction_signature,
            })

        builder.save()
        
        
        
def save_ssd_model_for_production(model, version, path='prod_models'):
    ''' A function that convert keras model to tensorflow server model
    Input:
        model: keras model need to be converted
        version: The version of the model
        path: Export path
    Return: 
        None (converted model has been saved to the path)
    '''
    tf.reset_default_graph()
    # Set the learning phase to 0 for model testing
    K.set_learning_phase(0)
    if not os.path.exists(path):
        os.makedirs(path)
    
    # Create export path for the converted model
    export_path = os.path.join(
        tf.compat.as_bytes(path),
        tf.compat.as_bytes(str(version)))
    
    # start the server model builder and define the prediction signature
    builder = tf.saved_model.builder.SavedModelBuilder(export_path)
    model_input = tf.saved_model.utils.build_tensor_info(model.input)
    location_output = tf.saved_model.utils.build_tensor_info(model.output[0])
    probability_output = tf.saved_model.utils.build_tensor_info(model.output[1])
    
    #Note inputs and ouput are the names you should use later when making request to predict.
    prediction_signature = (
        tf.saved_model.signature_def_utils.build_signature_def(
            inputs={'inputs': model_input},
            outputs={'location': location_output,
                  'probability': probability_output,
                    },
            method_name=tf.saved_model.signature_constants.PREDICT_METHOD_NAME))
   
    # save the graph and meta data into the model 
    with K.get_session() as sess:
        builder.add_meta_graph_and_variables(
            sess=sess, tags=[tf.saved_model.tag_constants.SERVING],
            signature_def_map={
                'predict':
                    prediction_signature,
            })

        builder.save()
        
        
def save_nod_model_for_production(model, version, path='prod_models'):
    ''' A function that convert keras model to tensorflow server model
    Input:
        model: keras model need to be converted
        version: The version of the model
        path: Export path
    Return: 
        None (converted model has been saved to the path)
    '''
    # Set the learning phase to 0 for model testing
    K.set_learning_phase(0)
    if not os.path.exists(path):
        os.mkdir(path)
    
    # Create export path for the converted model
    export_path = os.path.join(
        tf.compat.as_bytes(path),
        tf.compat.as_bytes(str(version)))
    
    # start the server model builder and define the prediction signature
    builder = tf.saved_model.builder.SavedModelBuilder(export_path)
    data_input = tf.saved_model.utils.build_tensor_info(model.input[0])
    coord_input = tf.saved_model.utils.build_tensor_info(model.input[1])
    model_output = tf.saved_model.utils.build_tensor_info(model.output)

    #Note inputs and ouput are the names you should use later when making request to predict.
    prediction_signature = (
        tf.saved_model.signature_def_utils.build_signature_def(
            inputs={'data_input': data_input,
                   'coord_input':coord_input},
            outputs={'output': model_output},
            method_name=tf.saved_model.signature_constants.PREDICT_METHOD_NAME))
    print "save model"
    # save the graph and meta data into the model 
    with K.get_session() as sess:
        builder.add_meta_graph_and_variables(
            sess=sess, tags=[tf.saved_model.tag_constants.SERVING],
            signature_def_map={
                'predict':
                    prediction_signature,
            })
        print "save the builder"

        builder.save()