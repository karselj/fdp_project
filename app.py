from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from create_app import app
from menu import menu_row
import single_upload
import multi_upload



app.layout = dbc.Container([
    # Header
    dbc.Row([
        dbc.Col(
            html.Div(
                className="section_div",
                children=[
                    dbc.Row(
                        justify="evenly",
                        children=[
                            html.Button(
                                "WILDLIFE IMAGE CLASSIFICATION",
                                id="btn_home",
                                className="btn_home"
                            )
                        ]
                    ),
                    dbc.Row(
                        justify="evenly",
                        children=[
                            html.H4("this is a short description of the app")
                        ]
                    )
                ]
            )
        )
    ],
    justify="center"
    ),

    # Menu
    dbc.Row([
        dbc.Col(
            html.Div(
                menu_row,
                className="section_div"
            )
        )
    ],
    justify="evenly"
    ),

    # Contents section
    dbc.Row([
        dbc.Col(
            html.Div(
                id="div_contents",
                className="section_div",
                children=[]
            )
        )
    ])
])


if __name__ == "__main__":
    app.run_server(debug=True, port=3838)