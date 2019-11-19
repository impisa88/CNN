# Convolutional Neural Network
# -*- coding: utf-8 -*-
# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# Install Tensorflow from the website: https://www.tensorflow.org/versions/r0.12/get_started/os_setup.html

# Installing Keras
# pip install --upgrade keras

# Part 1 - Building the CNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.models import model_from_json
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt
import os


# Initialising the CNN
modelo = Sequential()

# Step 1 - Convolution
modelo.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))

# Step 2 - Pooling
modelo.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer
modelo.add(Convolution2D(32, 3, 3, activation = 'relu'))
modelo.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
modelo.add(Flatten())

# Step 4 - Full connection
modelo.add(Dense(output_dim = 128, activation = 'relu'))
modelo.add(Dense(output_dim = 1, activation = 'sigmoid'))

# Compiling the CNN
modelo.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('/home/joao/Imagens/dataset/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')

test_set = test_datagen.flow_from_directory('/home/joao/Imagens/dataset/test_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')

modelo.fit_generator(training_set,
                         samples_per_epoch = 4000,
                         nb_epoch = 1,
                         validation_data = test_set,
                         nb_val_samples = 300)

#salvando modelo

modelo_salvo = modelo.to_json()
with open("modelo.json", "w") as json_file:
    json_file.write(modelo_salvo)
modelo.save_weights("modelo.h5")

#carregando modelo
json_file = open("modelo.json","r")
modelo_carregado = json_file.read()
json_file.close()
modelo_carregado_final = model_from_json(modelo_carregado)
modelo_carregado_final.load_weights("modelo.h5")


#somente para segunda rede neural


class_names = ['legumes', 'carboidrato', 'proteina', 'outros']


plt.figure(figsize=(10,10))
for i in range(4):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[nomes[i]])
plt.show()

predicao = modelo_carregado_final.predict(test_set)

predicao[0]
np.argmax(predicao[0])

img = test_images[0]
img = (np.expand_dims(img,0))
predictions_single = model.predict(img)
plot_value_array(0, predictions_single, test_labels) = plt.xticks(range(10), class_names, rotation=45)

#https://www.tensorflow.org/tutorials/keras/classification
