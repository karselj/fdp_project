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

def pretty_output(dict):
    """takes the top_k_prediction as input (dict) 
    and outputs the result
    in a more readable way"""

    temp = list()
    for key, value in dict.items():
        # don't show values that are smaller than 1%
        if value > 0.009:
            temp.append([key, value])

    pretty = dbc.Row([
        dbc.Col([
            dbc.Row(html.H4(temp[r][0])) for r in range(0, len(temp))
        ]),
        dbc.Col([
            dbc.Row(html.H4(temp[r][1])) for r in range(0, len(temp))
        ])
    ])

    return pretty


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


# Callback to get image and run it through the machine learning model
# https://github.com/np-8/dash-uploader/blob/dev/docs/dash-uploader.md#duupload
@du.callback(
    output=Output("result", "children"),
    id="upload_single",
)
def callback_on_completion(status: UploadStatus):
    button_clicked = ctx.triggered_id

    if not button_clicked:
        raise PreventUpdate

    path = str(status.latest_file)
    preprocessed_image = prepare_image(path)
    pred = model.predict(preprocessed_image)

    return pretty_output(top_k_predictions(pred))