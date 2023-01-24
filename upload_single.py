from dash import Dash, html, dcc, Input, Output, State, ctx
import dash_bootstrap_components as dbc
from create_app import app
from dash.exceptions import PreventUpdate
from load_model import prepare_image, top_k_predictions, model
import dash_uploader as du
from dash_uploader import UploadStatus
from IPython.display import Image

du.configure_upload(app, r'tmp/uploads')
single_upload = html.Div([
    dbc.Row(
        children=[
            dbc.Col("hello"),
            dbc.Col("goodbye")
        ]
    ),
    # ---- Upload section -----
    dbc.Row([
        dbc.Col(
            dbc.Row([
                # input field
                du.Upload(
                    id="upload_single",
                    text="Select a file",
                    text_completed="Uploaded: ",
                    filetypes=["jpeg", "jpg", "png", "JPG", "JPEG", "PNG"]
                )
            ]),
        )
    ],
    justify="center",
    align="evenly"
    ),

    dbc.Row([
        dbc.Col(
            html.Div(
                id="div_image_output",
                children=[
                    html.H2(id="result", children=[])
                ]
            )
        )
    ])
])

"""dcc.Upload(
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
)"""

# https://github.com/np-8/dash-uploader/blob/dev/docs/dash-uploader.md#duupload
@du.callback(
    output=Output("result", "children"),
    id="upload_single",
)
def callback_on_completion(status: UploadStatus):
    path = str(status.latest_file)

    preprocessed_image = prepare_image(path)
    pred = model.predict(preprocessed_image)
    print(path)
    return [top_k_predictions(pred), show_image(path)]


def show_image(contents):
    image = html.Div([
                dbc.Row([
                    # Should have maximum size of image
                    Image(filename=contents)
                    
                ],
                justify="center"
                )
            ])
    return image


"""@app.callback(
    Output("div_image_output", "children"),
    Input("upload_single", "contents"),
    Input("upload_single", "filename"),
    Input("btn_upload_single", "n_clicks")
)
def function(contents, filename, n_clicks):
    button_clicked = ctx.triggered_id
    if not button_clicked:
        print("im here")
        raise PreventUpdate
    else:
        img = convert_image(contents)
        preprocessed_image = prepare_image(img)
        pred = model.predict(preprocessed_image)
        
        return top_k_predictions(pred), show_image(contents, filename)"""
