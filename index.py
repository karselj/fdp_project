from dash import html
import dash_bootstrap_components as dbc

home = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Row(
                html.Img(
                    src="assets/images/elephant_b_00007.jpg",
                    className="img_homepage"
                )
            ),
            dbc.Row([
                dbc.Col(
                    html.P("Benchmark image", className="small")
                ),
                dbc.Col(
                    html.P("Source: personal collection", className="small", style={"textAlign":"right"})
                )
            ],
            justify="between"
            )
        ],
        width="auto"
        ),
        dbc.Col([
            dbc.Row(
                html.Img(
                    src="assets/images/cheetah_S1_I13_R1_PICT0472.JPG",
                    className="img_homepage"
                )
            ),
            dbc.Row([
                dbc.Col(
                    html.P("Camera trap image", className="small")
                ),
                dbc.Col(
                    html.P(
                        children=[
                            "Source: ",
                            html.A("Snapshot Safari", 
                                href="https://www.snapshotsafari.org", 
                                target="_blank"), ], 
                        className="small", 
                        style={"textAlign":"right"})
                )
            ],
            justify="between"
            )
        ],
        width="auto"
        )
    ],
    justify="center", 
    align="start"
    ),
    dbc.Row(
        dbc.Col([
            html.H3(
                className="index",
                children=[
                    """Welcome to the Wildlife Image Classifier. This 
                    AI model can identify the species of wildlife present 
                    in your image*, whether it's an image from your phone, 
                    a digital camera or a camera trap. Get started now and 
                    see what you can discover!"""
                ]
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.P(
                className="small",
                children=[
                    """*While this app may only provide the most likely 
                    classification, it's a powerful tool for helping you 
                    automate your classification process. See a list of the 
                    performance on each animal that the model can identify 
                    on the information page."""
                ]
            )
        ],
        width=9
        ),
    justify="center"
    )
])
