model = None    
graph = None

def predict(request):
    global model
    global graph
            
    from google.cloud import storage
    import pandas as pd
    import flask
    import tensorflow as tf
    import keras as k
    from keras.models import load_model
    from flask import jsonify
    
    def auc(y_true, y_pred):
        auc = tf.metrics.auc(y_true, y_pred)[1]
        k.backend.get_session().run(
                      tf.local_variables_initializer())
        return auc
    
    data = {"success": False}
    params = request.get_json()

    # download model if not cached    
    if not model:
        graph = tf.get_default_graph()
        
        bucket_name = "dsp_model_store_1"
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)

        blob = bucket.blob("serverless/keras/v1")
        blob.download_to_filename("/tmp/games.h5")
        model = load_model('/tmp/games.h5', 
                          custom_objects={'auc':auc})
    
    # apply the model 
    if "G1" in params: 
        new_row = { "G1": params.get("G1"),"G2": params.get("G2"), 
                    "G3": params.get("G3"),"G4": params.get("G4"), 
                    "G5": params.get("G5"),"G6": params.get("G6"), 
                    "G7": params.get("G7"),"G8": params.get("G8"), 
                    "G9": params.get("G9"),"G10":params.get("G10")}

        new_x = pd.DataFrame.from_dict(new_row, 
                                      orient = "index").transpose()               
     
        with graph.as_default():        
            data["response"]= str(model.predict_proba(new_x)[0][0])
            data["success"] = True
    
    return jsonify(data)
