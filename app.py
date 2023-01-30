from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from menu import menu_row
from create_app import app




app.layout = dbc.Container([
    # ---- Header and description ----
    dbc.Row(
        className="section_div",
        children=[
            dbc.Col([
                dbc.Row(
                    justify="center",
                    children=[
                        html.Button(
                            "WILDLIFE IMAGE CLASSIFICATION",
                            id="btn_home",
                            className="btn_home"
                        )
                    ]
                ),
                dbc.Row(
                    justify="center",
                    children=[
                        html.H4("this is a short description of the app that should be centered")
                    ]
                )
            ])
        ]
    ),

    # ---- Menu ----
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