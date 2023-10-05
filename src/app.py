"""APP"""
import dash
from dash import dcc, html
app = dash.Dash(__name__, external_scripts=[
    'https://polyfill.io/v3/polyfill.min.js?features=es6',
    'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'
])

app.layout = html.Div(id='main',children=[
  html.Div([
    dcc.Markdown('$$Area (m^{2})$$', mathjax=True),
    dcc.Markdown('$x^{2} + 5x+ 2x_{0}$', mathjax=True),
    dcc.Markdown('$$\dfrac{4}{3}$$', mathjax=True),
    dcc.Markdown('$$\dfrac{4}{3}$$', mathjax=True),
    dcc.Markdown('$$\dbinom{n}{k}$$', mathjax=True),
    dcc.Markdown('$$\int$$', mathjax=True),
    dcc.Markdown('$$\mu$$', mathjax=True),
    dcc.Markdown('$$\pi$$', mathjax=True),
    dcc.Markdown('$$f(x)= \dfrac{1}{\sigma \sqrt{2 \pi}} e^{ \dfrac{1}{2} \dfrac{x - \mu}{\sigma}^2 }$$', mathjax=True)
  ])
])

if __name__ == '__main__':
  app.run_server(debug=True)

if __name__ == '__main__':
    app.run_server(debug=True)
