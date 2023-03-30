from dash import html, dcc, Input, Output, State, no_update, ctx
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from create_app import app
from load_model import prepare_single_image, top_k_single, read_zip, model
import json


# https://dash.plotly.com/dash-core-components/download


multi_upload = html.Div([
    # ---- Information about single upload ----
    dbc.Row(
        justify="center",
        children=[
            html.P(
                className="upload_text",
                children=[
                    """Identify the animals in your photos with just a few clicks!
                    Select multiple photos or a zipped folder of photos, upload
                    them to our Wildlife Image Classifier and our AI model will 
                    analyze them to determine what species is present in each image.
                    Our easy-to-use interface makes it simple to upload and 
                    classify your images quickly and accurately. When the model 
                    has classified all images, click the download button to get 
                    the predictions for each photo in JSON format. To 
                    quickly classify a single photo, go to the page for single 
                    upload. The model can only classify images in jpeg format!"""
                ]
            )
        ]
    ),
    html.Hr(className="green"),
    # ---- Show results ----
    dbc.Row(
        dbc.Col([
            dcc.Store(id="results_store"),
            html.Br(),
            dcc.Loading(
                id="loader_multi",
                style={"display":"none"},
                type="circle",
                color="#A5B198",   # --green3
                children=[
                    html.P(
                        id="results_multi_text",
                        className="download_text",
                        style={"textAlign":"center"},
                        children=[]
                    ),
                    dcc.Download(id="download_json"),
                    html.Button(
                        "Download Top-5 predictions",
                        id="btn_download_json",
                        className="btn_download",
                        style={"display":"none"}
                    )
                ]
            )
        ],width="auto"),
    justify="center"
    ),
    html.Br(),
    html.Br(),
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
                        accept=".jpg",
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
    )
])


# --- Hide loader until button is triggered -----
@app.callback(
    Output("loader_multi", "style"),
    Input("btn_upload_multi", "n_clicks"),
    Input("btn_upload_multi_zip", "n_clicks"))
def load_multi(clicks_multi, clicks_zip):
    while ctx.triggered_id == None:
        raise PreventUpdate
    
    return {"display":"block"}


# --- Upload multiple image files ------
@app.callback(
    Output("results_multi_text", "children"),
    Output("results_store", "data"),
    Output("btn_download_json", "style"),

    # multiple image files
    Input("upload_multi_img", "contents"),
    Input("upload_multi_img", "filename"),
    Input("btn_upload_multi", "n_clicks"),

    # zipped folder
    Input("upload_multi_zip", "contents"),
    Input("btn_upload_multi_zip", "n_clicks"))
def upload(contents_img, filename_img, img_clicks,
           contents_zip, zip_clicks):
    
    # don't proceed until user has selected a photo
    while ctx.triggered_id == None:
        raise PreventUpdate
    
    predictions = dict()

    if ctx.triggered_id == "upload_multi_img":
        for i in range(0, len(contents_img)):
            preprocessed_image = prepare_single_image(contents_img[i])
            pred = model.predict(preprocessed_image)
            predictions[filename_img[i]] = top_k_single(pred)

        if len(predictions) == 1:
            return f"{len(predictions)} image classified", \
                     predictions, {"display":"block"}
        
        return f"{len(predictions)} images classified", \
                 predictions, {"display":"block"}

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
    
    return dict(content=json.dumps(predictions, indent=4), filename="predictions.json")
