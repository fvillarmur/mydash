"""APP"""
import os
import dash
from dash import dcc, html
from flask import send_from_directory

app = dash.Dash(__name__, external_scripts=[
    'https://polyfill.io/v3/polyfill.min.js?features=es6',
    'https://cdn.jsdelivr.net/npm/mathjax@3.0.1/es5/tex-mml-chtml.js'
    ],
    external_stylesheets=[
    '/assets/bootstrap.min.css'
    ],
    use_pages=True)

app.layout = html.Div([
    html.H1('Multi-page app with Dash Pages'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    html.Button('button', className='btn btn-success'),
    dash.page_container
])

@app.server.route('/assets/<path:path>')
def static_file(path):
    """serve static"""
    static_folder = os.path.join(os.getcwd(), 'assets')
    return send_from_directory(static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
