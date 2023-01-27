from dash import Dash, html, dcc, Input, Output, State, ctx, no_update
import dash_bootstrap_components as dbc
from create_app import app
from dash.exceptions import PreventUpdate
from load_model import prepare_image, top_k_pred, model, top_k_pred_pretty
import dash_uploader as du
from dash_uploader import UploadStatus
from PIL import Image
import os
import base64
import numpy as np

du.configure_upload(app, r'tmp/uploads')

single_upload = html.Div([

    # ---- Upload section ----
    dbc.Row([
        dcc.Store(id="single_image_session", storage_type="session"),
        dcc.Upload(
            id="upload_single",
            className="upload_file",
            filename="",
            accept="",
            contents="",
            multiple=False,
            children=[
                html.Button(
                    "Select a file",
                    id="btn_upload_single",
                    className="btn_upload",
                    disabled=False,
                    n_clicks=0
                )
            ]
        )
    ]),

    # ---- Show the results ----
    dbc.Row(
        children = [
            dbc.Col([
                html.Div(id="result_single_pred", children=[]),
                html.Div(id="result_single_img", children=[])
            ]),
            dbc.Col(
                html.Div(id="result_single_img")
            )
        ]
    )
])



def show_image(path):
    return html.Img(src=path)
     

@app.callback(
    Output("result_single_img", "children"),
    Output("result_single_pred", "children"),
    Input("upload_single", "contents"),
    Input("btn_upload_single", "n_clicks"))
def function(contents, n_clicks):
    while contents == "":               # don't proceed until user has selected a photo
        raise PreventUpdate

    preprocessed_image = prepare_image(contents)
    pred = model.predict(preprocessed_image)
    return show_image(contents), top_k_pred_pretty(top_k_pred(pred))
