from dash import Dash, html, dcc, Input, Output, State, ctx, no_update
import dash_bootstrap_components as dbc
from create_app import app

home = html.Div(
    html.H2("hello this is my app")
)