from dash import Dash, html, dcc, Input, Output, State, ctx
import dash_bootstrap_components as dbc
from create_app import app
from dash.exceptions import PreventUpdate

single_upload = html.Div([
    dbc.Row(
        children=[
            dbc.Col("hello"),
            dbc.Col("goodbye")
        ]
    ),
    dbc.Row([
        dbc.Col(
            dcc.Upload(
                id="upload_single",
                className="upload_file",
                filename="",
                accept="",
                contents="",
                multiple=False,
                children=html.Div([
                    "Drag and Drop or ",
                    html.A("Select a File")
                ])
            ),
            width=10
        )
    ],
    justify="center",
    align="evenly"
    ),
    dbc.Row([
        dbc.Col(
            html.Div(
                id="div_image_output",
                children=[]
            )
        )
    ])
])

def show_image(contents, filename):
    image = html.Div([
        dbc.Row([
            html.H5(filename)
        ],
        justify="center"
        ),
        dbc.Row([
            # Should have maximum size of image
            html.Img(
                className="show_image",
                src=contents)
        ],
        justify="center"
        )
    ])
    return image


@app.callback(
    Output("div_image_output", "children"),
    Input("upload_single", "contents"),
    Input("upload_single", "filename")
)
def function(contents, filename):
    if contents is not None:
        return show_image(contents, filename)
