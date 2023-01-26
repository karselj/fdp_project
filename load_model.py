import numpy as np
import io
import base64
from PIL import Image
from operator import itemgetter
from dash import html

import tensorflow as tf
from tensorflow import keras

from keras.applications import imagenet_utils
from keras.applications.densenet import preprocess_input

from keras.preprocessing.image import ImageDataGenerator
from keras.utils import img_to_array, load_img



# Modified code from deeplizard - https://www.youtube.com/playlist?list=PLZbbT5o_s2xrwRnXk_yCPtnqqo4_u2YGL
def prepare_image(image):
    """Need as input the filepath of the image."""
    img = load_img(image, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    
    return preprocess_input(img_array_expanded_dims)


# Function to get top 5 results from each test round
def top_k_predictions(pred, top_k=5):
    classes = ['hippopotamus', 'secretarybird', 'wildebeest', 'giraffe', 'zebra', 'leopard', 'waterbuck', 
    'warthog', 'impala', 'hyena', 'cheetah', 'monkeyvervet', 'buffalo', 'eland', 'baboon', 'lion', 'elephant']

    total = dict()
    for i in pred:
        indices, L_sorted = zip(*sorted(enumerate(i), key=itemgetter(1), reverse=True))

        for j in range(top_k):
            total[classes[indices[j]]] = L_sorted[j]
    print(str(total))
    return total


model = keras.models.load_model("ml_model/models/densenet121_v1.h5")