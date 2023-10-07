"""home"""
from dash import html

layout = html.Div([
    html.H1('This is our Home page'),
    html.Div('This is our Home page content.'),
])

def go_home():
    """home layout"""
    return layout
