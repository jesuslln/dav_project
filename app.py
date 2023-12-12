# Importamos las librerias mínimas necesarias
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) 


import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

from tab_search import goto_tab_search
from tab_theatre import goto_tab_theatre
from tab_cdn import goto_tab_cdn

from datos.data_processing import get_obras

obras = get_obras()

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

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)
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

    # Define callback to update H3 component based on user input
@app.callback(
    Output('display-input', 'children'),
    [Input('search-input', 'value')]
)


def update_filtered_result(input_value):
    if not input_value:
        return html.H3('Busca tus obras favoritas')  # Return an empty string if there's no input

    # Filter the dataset based on the user input
    filtered_obras = obras[obras['Titulo'].str.contains(input_value, case=False)]

    # Check the length of the filtered obras
    num_results = len(filtered_obras)

    if num_results > 0:
        # Initialize a list to store square components
        square_components = []

        # Determine the number of rows and columns based on the number of results
        num_rows = (num_results + 2) // 3  # Ceiling division to handle odd numbers
        num_cols = 3

        # Iterate over the results to create square components
        for i in range(num_results):
            result_titulo = filtered_obras.iloc[i]['Titulo']
            result_imagen = filtered_obras.iloc[i]['Imagen']

            # Create the square component
            square_component = html.Div(
                children=[
                    html.H4(result_titulo),
                    html.Img(src=result_imagen, style={"max-width": "100px", "max-height": "100px", "margin": "auto"}),
                ],
                className=f"col-{12 // num_cols}",
                style={"padding": "10px", "text-align": "center"},
            )

            # Append the square component to the list
            square_components.append(square_component)

        # Create rows with columns for square components
        rows = [
            html.Div(square_components[i:i + num_cols], className="row")
            for i in range(0, len(square_components), num_cols)
        ]

        # Return the assembled layout
        return rows

    else:
        return html.H3('No results')


if __name__ == '__main__':
    app.run_server(debug=True)
