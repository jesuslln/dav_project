from dash import dcc, html
import numpy as np
import plotly.graph_objects as go


def goto_tab_theatre():
    return html.Div(            
        children=[
            html.H1(  # Primera fila
                children=[
                    "Your Theatre"
                ],
                id="titulo",
                style={  # Aquí aplico todo lo que necesite de CSS
                    "text-align": "center",  # Alineo el texto al centro
                    "font-family": "Arial",  # Cambio el tipo de fuente
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
                        id="figura-1",
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
                        id="figura-2",
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
                        id="figura-3",
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
                        id="figura-4",
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

