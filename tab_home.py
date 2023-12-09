from dash import dcc, html



def goto_tab_home():
    return html.Div([
            html.Div([
                html.H3(
                    'Las más Vistas',
                    id="h-masvistas",
                    style={
                        "display": "inline-block",
                        "margin-left": "50px",
                        "margin-right": "500px",
                        "margin-top": "50px",
                    },
                ),
                html.H3(
                    'Las más Gustadas',
                    id="h-masgustadas",
                    style={
                        "display": "inline-block",
                        "margin-right": "50px",
                        "margin-left": "500px",
                        "margin-top": "50px",
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

            html.Div(id='search-results-container', style={"height": "250px"}),

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
                        "margin-top": "25px",
                        "margin-bottom": "50px",
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
                        "margin-top": "25px",
                        "margin-bottom": "50px",
                    }
                ),
            ])
        ],
            id="div-home",
        )