# Importamos las librerias mínimas necesarias
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import numpy as np
import plotly.graph_objects as go


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
    dcc.Tabs(
        id='tabs',
        value='tab-home',
        children=[
            dcc.Tab(label='Home', value='tab-home'),
            dcc.Tab(label='Search', value='tab-search'),
            dcc.Tab(label='Your Theatre', value='tab-theatre'),
        ],
    ),
    html.Div(id='tabs-content')
])

# Callback to update the content based on the selected tab
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def update_tab_content(selected_tab):
    if selected_tab == 'tab-home':
        return html.Div([
            html.Div([
                html.H3(
                    'Las más Vistas',
                    id="h-masvistas",
                    style={
                        "display": "inline-block",
                        "margin-left": "50px",
                        "margin-right": "500px"
                    },
                ),
                html.H3(
                    'Las más Gustadas',
                    id="h-masgustadas",
                    style={
                        "display": "inline-block",
                        "margin-right": "50px",
                        "margin-left": "500px"
                    },
                ),
            ]
            ),
            html.Div([
                html.Ul([
                    html.Li("Item A"),
                    html.Li("Item B"),
                    html.Li("Item C"),
                ],
                    style={
                        "display": "inline-block",
                        "list-style-type": "none",  # Remove bullet points
                        "margin": 0,                 # Remove default margins
                        "padding": 0,                # Remove default padding
                        "margin-left": "50px",
                        "margin-right": "500px",
                    }
                ),
                html.Ul([
                    html.Li("Item Play 1"),
                    html.Li("Item Play 2"),
                    html.Li("Item Play 3"),
                ],
                    style={
                        "display": "inline-block",
                        "list-style-type": "none",  # Remove bullet points
                        "margin": 0,                 # Remove default margins
                        "padding": 0,                # Remove default padding
                        "margin-right": "50px",
                        "margin-left": "550px",
                    }
                ),
            ]),
             html.Div([
                html.H3(
                    'Las más Nuevas',
                    id="h-masnuevas",
                    style={
                        "display": "inline-block",
                        "margin-left": "50px",
                        "margin-right": "500px"
                    },
                ),
                html.H3(
                    'Las más Esperadas',
                    id="h-masesperadas",
                    style={
                        "display": "inline-block",
                        "margin-right": "50px",
                        "margin-left": "500px"
                    },
                ),
            ]
            ),
            html.Div([
                html.Ul([
                    html.Li("Item A"),
                    html.Li("Item B"),
                    html.Li("Item C"),
                ],
                    style={
                        "display": "inline-block",
                        "list-style-type": "none",  # Remove bullet points
                        "margin": 0,                 # Remove default margins
                        "padding": 0,                # Remove default padding
                        "margin-left": "50px",
                        "margin-right": "500px",
                    }
                ),
                html.Ul([
                    html.Li("Item Play 1"),
                    html.Li("Item Play 2"),
                    html.Li("Item Play 3"),
                ],
                    style={
                        "display": "inline-block",
                        "list-style-type": "none",  # Remove bullet points
                        "margin": 0,                 # Remove default margins
                        "padding": 0,                # Remove default padding
                        "margin-right": "50px",
                        "margin-left": "550px",
                    }
                ),
            ])
        ],
            id="div-home",
            style={
                "margin-right": "125px",
                "margin-left": "125px",
                "margin-top": "100px",
                "border-style": "groove",
            }
        )

        # return html.Div([
        #     html.H3(
        #         'Las más Vistas',
        #         id="h-masvistas",
        #         style={
        #             "display": "inline-block",
        #             "margin-left": "50px",
        #             "margin-right" : "500px"
        #         },
        #     ),
        #     html.H3(
        #         'Las más Gustadas',
        #         id="h-masgustadas",
        #         style={
        #             "display": "inline-block",
        #             "margin-right" : "50px",
        #             "margin-left": "500px"
        #         },
        #     ),
        # ],
        #     id="div-home",
        #     style={
        #         "margin-right": "125px",
        #         "margin-left": "125px",
        #         "margin-top": "100px",
        #         "border-style": "groove",
        #     }
        # )

    elif selected_tab == 'tab-search':
        return html.Div([
            html.H3('Welcome to the Search Tab'),
            # Add content specific to the Search tab here
        ])
    elif selected_tab == 'tab-theatre':
        return html.Div(            
            children=[
                html.H1(  # Primera fila
                    children=[
                        "Introducción a Dash"
                    ],
                    id="titulo",
                    style={  # Aquí aplico todo lo que necesite de CSS
                        "text-align": "center",  # Alineo el texto al centro
                        "color": "lightsteelblue",  # Cambio el color de la fuente, se puede usar codigo hexagesimal
                        "font-family": "Arial",  # Cambio el tipo de fuente
                        "backgroundColor": "darkslategray",  # Cambio el color del fondo
                        "text-decoration": "underline"  # Subrayar el texto
                    }
                ),
                html.Div(
                    children=[
                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Bar(
                                        x=["Clase 1", "Clase 2", "Clase 3"],
                                        y=[10, 6, 13],
                                        marker_color=["gold", "darkorange", "firebrick"],
                                    )
                                ],
                                layout=go.Layout(
                                    title="Primer gráfico de prueba",
                                    xaxis_title="Clases",
                                    yaxis_title="Elementos",
                                    width=600,
                                    height=600
                                )
                            ),
                            id="primera_figura",
                            style={
                                "display": "inline-block",  # Diferenciar entre block, inline-block , inline
                            }
                        ),
                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Bar(
                                        x=["Clase 1", "Clase 2", "Clase 3"],
                                        y=[10, 6, 13],
                                        marker_color=["gold", "darkorange", "firebrick"],
                                    )
                                ],
                                layout=go.Layout(
                                    title="Otro gráfico de prueba",
                                    xaxis_title="Clases",
                                    yaxis_title="Elementos",
                                    width=600,
                                    height=600
                                )
                            ),
                            id="segunda_figura",
                            style={
                                "display": "inline-block",  # Diferenciar entre block, inline-block , inline
                            }
                        ),
                    ],
                    id="tercera_fila",
                ),
                html.Div(  # Cuarta fila
                    children=[
                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Histogram(
                                        x=np.random.normal(size=1000),
                                        marker_color="steelblue",
                                        name="Histograma",
                                        histnorm="probability"
                                    ),
                                ],
                                layout=go.Layout(
                                    title="Histograma de valores",
                                    xaxis_title="Valores de una normal de media 0 y std 1",
                                    width=600,
                                    height=600,
                                    bargap=0.1
                                )
                            ),
                            id="tercera_figura",
                            style={
                                "display": "inline-block",
                            }
                        ),

                        dcc.Graph(
                            figure=go.Figure(
                                data=[
                                    go.Histogram(
                                        x=np.random.gamma(shape=1 / 2, scale=1 / 2, size=1000),
                                        marker_color="indigo",
                                        name="Histograma",
                                        histnorm="probability"
                                    ),
                                ],
                                layout=go.Layout(
                                    title="Histograma de valores",
                                    xaxis_title="Valores de una gamma",
                                    width=600,
                                    height=600,
                                    bargap=0.1
                                )
                            ),
                            id="cuarta_figura",
                            style={
                                "display": "inline-block"
                            }
                        ),
                    ],
                    id="cuarta_fila",
                ),
                html.Div(  # Quinta Fila - Contacto
                    children=[
                        html.H2(
                            children=["Contactanos en este correo para saber más:"],
                            id="titulo_contacto",
                            style={
                                'text-align': 'center',  # Center-align the text
                                'margin': '20px',  # Add some margin for spacing
                                'font-family': 'Arial, sans-serif',  # Choose a clean sans-serif font
                                'color': '#333',  # Set text color to a dark shade
                                'background-color': '#f8f8f8',  # Set a light background color
                                'padding': '15px',  # Add padding for better readability
                                'border-radius': '10px',  # Round the corners of the container
                                'box-shadow': '0 0 10px rgba(0, 0, 0, 0.1)'  # Add a subtle box shadow
                            }
                        ),
                    ],
                    id="quinta_fila"
                ),
                html.Div(  # Sexta fila - Correo
                    children=[
                        html.P(
                            children=["contacto.mipaginadash@gmail.com"],
                            id="correo_contacto",
                            style={
                                'text-align': 'center',  # Center-align the text
                                'margin': '20px',  # Add some margin for spacing
                                'font-family': 'Arial, sans-serif',  # Choose a clean sans-serif font
                                'color': '#333',  # Set text color to a dark shade
                                'background-color': '#f8f8f8',  # Set a light background color
                                'padding': '15px',  # Add padding for better readability
                                'border-radius': '10px',  # Round the corners of the container
                                'box-shadow': '0 0 10px rgba(0, 0, 0, 0.1)'  # Add a subtle box shadow
                            }
                        )
                    ],
                    id="sexta_fila"
                )

            ],
            id="primera_fila",
            style={
                "margin-right": "125px",
                "margin-left": "125px",
                "margin-top": "100px",
                "border-style": "groove",
            }
        )

    else:
        return html.Div([
            html.H3('Invalid tab selected')
        ])

if __name__ == '__main__':
    app.run_server(debug=True)
