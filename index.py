from dash import html
import dash_bootstrap_components as dbc

home = html.Div([
    dbc.Row([
        dbc.Col([
            html.Img(
                src="assets/images/elephant_b_00007.jpg",
                className="img_homepage"
            ),
            html.P("Benchmark image", className="small")
        ],
        width="auto"
        ),
        dbc.Col([
            html.Img(
                src="assets/images/cheetah_S1_I13_R1_PICT0472.JPG",
                className="img_homepage"
            ),
            html.P("Camera trap image", className="small")
        ],
        width="auto"
        )
    ],
    justify="center", 
    align="start"
    ),
    dbc.Row(
        dbc.Col(
            html.H3(
                className="index",
                children=[
                    """Welcome to our Wildlife Image Classifier, where 
                    discovering the natural world has never been easier. Our 
                    AI model can identify the most likely 
                    animal species present in your image, whether it's a 
                    photo from your phone, a digital camera or a camera trap. 
                    While our app may only provide the most likely animal 
                    classification, it's a powerful tool for helping you 
                    automate your classification process. 
                    Get started now and see what you can discover!"""
                ]
            ),
            width=9
        ),
        justify="center"
    )
])
