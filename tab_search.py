# tab_search.py

from dash import dcc, html

def create_square_component(text, image_source):
    return html.Div(
        children=[
            html.H4(text, style={"text-align": "center"}),
            html.Img(src=image_source, style={"max-width": "100px", "max-height": "100px", "margin": "auto"}),
        ],
        style={"padding": "10px", "text-align": "center", "width": "50%"}
    )

def goto_tab_search():  # Pass the 'app' variable as a parameter
    layout = html.Div([

        #First row
        html.Div([
            # Search component
            dcc.Input(
                id='search-input',
                type='text',
                placeholder='Enter your search query...'
            ),

            ],
            className = "row"
        ),

        #Second row
        html.Div([
            # Output
            ],
            className = "row",
            id='display-input'
        ),

        # #Third row
        # html.Div([
        #     create_square_component("Topic 1", "./assets/login_background.jpg"),
        #     create_square_component("Topic 2", "./assets/login_background.jpg"),
        # ], 
        #     className = "row",
        #     style={"display": "flex", "flex-wrap": "wrap"}
        # ),

        # #Fourth row
        # html.Div([
        #     create_square_component("Topic 3", "./assets/login_background.jpg"),
        #     create_square_component("Topic 4", "./assets/login_background.jpg"),
        # ], 
        #     className = "row",
        #     style={"display": "flex", "flex-wrap": "wrap"}
        # ),

    ])

    return layout
