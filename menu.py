from dash import Dash, html, dcc, Input, Output, State, ctx
import dash_bootstrap_components as dbc
from create_app import app
from single_upload import single_upload


menu_row = dbc.Row(
    className="g-0",
    justify="evenly",
    children = [
        dbc.Col(
            html.Button(
                "Info",
                id="btn_info",
                className="btn_menu",
                style={"display":"block"},
                disabled=False,
                n_clicks=0
            ),
            width=4
        ),
        dbc.Col(
            html.Button(
                "Single Upload",
                id="btn_single_upload",
                className="btn_menu",
                style={"display":"block"},
                disabled=False,
                n_clicks=0
            ),
            width=4
        ),
        dbc.Col(
            html.Button(
                "Multi Upload",
                id="btn_multi_upload",
                className="btn_menu",
                style={"display":"block"},
                disabled=False,
                n_clicks=0
            ),
            width=4
        )
    ]
)



@app.callback(
    Output("div_contents", "children"),
    Input("btn_info", "n_clicks"),
    Input("btn_single_upload", "n_clicks"),
    Input("btn_multi_upload", "n_clicks"),
    Input("btn_home", "n_clicks")
)
def update_output_div(info, single, multi, home):
    btn_clicked = ctx.triggered_id

    if btn_clicked == "btn_info":
        return html.P("hello")
    elif btn_clicked == "btn_single_upload":
        return single_upload
    elif btn_clicked == "btn_multi_upload":
        return "Multi"
    elif btn_clicked == "btn_home":
        return "homepage"
    else:
        return "homepage"