from dash import html
import dash_bootstrap_components as dbc
import pandas as pd

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

df = pd.DataFrame(columns=["Species", "Recall"])
for key, value in results.items():
    if value > 0.009:
        df2 = pd.DataFrame([[key.capitalize(), (f'{value:.2f}')]], columns=["Species", "Recall"])
        df = pd.concat([df, df2])


information = html.Div(
    dbc.Row([
        dbc.Col([
            html.H4(
                "Features:",
                style={"textAlign":"left"}
            ),
            html.P(
                """Advanced machine learning algorithm trained on large datasets to accurately identify and classify different species of wildlife.
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
                working in the field of wildlife management. Simply upload your image and 
                our tool will automatically classify the species present in each image. Results containing the 
                top-5 predicted species for each image can easily be exported in JSON format
                for further analysis and reporting. \n Note that the model is not 100% accurate and results should be 
                verified by a human. However, if model prediction is over 90% the species is usually predicted correctly. 
                The model is only designed to detect one species in an image, therefore, it can be inaccurate if several
                different species are present."""
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
                "Species:",
                style={"textAlign":"left"}
            ),
            html.P(
                children=[
                    """During testing the model achieved the following accuracy per species:""",
                ]
            )
        ]
        ),
        dbc.Col([
            dbc.Table.from_dataframe(
                        df.sort_values(["Species"]),
                        class_name="table table_information",           
                        striped=True,
                        bordered=True,
                        hover=True
            )
        ]
        )
    ],
    justify="evenly")
)