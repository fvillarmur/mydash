"""reference"""
from dash import html

layout = html.Div([
    html.P('''Bertsekas, D., & Tsitsiklis, J. N. (2008).
           Introduction to probability. Athena Scientific.'''),
    html.P('''Chapra, S. C., & Canale, R. P. (2007). Métodos numéricos para ingenieros.''')
])


def go_reference():
    """reference"""
    return layout
