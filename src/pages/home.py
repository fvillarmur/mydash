"""home"""
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from dash_bootstrap_templates import ThemeSwitchAIO
from dash_daq import NumericInput as daqNumericInput

SEGMENTS = 200000
SEGMENTS_GRAPHS = 1000
daqNumericInput: callable

mean_input = daqNumericInput(
    id='mean',
    value=0,
    min=-1000000,
    max=1000000,
    size=100,
    persistence_type=True
)

sigma_input = daqNumericInput(
    id='sigma',
    value=1,
    min=1,
    max=1000000,
    size=100
)

limit_inf_input = daqNumericInput(
    id='limit_inf',
    value=-4,
    min=-1000000,
    max=1000000,
    size=100
)

limit_sup_input = daqNumericInput(
    id='limit_sup',
    value=0,
    min=-1000000,
    max=1000000,
    size=100
)

form = dbc.Form([
    dbc.Row(
        [
            dbc.Label(dcc.Markdown('$\\mu$', mathjax=True), width="auto"),
            dbc.Col(mean_input),
            dbc.Label(dcc.Markdown('$\\sigma$', mathjax=True), width="auto"),
            dbc.Col(sigma_input)
        ],
    ),
    dbc.Row(
        [
            dbc.Col(limit_inf_input),
            dbc.Col(dbc.Label(dcc.Markdown(
                '$\\geq x \\leq$', mathjax=True), width="auto")),
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
        return html.Div('Solo se aceptan números en las entradas.')

    if limit_inf >= limit_sup:
        return html.Div('Límite superior tiene que ser mayor que el inferior.')

    array_x = np.linspace(limit_inf, limit_sup, SEGMENTS)
    array_fx = function_evaluation(array_x, sigma, mean)
    result = simpson_multiple(array_fx, limit_inf, limit_sup)

    template = "cosmo" if toggle else "darkly"

    fig_function = create_fig_function(sigma, mean)
    fig_area = create_fig_area(limit_inf, limit_sup, sigma, mean)
    final_figure = go.Figure(data=fig_function.data + fig_area.data)

    final_figure.update_layout(template=template,
                               xaxis_title=r'$\sqrt{(n_\text{c}(t|{T_\text{early}}))}$',
                               yaxis_title=r'$d, r \text{ (solar radius)}$')

    return [
        html.Div(f'''{result}'''),
        html.Div(dcc.Graph(id="theme-switch-graph", figure=final_figure, mathjax=True))]


def create_fig_function(sigma, mean):
    """create figure function"""
    sigma_times = 5
    array_x_graph = np.linspace(
        mean - sigma_times*sigma, mean + sigma_times*sigma, SEGMENTS_GRAPHS)
    array_fx_graph = function_evaluation(array_x_graph, sigma, mean)
    return px.line(x=array_x_graph, y=array_fx_graph,
                   title=r'$\alpha_{1c} = 352 \pm 11 \text{ km s}^{-1}$')


def create_fig_area(limit_inf, limit_sup, sigma, mean):
    """create figure area"""
    array_x_area_graph = np.linspace(limit_inf, limit_sup, SEGMENTS_GRAPHS)
    array_fx_area_graph = function_evaluation(array_x_area_graph, sigma, mean)
    return px.area(x=array_x_area_graph, y=array_fx_area_graph)


def function_evaluation(array_x, sigma, mean):
    """function evaluation"""
    fx = (1/(sigma * (2*np.pi)**.5)) * \
        np.exp(-.5*(((array_x - mean) / sigma)**2))
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
