from dash import html, Input, Output, ctx
import dash_bootstrap_components as dbc
from create_app import app
from index import home
from information import information
from upload_single import single_upload
from upload_multi import multi_upload



menu_row = dbc.Row(
    className="g-0",
    justify="evenly",
    children = [
        dbc.Col(
            html.Button(
                "Info",
                id="btn_info",
                className="btn_menu",
                style={"borderRadius": "10px 0px 0px 0px"}
            ),
            width=4
        ),
        dbc.Col(
            html.Button(
                "Single Upload",
                id="btn_single_upload",
                className="btn_menu"
            ),
            width=4
        ),
        dbc.Col(
            html.Button(
                "Multi Upload",
                id="btn_multi_upload",
                className="btn_menu",
                style={"borderRadius": "0px 10px 0px 0px"}
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
def update_output_div(info, single, multi, home_btn):
    btn_clicked = ctx.triggered_id

    if btn_clicked == "btn_info":
        return information
    elif btn_clicked == "btn_single_upload":
        return single_upload
    elif btn_clicked == "btn_multi_upload":
        return multi_upload
    elif btn_clicked == "btn_home":
        return home
    return home