"""home"""
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from dash_bootstrap_templates import ThemeSwitchAIO

SEGMENTS = 200000
SEGMENTS_GRAPHS = 1000

mean_input = dcc.Input(
    id="mean",
    type="number",
    placeholder="Media",
    debounce=True,
    value=0,
    className='form-control',
    required=True
)

sigma_input = dcc.Input(
    id="sigma",
    type="number",
    placeholder="Desviación estándar",
    debounce=True,
    value=1,
    min=.00001,
    className='form-control',
    required=True
)

limit_inf_input = dcc.Input(
    id="limit_inf",
    type="number",
    placeholder="Límite inferior",
    debounce=True,
    value=-5,
    size='10',
    className='form-control',
    required=True
)

limit_sup_input = dcc.Input(
    id="limit_sup",
    type="number",
    placeholder="Límite superior",
    debounce=True,
    value=0,
    className='form-control',
    required=True
)

row1 = html.Tr([html.Td(dcc.Markdown('$\\mu$', mathjax=True)), html.Td(mean_input),
                html.Td(dcc.Markdown('$\\sigma$', mathjax=True)), html.Td(sigma_input)])
row2 = html.Tr([html.Td("Límite inferior"), html.Td(limit_inf_input),
                html.Td("Límite superior"), html.Td(limit_sup_input)])

table_body = [html.Tbody([row1, row2])]

table = dbc.Table( table_body, bordered=True, size='sm', responsive=True)

layout = html.Div([
    table,
    html.Br(),
    html.Div([
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

    final_figure = create_final_figure(sigma, mean, limit_inf ,limit_sup, toggle)

    return [
        html.Div(dcc.Graph(id="theme-switch-graph", figure=final_figure, mathjax=True))]


def go_home():
    """home layout"""
    return layout

def create_final_figure(sigma, mean, limit_inf ,limit_sup, toggle):
    """creates final figure"""
    array_x = np.linspace(limit_inf, limit_sup, SEGMENTS)
    array_fx = function_evaluation(array_x, sigma, mean)
    result = simpson_multiple(array_fx, limit_inf, limit_sup)

    template = "cosmo" if toggle else "darkly"

    fig_function = create_fig_function(sigma, mean)
    fig_area = create_fig_area(limit_inf, limit_sup, sigma, mean)
    final_figure = go.Figure(data=fig_function.data + fig_area.data)

    final_figure.update_layout(
        template=template,
        title=f'''$$P({limit_inf} \\geq x \\leq {limit_sup}) = {result}$$''',
        xaxis_title=f'$\\sigma = {sigma}; \\mu = {mean}$',
        yaxis_title=r'$f(x) = N(\mu, \sigma^2)$')

    return final_figure


def create_fig_function(sigma, mean):
    """create figure function"""
    sigma_times = 5
    array_x_graph = np.linspace(
        mean - sigma_times*sigma, mean + sigma_times*sigma, SEGMENTS_GRAPHS)
    array_fx_graph = function_evaluation(array_x_graph, sigma, mean)
    return px.line(x=array_x_graph, y=array_fx_graph)


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
