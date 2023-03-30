from dash import html
import dash_bootstrap_components as dbc
import pandas as pd

results = {
    'hippopotamus':   0.78, 
    'secretary bird': 0.79,
    'wildebeest':     0.71, 
    'giraffe':        0.84, 
    'zebra':          0.91, 
    'leopard':        0.70,     
    'waterbuck':      0.69, 
    'warthog':        0.64, 
    'impala':         0.89,
    'hyena':          0.69, 
    'cheetah':        0.62, 
    'vervet monkey':  0.65, 
    'buffalo':        0.64, 
    'eland':          0.75, 
    'baboon':         0.73, 
    'lion':           0.67, 
    'elephant':       0.86
}

df = pd.DataFrame(columns=["Species", "F1-Score"])
for key, value in results.items():
    if value > 0.009:
        df2 = pd.DataFrame([[key.capitalize(), (f'{value:.2f}')]], 
                           columns=["Species", "F1-Score"])
        df = pd.concat([df, df2])


information = html.Div(
    dbc.Row([
        dbc.Col([
            html.P(
                """Our tool is designed to be used by wildlife biologists, 
                conservationists, and other professionals working in the 
                field of wildlife management. Simply upload your image and 
                our tool will automatically classify the species present 
                in each image. Results containing the top-5 predicted species 
                and the confidence score for each image can easily be downloaded 
                in JSON format for further analysis and reporting."""
            ),
            html.H4(
                "Technicalities:",
                style={"textAlign":"left"}
            ),
            html.P([
                """The machine learning model used in this tool is a deep neural 
                network of the  """,
                html.A("DenseNet-121 architecture", 
                       href="https://arxiv.org/abs/1608.06993", 
                       target="_blank"),  
                """. It is trained on approximately 11.000 images of types camera trap 
                and benchmark. We define benchmark images as images where the animal is 
                the main focal point, for example, the first image you would get on a 
                google search on a species. It can therefore classify most kinds of 
                images, though with varying accuracies. The camera trap training data 
                comes from the """, 
                html.A("Snapshot Safari", 
                       href="", 
                       target="_blank"), 
                """ project, therefore, this tool is designed to be used by teams 
                across the African continent. On our test data, the model achieved 
                an accuracy of 94% on benchmark images and 56% on camera trap images 
                from unseen locations. \n Note that the model is not 100% accurate 
                and results should be verified by a human. However, if prediction 
                confidence is over 90% the prediction is correct 95% of the times. 
                The model is only designed to detect one species in an image, 
                therefore, it can be inaccurate if several different species are 
                present. Currently, the app can only classify images in jpeg format."""
            ]),
            html.H4(
                "Benefits:",
                style={"textAlign":"left"}
            ),
            html.P(
                """Reduce manual labor and time spent on classifying animals in images, 
                and allow for more focused and effective analysis of the data. We are 
                committed to improving and updating our tool to provide the most 
                accurate and efficient image classification solutions for the wildlife 
                management community. If you have any questions or feedback, 
                please don't hesitate to contact us at karsel51006@stud.noroff.no."""
            )
        ]),
        dbc.Col([
            html.H4(
                """The achieved the following F1-Score on our test set:""",
                style={"textAlign":"left"}
            ),
            html.Hr(className="green"),
            dbc.Table.from_dataframe(
                        df.sort_values(["Species"]),
                        class_name="table table_information",           
                        striped=True,
                        bordered=True,
                        hover=True
            )
        ])
    ],
    justify="evenly")
)