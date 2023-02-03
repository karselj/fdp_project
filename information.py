from dash import html
import dash_bootstrap_components as dbc

results = {
    'hippopotamus':   0.89, 
    'secretary bird': 1.00,
    'wildebeest':     0.77, 
    'giraffe':        0.90, 
    'zebra':          0.93, 
    'leopard':        0.88,     
    'waterbuck':      0.74, 
    'warthog':        0.83, 
    'impala':         0.97,
    'hyena':          0.84, 
    'cheetah':        0.85, 
    'vervet monkey':  0.87, 
    'buffalo':        0.92, 
    'eland':          0.83, 
    'baboon':         0.90, 
    'lion':           0.84, 
    'elephant':       0.92
}

information = html.Div(
    children=[
        html.P(
            """Welcome to our wildlife image classification tool! Our tool is designed to 
            accurately classify images captured by camera traps and benchmark images, allowing 
            for the efficient and effective analysis of wildlife populations in their natural 
            habitats."""
        ),
        html.H4(
            "Features:",
            style={"textAlign":"left"}
        ),
        html.P(
            """Advanced machine learning algorithms trained on large datasets to accurately identify and classify different species of wildlife.
            Ability to process both camera trap images and benchmark images for comprehensive analysis.
            User-friendly interface for easy navigation and image classification.
            Fast and efficient processing to minimize wait times and allow for quick and accurate results.
            Integration with other wildlife tracking and monitoring systems for a comprehensive analysis of wildlife populations."""
        ),
        html.H4(
            "Usage:",
            style={"textAlign":"left"}
        ),
        html.P(
            """Our tool is designed to be used by wildlife biologists, conservationists, and other professionals 
            working in the field of wildlife management. Simply upload your camera trap or benchmark images, and 
            our tool will automatically classify the species present in each image. Results can be easily exported 
            for further analysis and reporting."""
        ),
        html.H4(
            "Benefits:",
            style={"textAlign":"left"}
        ),
        html.P(
            """Accurately and efficiently classify large numbers of camera trap images for improved understanding of 
            wildlife populations. Reduce manual labor and time spent on image classification, allowing for more focused 
            and effective analysis of wildlife data. Improved accuracy and consistency in image classification, 
            leading to more reliable and trustworthy results. Easy integration with other wildlife tracking and monitoring 
            systems for a comprehensive understanding of wildlife populations. We are committed to improving and updating 
            our tool to provide the most accurate and efficient image classification solutions for the wildlife management 
            community. If you have any questions or feedback, please don't hesitate to contact us."""
        ),
        html.H4(
            "Classes:",
            style={"textAlign":"left"}
        ),
        html.P(
            children=[
                """This model has achieved varying accuracies on the different classes:""",
                html.Ul([
                    html.Li(
                        dbc.Row([
                            dbc.Col(key.capitalize(), style={"textAlign":"left"}, width=6, lg=1, sm=6),
                            dbc.Col(str(value*100)+"%", style={"textAlign":"right"}, width=6, lg=1, sm=6)
                        ],justify="start")
                    ) for key, value in results.items()
                ])
            ]
        )
    ]
)