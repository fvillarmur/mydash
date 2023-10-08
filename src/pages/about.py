"""about"""
from dash import html

layout = html.Div([
    html.H1('This is our about page'),
    html.I(className = "fa-brands fa-linkedin")
])


def go_about():
    """about"""
    return layout
