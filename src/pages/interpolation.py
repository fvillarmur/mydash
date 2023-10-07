"""interpolation"""
from dash import html, dcc

layout = html.Div(children=[
    html.Div([
        dcc.Markdown('$$Area (m^{2})$$', mathjax=True),
        dcc.Markdown('$x^{2} + 5x+ 2x_{0}$', mathjax=True),
        dcc.Markdown('$$\dfrac{4}{3}$$', mathjax=True),
        dcc.Markdown('$$\dfrac{4}{3}$$', mathjax=True),
        dcc.Markdown('$$\dbinom{n}{k}$$', mathjax=True),
        dcc.Markdown('$$\int$$', mathjax=True),
        dcc.Markdown('$$\mu$$', mathjax=True),
        dcc.Markdown('$$\pi$$', mathjax=True),
        dcc.Markdown(
            '$$f(x)= \dfrac{1}{\sigma \sqrt{2 \pi}} e^{ \dfrac{1}{2} \dfrac{x - \mu}{\sigma}^2 }$$',
            mathjax=True)
    ])
])

def go_interpolation():
    """interpolation"""
    return layout
