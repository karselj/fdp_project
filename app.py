from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

app = Dash(__name__, 
           external_stylesheets=[dbc.themes.BOOTSTRAP, "/assets/style.css"])


app.layout = dbc.Container([
    # Header row
    dbc.Row([
        dbc.Col(
            html.H1("Hello dash")
        )
    ]),
    # Content row
    dbc.Row([
        # Left sidebar for menu items
        dbc.Col(
            "Sidemenu",
            width=3
        ),
        # Main column for other content, this is the only one that will update
        # -- in the callbacks
        dbc.Col(
            "Content",
            width=9
        )
    ],
    justify="evenly"
    )
])


if __name__ == "__main__":
    app.run_server(debug=True, port=3838)