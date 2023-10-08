"""home"""
from dash import html, dcc, callback, Input, Output
import numpy as np
import plotly.express as px
from dash_bootstrap_templates import ThemeSwitchAIO

SEGMENTS = 200000

layout = html.Div([
    html.H1('This is our Home page'),
    html.Div('This is our Home page content.'),
    dcc.Input(id='limit_inf', value=0, type='number'),
    dcc.Input(id='limit_sup', value=0, type='number'),
    dcc.Input(id='mean', value=0, type='number'),
    dcc.Input(id='sigma', value=1, type='number'),
    html.Br(),
    html.Div(id='result'),
    html.Div(dcc.Graph(id="theme-switch-graph", mathjax=True), className="m-4")
])


@callback(
    Output('result', 'children'),
    Input('limit_inf', 'value'),
    Input('limit_sup', 'value'),
    Input('mean', 'value'),
    Input('sigma', 'value')
)
def simpson_gauss(limit_inf, limit_sup, mean, sigma):
    "método de simpson 1/3 para distribución gauss"
    if (not isinstance(limit_inf, (int, float, complex)) or
        not isinstance(limit_sup, (int, float, complex)) or
        not isinstance(mean, (int, float, complex)) or
        not isinstance(sigma, (int, float, complex))):
        return 0

    array_fx = function_evaluation(limit_inf, limit_sup)
    return simpson_multiple(array_fx, limit_inf, limit_sup)

# https://dash.plotly.com/advanced-callbacks


@callback(
    Output("theme-switch-graph", "figure"),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def update_graph(toggle):
    """update graph"""
    template = "cosmo" if toggle else "darkly"
    fig = px.line(x=[1, 2, 3, 4], y=[1, 4, 9, 16],
                  title=r'$\alpha_{1c} = 352 \pm 11 \text{ km s}^{-1}$',
                  template=template)
    fig.update_layout(
        xaxis_title=r'$\sqrt{(n_\text{c}(t|{T_\text{early}}))}$',
        yaxis_title=r'$d, r \text{ (solar radius)}$'
    )
    return fig


def function_evaluation(limit_inf, limit_sup):
    """function evaluation"""
    array_x = np.linspace(limit_inf, limit_sup, SEGMENTS)
    return array_x**2


def simpson_multiple(array_fx, limit_inf, limit_sup):
    """simpson method"""
    last = SEGMENTS - 1
    odds = array_fx[1:last:2]
    evens = array_fx[2:last:2]

    sum_odds = np.sum(4*odds)
    sum_evens = np.sum(2*evens)

    total_sum = array_fx[0] + sum_evens + sum_odds + array_fx[last]
    _h = (limit_sup - limit_inf)/(3*SEGMENTS)

    return _h*total_sum


def go_home():
    """home layout"""
    return layout
