"""APP"""
import os
import dash
from flask import send_from_directory
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from navbar import get_navbar
from pages.analytics import go_analytics
from pages.home import go_home
from pages.interpolation import go_interpolation

app = dash.Dash(__name__, external_scripts=[
    'https://polyfill.io/v3/polyfill.min.js?features=es6',
    'https://cdn.jsdelivr.net/npm/mathjax@3.0.1/es5/tex-mml-chtml.js'
],
    external_stylesheets=[
    dbc.themes.COSMO,
    dbc.icons.FONT_AWESOME
],
    suppress_callback_exceptions=True)

content = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.Div(id="page-content")
                        ]
                    ),
                    className="col-md-8",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mt-3 card shadow-lg p-3 mb-5 bg-body rounded"
)

app.layout = dbc.Container(
    [dcc.Location(id="url"), get_navbar(), content])

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    """render page content"""
    if pathname == "/":
        return go_home()

    if pathname == "/analytics":
        return go_analytics()

    if pathname == "/interpolation":
        return go_interpolation()
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

@app.server.route('/assets/<path:path>')
def static_file(path):
    """serve static"""
    static_folder = os.path.join(os.getcwd(), 'assets')
    return send_from_directory(static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
