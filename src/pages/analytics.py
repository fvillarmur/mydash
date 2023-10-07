"""home"""
from dash import html, dcc, callback, Input, Output

def go_analytics():
    """go analytics"""
    return layout

layout = html.Div([
    html.H1('This is our Analytics page'),
    html.Div([
        "Select a city: ",
        dcc.RadioItems(
            options=['New York City', 'Montreal', 'San Francisco'],
            value='Montreal',
            id='analytics-input'
        )
    ]),
    html.Br(),
    html.Div(id='analytics-output'),
])

@callback(
    Output('analytics-output', 'children'),
    Input('analytics-input', 'value')
)
def update_city_selected(input_value):
    """update city"""
    return f'You selected: {input_value}'
