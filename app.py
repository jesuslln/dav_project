# Importamos las librerias mínimas necesarias
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 


import dash
from dash import dcc, html
from dash.dependencies import Input, Output

from tab_search import goto_tab_search
from tab_theatre import goto_tab_theatre
from tab_cdn import goto_tab_cdn


# External CSS stylesheets
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    },
    '/assets/styles.css'  # Link to the external CSS file
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.Nav(
        children=[
            dcc.Tabs(
                id='tabs',
                value='tab-theatre',
                children=[
                    dcc.Tab(label='Your Theatre', value='tab-theatre'),
                    dcc.Tab(label='Search', value='tab-search'),
                    dcc.Tab(label='CDN Info', value='tab-cdn', id="tab-cdn"),
                ],
            ),
        ],
        id='navbar',
        className='navbar navbar-expand-lg navbar-light bg-light',
    ),
    html.Div(id='tabs-content', className='container'),
])


# Callback to update the content based on the selected tab
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def update_tab_content(selected_tab):
    if selected_tab == 'tab-cdn':
        return goto_tab_cdn()

    elif selected_tab == 'tab-search':
        return goto_tab_search()
       
    elif selected_tab == 'tab-theatre':
        return goto_tab_theatre()
    else:
        return html.Div([
            html.H3('Invalid tab selected')
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
