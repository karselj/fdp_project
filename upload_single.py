from dash import Dash, html, dcc, Input, Output, State, ctx, no_update
import dash_bootstrap_components as dbc
from create_app import app
from dash.exceptions import PreventUpdate
from load_model import prepare_single_image, top_k_single, model, top_k_pred_pretty



single_upload = html.Div([
    # ---- Information about single upload ----
    dbc.Row(
        justify="center",
        children=[
            html.P("This section will describe how this upload function works.")
        ]
    ),

    # ---- Show the results ----
    dbc.Row(
        justify="evenly",
        children=[
            dbc.Col(  
                html.Div(id="result_single_pred"),
                width={"size":3, "offset":1}
            ),
            dbc.Col(
                html.Div(id="result_single_img"),
                width={"size":6, "offset":2}
            )
        ]
    ),
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
                        accept="image/*",
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
def function(contents, n_clicks):
    while contents == "":               # don't proceed until user has selected a photo
        raise PreventUpdate

    preprocessed_image = prepare_single_image(contents)
    pred = model.predict(preprocessed_image)

    return top_k_pred_pretty(top_k_single(pred)), display_image(contents)
