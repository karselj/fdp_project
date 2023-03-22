from dash import html
import dash_bootstrap_components as dbc

home = html.Div(
    dbc.Row([
        dbc.Col(
            html.H3(
                className="index",
                children=[
                    "Welcome to our Wildlife Image Classifier web app, where \
                    discovering the natural world has never been easier. Our \
                    cutting-edge AI model can accurately identify the most likely \
                    animal species present in your uploaded image, whether it's a \
                    camera trap photo or a regular image. While our app may only \
                    provide the most likely animal classification, it's a powerful \
                    tool for helping you learn more about the creatures you \
                    encounter. Get started now and see what you can discover!"
                ]
            )
        ),
        dbc.Col([
            dbc.Row(
                html.Img(
                    src="assets/images/cheetah_S1_I13_R1_PICT0472.JPG",
                    className="img_homepage"
                )
            ),
            dbc.Row(
                html.Img(
                    src="assets/images/elephant_b_00007.jpg",
                    className="img_homepage"
                )
            )
        ])
    ])
)