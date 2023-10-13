"""home"""
from dash import html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO

from utils.simpson_logic import create_final_figure


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

table = dbc.Table(table_body, bordered=True, size='sm', responsive=True)

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

    final_figure = create_final_figure(
        sigma, mean, limit_inf, limit_sup, toggle)

    return [
        html.Div(dcc.Graph(id="theme-switch-graph", figure=final_figure, mathjax=True))]


def go_home():
    """home layout"""
    return layout
