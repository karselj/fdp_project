from dash import Dash, html, dcc, Input, Output, State, no_update, ctx
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
from create_app import app
from load_model import model, prepare_single_image, top_k_single


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
    Input("upload_multi_img", "contents"),
    Input("upload_multi_img", "filename"),
    Input("btn_upload_multi", "n_clicks"))
def upload(contents, filename, n_clicks):
    while contents == "":               # don't proceed until user has selected a photo
        raise PreventUpdate

    predictions = dict()
    for i in range(0, len(contents)):
        preprocessed_image = prepare_single_image(contents[i])
        pred = model.predict(preprocessed_image)
        predictions[filename[i]] = top_k_single(pred)

    return f"{len(predictions)} images classified", predictions, {"display":"block"}


@app.callback(
    Output("download_json", "data"),
    Input("btn_download_json", "n_clicks"),
    Input("results_store", "data"))
def download(n_clicks, predictions):
    while "btn_download_json" != ctx.triggered_id:
        raise PreventUpdate

    return dict(content=str(predictions), filename="prediction_results.json")


# ---- Upload zip folder containing multiple files ----

