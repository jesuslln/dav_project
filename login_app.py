# Importamos las librerias mínimas necesarias
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

# External CSS stylesheets
external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


app.layout = html.Div([
    # Left side containing input fields and buttons
    html.Div([
        html.H1("Login"),
        html.Div([
            html.Label("Username or Email"),
            dcc.Input(type="text", id="username-input", placeholder="Enter your username or email"),
        ], className="input-container"),
        html.Div([
            html.Label("Password"),
            dcc.Input(type="password", id="password-input", placeholder="Enter your password"),
        ], className="input-container"),
        html.Button("Sign in", id="signin-button", n_clicks=0, className="signin-button"),
        html.Div("Or sign in with", className="or-text"),
    ], className="login-container"),

    # Right side containing an image
    html.Div([
        html.Img(src="./assets/login_background.jpg", alt="Your Image", className="login-image"),
    ], className="image-container"),

    # Hidden div to store the current page
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

def display_page(pathname, username, password):
    if pathname == '/home':
        return html.Div([
            html.H1(f"Welcome, {username} to the Home Page!"),
            html.P(f"You have successfully signed in with password: {password}")
        ])
    else:
        return html.Div()

# Callback to update the URL when the "Sign in" button is clicked
@app.callback(Output('url', 'pathname'),
              [Input('signin-button', 'n_clicks')],
              [State('username-input', 'value'),
               State('password-input', 'value')])
def update_url(n_clicks, username, password):
    if n_clicks > 0:
        return '/home'
    else:
        return '/'


if __name__ == '__main__':
    app.run_server(debug=True)

