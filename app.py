import shutil
import traceback
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from keras.models import model_from_json

from utils import model_utils

app = Flask(__name__)
CORS(app)

TRAINING_FILE_PATH = 'data/caesarian.csv'

# These will be populated at training time
model = None
model_columns = None

@app.route('/', methods=['GET'])
def index():
  return jsonify({'Welcome': 'That worked'})

@app.route('/train', methods=['GET'])
def train():
    df = pd.read_csv(TRAINING_FILE_PATH)

    # We use a global here so we can modify the model and list of column names
    global model_columns, model
    model_columns, model = model_utils.train(df)
    
    # save the model

    # serialize model to JSON
    model_json = model.to_json()
    with open(model_utils.MODEL_FILE_NAME + ".json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights(model_utils.MODEL_FILE_NAME + ".h5")
    print("Saved model to disk")

    return jsonify({'success': 'Model training successful'})

@app.route('/predict', methods=['POST'])
def predict():
    print(model)
    if model:
        try:
            input_df = pd.DataFrame(request.json)
            predictions = model_utils.predict(input_df, model, model_columns)
            return jsonify(predictions)
        except Exception as e:
            return jsonify({'error': str(e), 'trace': traceback.format_exc()})
    else:
        return jsonify({'error': 'Please train model before trying to predict'})

if __name__ == '__main__':
    try:
        # load json and create model
        json_file = open(model_utils.MODEL_FILE_NAME + '.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights(model_utils.MODEL_FILE_NAME + ".h5")
        print("Loaded model from disk")
    except Exception as e:
        print('No model here')
        print('Train first')
        print(str(e))
        model = None

    app.run(host='0.0.0.0', port=5000, debug=True)
