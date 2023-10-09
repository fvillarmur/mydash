"""home"""
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from dash_bootstrap_templates import ThemeSwitchAIO
from dash_daq import NumericInput as daqNumericInput

SEGMENTS = 200000
daqNumericInput: callable

mean_input = daqNumericInput(
                id='mean',
                min=-1000000,
                max=1000000,
                value=10,
                size=100
            )

sigma_input = daqNumericInput(
                id='sigma',
                min=1,
                max=1000000,
                value=1,
                size=100
            )

limit_inf_input = daqNumericInput(
                id='limit_inf',
                min=-1000000,
                max=1000000,
                value=2,
                size=100
            )

limit_sup_input = daqNumericInput(
                id='limit_sup',
                min=-1000000,
                max=1000000,
                value=4,
                size=100
            )

form = dbc.Form([
    dbc.Row(
        [
            dbc.Label(dcc.Markdown('$\\mu$',mathjax=True), width="auto"),
            dbc.Col(mean_input),
            dbc.Label(dcc.Markdown('$\\sigma$',mathjax=True), width="auto"),
            dbc.Col(sigma_input)
        ],
    ),
    dbc.Row(
        [
            dbc.Col(limit_inf_input),
            dbc.Col(dbc.Label(dcc.Markdown('$\\geq x \\leq$',mathjax=True), width="auto")),
            dbc.Col(limit_sup_input)
        ]
    ),
   ]
)

layout = html.Div([
    form,
    html.Br(),
    html.Div([
        html.Div('0'),
        html.Div(dcc.Graph(id="theme-switch-graph", mathjax=True))
    ], id='result'),
])

@callback(
    Output('result', 'children'),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
    Input('limit_inf', 'value'),
    Input('limit_sup', 'value'),
    Input('mean', 'value'),
    Input('sigma', 'value')
)
def update_graph(toggle, limit_inf, limit_sup, mean, sigma):
    """update graph"""
    if (not isinstance(limit_inf, (int, float, complex)) or
        not isinstance(limit_sup, (int, float, complex)) or
        not isinstance(mean, (int, float, complex)) or
        not isinstance(sigma, (int, float, complex))):
        return 0

    array_x = np.linspace(limit_inf, limit_sup, SEGMENTS)
    array_fx = function_evaluation(array_x, sigma, mean)
    result = simpson_multiple(array_fx, limit_inf, limit_sup)

    segments_graphs = 1000
    array_x_graph = np.linspace(limit_inf - 2*limit_inf, limit_sup + 2*limit_sup, segments_graphs)
    array_fx_graph = function_evaluation(array_x_graph, sigma, mean)

    array_x_area_graph = np.linspace(limit_inf, limit_sup, segments_graphs)
    array_fx_area_graph = function_evaluation(array_x_area_graph, sigma, mean)

    template = "cosmo" if toggle else "darkly"
    fig_function = px.line(x=array_x_graph, y=array_fx_graph,
                  title=r'$\alpha_{1c} = 352 \pm 11 \text{ km s}^{-1}$')

    fig_area = px.area(x = array_x_area_graph, y = array_fx_area_graph)

    final_figure = go.Figure(data= fig_function.data + fig_area.data)

    final_figure.update_layout(template = template,
        xaxis_title=r'$\sqrt{(n_\text{c}(t|{T_\text{early}}))}$',
        yaxis_title=r'$d, r \text{ (solar radius)}$')

    return [
        html.Div(f'''{result}'''),
        html.Div(dcc.Graph(id="theme-switch-graph", figure=final_figure, mathjax=True))]

def function_evaluation(array_x, sigma, mean):
    """function evaluation"""
    fx = (1/(sigma * (2*np.pi)**.5))*np.exp(-.5*( ((array_x - mean) / sigma )**2 ) )
    return fx


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
