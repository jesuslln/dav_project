from dash import dcc, html
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from datos.data_processing import get_data_user1, get_data_user2, get_obras


data_user1 = get_data_user1()
data_user2 = get_data_user2()
obras = get_obras()

data_user1['user'] = 'Tu'
data_user2['user'] = 'Marta'
data_users = pd.concat([data_user1, data_user2], ignore_index = True)

data_user1 = data_user1.merge(obras[['Titulo', 'Teatro']], on='Titulo', how='inner')


data_users_byYear = data_users.copy()
data_users_byYear['Fecha_Sesion'] = data_users_byYear['Fecha_Sesion'].dt.year
data_users_byYear = pd.DataFrame(data_users_byYear.groupby(['Fecha_Sesion', 'user']).size().reset_index(name='Count'))
data_users_byYear['Fecha_Sesion'] = data_users_byYear['Fecha_Sesion'].astype(str)


data_user1_byTheatre = data_user1.copy()
data_user1_byTheatre['Fecha_Sesion'] = data_user1_byTheatre['Fecha_Sesion'].dt.year.astype(str)
data_user1_byTheatre = pd.DataFrame(data_user1_byTheatre.groupby(['Fecha_Sesion', 'Teatro']).size().reset_index(name='Count'))

fig_1 = px.line(data_users_byYear, x='Fecha_Sesion', y='Count', color='user', markers=True)

fig_1.update_layout(title = "Compara obras con tu amigo",
                  xaxis_title = "Años", yaxis_title = "Número de Obras Vistas",
                  barmode='stack')



colors = {
    "Teatro Valle-Inclán": "lightblue",
    "Teatro María Guerrero": "mediumseagreen",
    'Titerescena': "red",
}

fig_2 = go.Figure()

for key in colors.keys():
    aux = data_user1_byTheatre[data_user1_byTheatre["Teatro"] == key]
    fig_2.add_trace(
        go.Bar(
            x = aux['Fecha_Sesion'],
            y = aux["Count"],
            name = key,
            marker_color = colors[key],
            width= np.repeat(0.65,len(data_user1_byTheatre))
        )
    )
fig_2.update_layout(title = "Obras que has visto cada año y en cada Teatro",
                  xaxis_title = "Años", yaxis_title = "Obras Vistas",
                  barmode='stack')



def goto_tab_theatre():
    return html.Div(
    children=[
        # First Row
        html.Div(
            children=[
                html.H1("Vive tu Teatro", id="titulo-teatro", className="text-center"),
            ],
            className="row mb-4",
        ),

        # Second Row
        html.Div(
            children=[
                # First Column
                html.Div(
                    children=[
                        dcc.Graph(
                            figure=fig_1,
                            id="figura-1"
                        ),
                    ],
                    className="col-md-5 mb-2",
                ),

                # Add space between graphs
                html.Div(className="col-md-2"),


                # Second Column
                html.Div(
                    children=[
                        dcc.Graph(
                            figure= fig_2,
                            id="figura-2"
                        ),
                    ],
                    className="col-md-5 mb-2",
                ),
            ],
            className="row",
        ),
    ],
    id="primera_fila",
    className="container",
)


