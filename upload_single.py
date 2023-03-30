from dash import html, dcc, Input, Output, ctx
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

from create_app import app
from load_model import prepare_single_image, top_k_single, top_k_table, model



single_upload = html.Div([
    # ---- Information about single upload ----
    dbc.Row(
        justify="center",
        children=[
            html.P(
                className="upload_text",
                children=[
                    """Identify the animal in your photo with just a few clicks!
                    Upload a single photo to our Wildlife Image Classifier 
                    and our AI model will analyze it to determine what species 
                    is present in the image. Our 
                    easy-to-use interface makes it simple to upload and classify 
                    your photos quickly and accurately. To get multiple photos
                    classified at the same time, go to the page for multi upload.
                    The model can only classify images in jpeg format!"""
                ]
            )
        ]
    ),
    html.Hr(className="green"),
    html.Br(),

    # ---- Show the results ----
    dcc.Loading(
        id="loader_single",
        style={"display":"none"},
        type="circle",
        color="#B85042",   # --green3
        children=[
            dbc.Row([
                dbc.Col(  
                    html.Div(id="result_single_pred"),
                    width="auto"
                ),
                dbc.Col(
                    html.Div(id="result_single_img"),
                    width="auto"
                )
            ],
            justify="center",
            align="center"
            )
        ] 
    ),
    html.Br(),
    html.Br(),

    # ---- Upload section ----
    dbc.Row(
        justify="center",
        children=[
            dbc.Col(
                width="auto",
                children=[
                    dcc.Upload(
                        id="upload_single",
                        filename="",
                        accept=".jpg",
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
                ]
            )
        ]
    )
])



def display_image(path):
    return html.Img(
        src=path,
        className="img_show_one")
     

@app.callback(
    Output("result_single_pred", "children"),
    Output("result_single_img", "children"),
    Input("upload_single", "contents"),
    Input("btn_upload_single", "n_clicks"))
def return_prediction(contents, n_clicks):
    # don't proceed until user has selected a photo
    while contents == "":               
        raise PreventUpdate

    preprocessed_image = prepare_single_image(contents)
    pred = model.predict(preprocessed_image)

    table = dbc.Table.from_dataframe(
        top_k_table(top_k_single(pred, 10)),
        class_name="table table_results",           
        striped=True,
        bordered=True,
        hover=True)
                        


    return table, display_image(contents)


# --- Hide loader until button is clicked -----
@app.callback(
    Output("loader_single", "style"),
    Input("btn_upload_single", "n_clicks"))
def load_single(n_clicks):
    while "btn_upload_single" != ctx.triggered_id:
        raise PreventUpdate
    return {"display":"block"}
