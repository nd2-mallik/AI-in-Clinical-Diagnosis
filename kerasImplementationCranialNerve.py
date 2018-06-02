# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 09:58:51 2018

@author: Mallikarjun Dodmani
"""

# Visualize training history
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy
import pandas
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
import keras.backend as K
def mean_pred(y_true, y_pred):
    return K.mean(y_pred)
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load pima indians dataset
#datasetIn = numpy.loadtxt(r"C:\Users\DST_AI\Desktop\Test_Data/CNInput.csv", delimiter=",")
#datasetOut = numpy.loadtxt(r"C:\Users\DST_AI\Desktop\Test_Data/CNDR.csv", delimiter=",")

dataframe1 = pandas.read_csv(r"C:\Users\DST_AI\Desktop\Test_Data/CNInputEncoded.csv", delimiter=",")
datasetIn = dataframe1.values
X = datasetIn[:,0:104]
print('X',X)
Y = datasetIn[:,104]
print('y',Y)
# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)

# split into input (X) and output (Y) variables
#X = datasetIn[:,0:103]
#Y = datasetOut[:,0]
# create model
model = Sequential()
model.add(Dense(100, input_dim=104, kernel_initializer='uniform', activation='relu'))
model.add(Dense(100, kernel_initializer='uniform', activation='relu'))
model.add(Dense(100, kernel_initializer='uniform', activation='relu'))
model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy', 'mse', 'mae', 'mape'])
# Fit the model
history = model.fit(X, Y, validation_split=0.33, epochs=500, batch_size=10, verbose=0)
# list all data in history
print(history.history.keys())
# summarize history for accuracy
# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
print("\n%s: %.2f%%" % (model.metrics_names[2], scores[2]))
print("\n%s: %.2f%%" % (model.metrics_names[3], scores[3]))
print("\n%s: %.2f%%" % (model.metrics_names[4], scores[4]))
predictions = model.predict(X)
# round predictions
rounded = [round(x[0]) for x in predictions]
# =============================================================================
# model_json = model.to_json()
# with open("model.json", "w") as json_file:
#     json_file.write(model_json)
# # serialize weights to HDF5
# model.save_weights("model.h5")
# from keras.layers import Dense
# from keras.models import model_from_json
# import os
# # load json and create model
# json_file = open('model.json', 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# loaded_model = model_from_json(loaded_model_json)
# # load weights into new model
# loaded_model.load_weights("model.h5")
# loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy', mean_pred])
# score = loaded_model.evaluate(X, Y, verbose=0)
# =============================================================================
#print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Cranial Nerve Model Accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Cranial Nerve Model Loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(history.history['mean_squared_error'])
plt.plot(history.history['mean_absolute_error'])
plt.plot(history.history['mean_absolute_percentage_error'])
plt.legend(['mse', 'mae', 'mape'], loc='upper left')
plt.title('Error plot')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.show()
