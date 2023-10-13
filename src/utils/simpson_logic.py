"""simpson"""
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

SEGMENTS = 200000
SEGMENTS_GRAPHS = 1000


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


def create_final_figure(sigma, mean, limit_inf, limit_sup, toggle):
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
