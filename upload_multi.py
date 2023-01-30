from dash import Dash, html, dcc, Input, Output, State, no_update, ctx
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from create_app import app
from load_model import model, prepare_single_image, top_k_single, read_zip

import base64
from io import BytesIO
from zipfile import ZipFile


# https://dash.plotly.com/dash-core-components/download


multi_upload = html.Div([
    # ---- Information about single upload ----
    dbc.Row(
        justify="center",
        children=[
            html.P("This section will describe how this upload function works. Select multiple photos or a zip folder.")
        ]
    ),

    # ---- Upload section ----
    dbc.Row(
        justify="center",
        children=[
            # ---- Upload multiple image files ----
            dbc.Col(
                width="auto",
                children=[
                    dcc.Upload(
                        id="upload_multi_img",
                        filename="",
                        accept="image/*",
                        contents="",
                        multiple=True,
                        children=[
                            html.Button(
                                "Select multiple files",
                                id="btn_upload_multi",
                                className="btn_upload",
                                disabled=False,
                                n_clicks=0
                            )
                        ]
                    )
                ]
            ),
            # ---- Upload multiple files in a zipped folder ----
            dbc.Col(
                width="auto",
                children=[
                    dcc.Upload(
                        id="upload_multi_zip",
                        filename="",
                        accept=".zip",
                        contents="",
                        multiple=False,
                        children=[
                            html.Button(
                                "Select a zip folder",
                                id="btn_upload_multi_zip",
                                className="btn_upload",
                                disabled=False,
                                n_clicks=0
                            )
                        ]
                    )
                ]
            )
        ]
    ),

    # ---- Show results ----
    dbc.Row(
        dbc.Col(
            html.Div(
                children=[
                    dcc.Store(id="results_store"),
                    html.P(
                        id="results_multi_text",
                        children=[]
                    ),
                    html.Button(
                        "Download results as JSON",
                        id="btn_download_json",
                        className="btn_upload",
                        style={"display":"none"}
                    ),
                    dcc.Download(id="download_json")
                ]
            )
        )
    )
])


# --- Upload multiple image files ------
@app.callback(
    Output("results_multi_text", "children"),
    Output("results_store", "data"),
    Output("btn_download_json", "style"),

    # multiple image files
    Input("upload_multi_img", "contents"),
    Input("upload_multi_img", "filename"),
    State("upload_multi_img", "last_modified"),
    Input("btn_upload_multi", "n_clicks"),
    # zipped folder
    Input("upload_multi_zip", "contents"),
    [State("upload_multi_zip", "filename"),
    State("upload_multi_zip", "last_modified")],
    Input("btn_upload_multi_zip", "n_clicks"))
def upload(contents_img, filename_img, date_img, img_clicks,
           contents_zip, filename_zip, date_zip, zip_clicks):

    print(ctx.triggered_id)
    while ctx.triggered_id == None:       # don't proceed until user has selected a photo
        raise PreventUpdate
    
    predictions = dict()

    if ctx.triggered_id == "upload_multi_img":
        for i in range(0, len(contents_img)):
            preprocessed_image = prepare_single_image(contents_img[i])
            pred = model.predict(preprocessed_image)
            predictions[filename_img[i]] = top_k_single(pred)

        print(type(predictions))
        return f"{len(predictions)} images classified", predictions, {"display":"block"}

    

    elif ctx.triggered_id == "upload_multi_zip":

        pred, length = read_zip(contents_zip)

        return f"{length} images classified", pred, {"display":"block"}
  
    return no_update, no_update, no_update


# ---- Download JSON file ----
@app.callback(
    Output("download_json", "data"),
    Input("btn_download_json", "n_clicks"),
    Input("results_store", "data"))
def download(n_clicks, predictions):
    while "btn_download_json" != ctx.triggered_id:
        raise PreventUpdate

    return dict(content=str(predictions), filename="prediction_results.json")


