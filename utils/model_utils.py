import os
import time
import joblib
import pandas as pd
from keras import Sequential
from keras.layers import Dense
from keras.models import model_from_json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# fix random seed for reproducibility
np.random.seed(7)

# inputs
include = ['Age', 'DeliveryN', 'DeliveryT', 'Blood', 'Heart', 'Caesarian']
dependent_variable = include[-1]

MODEL_DIRECTORY = 'model'
MODEL_FILE_NAME = '%s/model' % MODEL_DIRECTORY

def train(df):
    df_ = df[include]
    print("Training data sample:\n", df_.head())

    # encode class values as integers
    enc_DeliveryN = pd.get_dummies(df_['DeliveryN'], prefix='DeliveryN')
    enc_DeliveryT = pd.get_dummies(df_['DeliveryT'], prefix='DeliveryT')
    enc_Blood = pd.get_dummies(df_['Blood'], prefix='Blood')

    # Normalize age
    scaler = MinMaxScaler()
    df_['Age'] = scaler.fit_transform(df_[['Age']])

    os.mkdir(MODEL_DIRECTORY)

    joblib.dump(scaler, MODEL_DIRECTORY + '/scaler.pkl')

    # create feature dataframe
    X = pd.concat([df_['Age'], enc_DeliveryN, enc_DeliveryT, enc_Blood, df_['Heart']], axis=1, sort=False)
    # create lable dataframe
    y = df_['Caesarian']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    print(X_train.head())
    print(y_train.head())

    # capture a list of columns that will be used for prediction
    model_columns = list(X_train.columns)

    model = Sequential()
    #First Hidden Layer
    model.add(Dense(4, activation='relu', kernel_initializer='random_normal', input_dim=12))
    #Second  Hidden Layer
    model.add(Dense(4, activation='relu', kernel_initializer='random_normal'))
    #Output Layer
    model.add(Dense(1, activation='sigmoid', kernel_initializer='random_normal'))

    #compile the model
    model.compile(optimizer='adam',loss='binary_crossentropy', metrics =['accuracy'])

    start = time.time()
    # fit the model
    model.fit(X_train,y_train, batch_size=10, epochs=100)
    scores = model.evaluate(X, y, verbose=0)
    print('Trained in %.1f seconds' % (time.time() - start))
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

    return model_columns, model


def predict(input_df, model, columns):
    print("Input data frame is...\n")
    print("-----------")
    print(input_df)
    print("-----------")

    # load json and create model
    json_file = open(MODEL_FILE_NAME + '.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # load weights into new model
    print(MODEL_FILE_NAME)
    loaded_model.load_weights(MODEL_FILE_NAME + ".h5")
    print("Loaded model from disk")

    # encode class values as integers
    enc_DeliveryN = pd.get_dummies(input_df['DeliveryN'], prefix='DeliveryN')
    enc_DeliveryT = pd.get_dummies(input_df['DeliveryT'], prefix='DeliveryT')
    enc_Blood = pd.get_dummies(input_df['Blood'], prefix='Blood')

    # Normalize age
    scaler = joblib.load(MODEL_DIRECTORY + '/scaler.pkl')
    input_df['Age'] = scaler.transform(input_df[['Age']])

    features = pd.concat([input_df, enc_DeliveryN, enc_DeliveryT, enc_Blood], axis=1, sort=False)
    features = features.reindex(columns=columns, fill_value=0)

    prediction = model.predict(features)[0][0]

    print('The prediction is')
    print(prediction)
    if prediction>0.5:
      prediction = 1
    else:
      prediction = 0

    return {'predictions': prediction}




