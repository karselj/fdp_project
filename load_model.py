import base64
import numpy as np
from io import BytesIO
from operator import itemgetter
from zipfile import ZipFile

from dash import html
import dash_bootstrap_components as dbc

from tensorflow import keras
from keras.applications.densenet import preprocess_input
from keras.utils import img_to_array, load_img



# Load model
model = keras.models.load_model("ml_model/models/densenet121_v1.h5")



# ------ Single Image Upload ------------------------------------------------------------------------------------------
# Modified code from deeplizard - https://www.youtube.com/playlist?list=PLZbbT5o_s2xrwRnXk_yCPtnqqo4_u2YGL
# Added some code from tensorflow - https://www.tensorflow.org/api_docs/python/tf/keras/utils/load_img 
def prepare_single_image(contents):
    """Need as input the filepath of the image.
    Prepare image to be used as input in a densenet model."""

    if type(contents) == str:
        contents = contents.replace('data:image/jpeg;base64,', '')      # clean up data bytes string
        contents = base64.b64decode(contents)                           # decode from base64
    
    img = BytesIO(contents)                                         # convert to BytesIO object

    load = load_img(img, target_size=(224, 224))                    # load resized BytesIO object/image into PIL format
    img_array = img_to_array(load)                                  # convert image to numpy array
    img_array_expanded_dims = np.array([img_array])                 # convert single image to batch

    return preprocess_input(img_array_expanded_dims)


    
# Function to get top results from each test round
def top_k_single(pred, top_k=5):
    """Get the top-5 predictions for a given image.
    pred: results from model.predict()
    Returns a dictionary of results in format 'animal':'prediction' """

    classes = ['hippopotamus', 'secretarybird', 'wildebeest', 'giraffe', 'zebra', 'leopard', 'waterbuck', 
    'warthog', 'impala', 'hyena', 'cheetah', 'monkeyvervet', 'buffalo', 'eland', 'baboon', 'lion', 'elephant']

    total = dict()
    for i in pred:
        indices, L_sorted = zip(*sorted(enumerate(i), key=itemgetter(1), reverse=True))

        for j in range(top_k):
            total[classes[indices[j]]] = L_sorted[j]

    return total


def top_k_pred_pretty(dict):
    """Takes the top_k_pred results as input (dict) and outputs the result
    in a more readable way"""

    temp = list()
    for key, value in dict.items():
        # don't show values that are smaller than 1%
        if value > 0.009:
            temp.append([key, value])

    pretty = html.Div([
        dbc.Row([
            dbc.Col(html.H3("Results"))
        ]),
        dbc.Row([
            dbc.Col([
                # display the predicted species
                html.H4(
                    temp[r][0].capitalize(), 
                    style={"textAlign":"left"}
                ) for r in range(0, len(temp))
            ]),
            dbc.Col([
                # display the prediction for each species 
                html.H4(
                    f"{round(temp[r][1]*100,2)}"+" %", 
                    style={"textAlign":"right"}
                ) for r in range(0, len(temp))
            ])
        ])
    ])
    return pretty


# ------ Zip Folder Upload ------------------------------------------------------------------------------------------

# Modified code from:
# https://stackoverflow.com/questions/60729575/how-to-handle-uploaded-zip-file-in-dash-plotly
def read_zip(contents):
    content_string = contents.replace('data:application/zip;base64,', '')

    try:
        len(content_string)%4 == 0
    except:
        raise Exception

    content_decoded = base64.b64decode(content_string)
    # Use BytesIO to handle the decoded content
    zip_str = BytesIO(content_decoded)
    # Now you can use ZipFile to take the BytesIO output

    predictions = dict()

    with ZipFile(zip_str, "r") as folder:
        for img in folder.namelist():
            if "__MACOSX" not in img:
                preprocessed_image = prepare_single_image(folder.read(img))
                pred = model.predict(preprocessed_image)
                predictions[img] = top_k_single(pred)

    return predictions, len(predictions)

