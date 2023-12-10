from dash import dcc, html


def create_square_component(text, image_source):
    return html.Div(
        children=[
            html.H4(text, style={"text-align": "center"}),
            html.Img(src=image_source, style={"max-width": "100px", "max-height": "100px", "margin": "auto"}),
        ],
        style={ "padding": "10px", "text-align": "center", "width": "50%"}
    )

def goto_tab_search():
    return html.Div([            
                # Search component
                dcc.Input(
                    id='search-input',
                    type='text',
                    placeholder='Enter your search query...'
                ),

                html.Div(id='search-results-container', style={"height": "500px"}),
                # Square-shaped components in two rows and two columns
                html.Div([
                    create_square_component("Topic 1", "./assets/login_background.jpg"),
                    create_square_component("Topic 2", "./assets/login_background.jpg"),
                ], style={"display": "flex", "flex-wrap": "wrap"}),

                # Second row of square-shaped components
                html.Div([
                    create_square_component("Topic 3", "./assets/login_background.jpg"),
                    create_square_component("Topic 4", "./assets/login_background.jpg"),
                ], style={"display": "flex", "flex-wrap": "wrap"}),

            ])