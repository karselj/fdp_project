from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from menu import menu_row
from create_app import app




app.layout = dbc.Container([
    html.Br(),
    # ---- Header and description ----
    dbc.Row(
        html.Div([
            html.Div(
                style={"display":"flex", "alignItems":"center"},
                children=[
                    html.Button(
                        "WILDLIFE IMAGE CLASSIFICATION",
                        id="btn_home",
                        className="btn_home"
                    )
                ]
            ),
            html.Hr(),
            html.H4("this is a short description of the app that should be centered")
        ])
    ),
    dbc.Row(
        className="g-0",
        justify="center",
        children=[
            html.Div(
                className="section_div",
                children=[
                    # ---- Menu ----
                    menu_row,
                    # ---- Contents ----
                    html.Div(
                        id="div_contents",
                        className="contents_div",
                        children=[]
                    )
                ]
            )
        ]
    ),
    html.Br()
])


if __name__ == "__main__":
    app.run_server(debug=True, port=3838)