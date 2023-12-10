from dash import dcc, html



def goto_tab_home():
    return html.Div([
            # First Row
            html.Div([
                html.Div([
                    html.H3('Title 1'),
                ], className='col-md-6 text-center'),  # Adjust column width as needed

                html.Div([
                    html.H3('Title 2'),
                ], className='col-md-6 text-center'),  # Adjust column width as needed
            ], className='row'),

            # html.Div([
            #     html.Ul([
            #         html.Li("Item A"),
            #         html.Li("Item B"),
            #         html.Li("Item C"),
            #     ],
            #         className = "home-list-left"
            #     ),
            #     html.Ul([
            #         html.Li("Item Play 1"),
            #         html.Li("Item Play 2"),
            #         html.Li("Item Play 3"),
            #     ],
            #         className = "home-list-right"
            #     ),
            # ],
            #     className= "row"
            # ),

            # html.Div(id='search-results-container', style={"height": "250px"}),

            #  html.Div([
            #     html.H3(
            #         'Las más Nuevas',
            #         id="h-masnuevas",
            #         className = "heading-right"
            #     ),
            #     html.H3(
            #         'Las más Esperadas',
            #         id="h-masesperadas",
            #         className = "heading-left"
            #     ),
            # ],
            #     className= "row"
            # ),
            # html.Div([
            #     html.Ul([
            #         html.Li("Item A"),
            #         html.Li("Item B"),
            #         html.Li("Item C"),
            #     ],
            #         className = "home-list-right"
            #     ),
            #     html.Ul([
            #         html.Li("Item Play 1"),
            #         html.Li("Item Play 2"),
            #         html.Li("Item Play 3"),
            #     ],
            #         className = "home-list-left"
            #     ),
            # ],
            #     className= "row"
            # )
        ],
            id="div-home",
            className= "container"
        )