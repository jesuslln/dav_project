from dash import dcc, html
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

from datos.data_processing import get_obras


obras = get_obras()

obras_byTheatre = obras["Teatro"].value_counts()


obras_year = obras.copy()
obras_year["Fecha_inicio"] = obras_year["Fecha_inicio"].dt.year
obras_byYear_Teatro = pd.DataFrame(obras_year.groupby("Fecha_inicio")["Teatro"].value_counts()).rename(columns = {"Teatro": "count"}).reset_index()

obras_Teatro_bySala = pd.DataFrame(obras.groupby("Teatro")["Sala"].value_counts()).rename(columns = {"Sala": "count"}).reset_index()


teatro_suffix_mapping = {
    'Teatro María Guerrero': 'MG',
    'Teatro Valle-Inclán': 'VI',
    # Add more mappings as needed
}

# Update Sala names based on Teatro
obras_Teatro_bySala['Sala'] = obras_Teatro_bySala.apply(
    lambda row: f"{row['Sala']} {teatro_suffix_mapping.get(row['Teatro'], '')}",
    axis=1
)



obras_treemap = pd.DataFrame(obras.groupby('Titulo')['entradas_vendidas'].sum()).sort_values(by='entradas_vendidas', ascending=False)
obras_treemap = obras_treemap.merge(obras[['Titulo', 'Teatro']], on='Titulo', how='inner')

obras_treemap['Titulo_truncated'] = obras_treemap['Titulo'].apply(lambda x: x[:10] + '...' if len(x) > 10 else x)
total_sum_by_group = obras_treemap.groupby(['Teatro', 'Titulo_truncated'])['entradas_vendidas'].sum().reset_index()
total_sum_by_teatro = obras_treemap.groupby('Teatro')['entradas_vendidas'].sum().reset_index()

obras_treemap = pd.merge(obras_treemap, total_sum_by_group, on=['Teatro', 'Titulo_truncated'], how='left', suffixes=('', '_total_sum_group'))
obras_treemap = pd.merge(obras_treemap, total_sum_by_teatro, on='Teatro', how='left', suffixes=('', '_total_sum_teatro'))



## Figura 1
colors = {
    "Teatro Valle-Inclán": "lightblue",
    "Teatro María Guerrero": "mediumseagreen",
    'Titerescena': "red",
}

fig_1 = go.Figure()

for key in colors.keys():
    aux = obras_byYear_Teatro[obras_byYear_Teatro["Teatro"] == key]
    fig_1.add_trace(
        go.Bar(
            x = ["2021", "2022", "2023", "2024"],
            y = aux["count"],
            name = key,
            marker_color = colors[key],
            width= np.repeat(0.65,len(obras_byYear_Teatro))
        )
    )

fig_1.update_layout(title = "Número de obras en cada teatro por año",
                  xaxis_title = "Años", yaxis_title = "Obras Representadas",
                  barmode='stack')


### Figura 2

fig_2 =go.Figure(go.Sunburst(
    labels = list(obras["Teatro"].unique()) + list(obras_Teatro_bySala["Sala"]),
    parents = ["", "" , ""] + list(obras_Teatro_bySala["Teatro"]),
    values = list(obras_byTheatre) + list(obras_Teatro_bySala["count"]),
))
fig_2.update_layout(title = "Obras por Teatro y por Sala",
                    margin = dict(t=40, l=0, r=0, b=0),
                    showlegend = True
                    )



#### Figura 3 

fig_3 = px.treemap(obras_treemap, path=['Teatro', 'Titulo_truncated'], values='entradas_vendidas',
                 color='entradas_vendidas',
                 color_continuous_scale='RdBu',
                 color_continuous_midpoint=np.average(obras['entradas_vendidas'], weights=obras['entradas_vendidas']),
                 custom_data=['Titulo', 'entradas_vendidas_total_sum_group', 'entradas_vendidas_total_sum_teatro']  # Specify the column for custom data

                )

total_sum = obras_treemap['entradas_vendidas'].sum()

fig_3.update_traces(texttemplate='%{label}<br>%{value}', textposition='middle center',
                  textfont=dict(size=[36]), 
                  hovertemplate='%{customdata[0]}<br>Total: %{customdata[1]}<br>Total Sum (Teatro): %{customdata[2]}'
                 )

fig_3.update_layout(title = "Entradas vendidas por Teatro y Obra",
                    margin = dict(t=50, l=25, r=25, b=25))


### Modelo Random Forest Regreso - Importancia de las Variables
data = obras[['Teatro', 'Sala', 'Fecha_inicio', 'Duracion']].copy()
data['Ano'] = data['Fecha_inicio'].dt.year
data['Mes'] = data['Fecha_inicio'].dt.month
data.drop(columns=['Fecha_inicio'], inplace=True)

data_encoded = pd.get_dummies(data, columns=['Teatro', 'Sala', 'Ano', 'Mes'])
data_encoded['Duracion'] = data['Duracion']

# Dividir train-test
X = data_encoded.copy()
y = obras['entradas_vendidas'].copy()
X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size = 0.3, random_state = 123)

rf = RandomForestRegressor()
rf.fit(X_train, y_train)

predictions = rf.predict(X_test)
predictions_train = rf.predict(X_train)
feature_importances = rf.feature_importances_
feature_names = data_encoded.columns

sorted_indices = feature_importances.argsort()
sorted_feature_importances = feature_importances[sorted_indices]
sorted_feature_names = [feature_names[i] for i in sorted_indices]

# Creating a horizontal bar plot using Plotly
fig_model = go.Figure()

fig_model.add_trace(go.Bar(
    y=sorted_feature_names,
    x=sorted_feature_importances,
    orientation='h',
    marker=dict(color='skyblue'),  # You can customize the color as needed
))

fig_model.update_layout(
    title='Importancia de las Variables',
    xaxis_title='Importancia',
    yaxis_title='Variables',
    height=400,
    width=800,
)


#### simple model
X = obras[['Duracion']].copy()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

# Create and train the RandomForestRegressor
rf = RandomForestRegressor()
rf.fit(X_train, y_train)




def goto_tab_cdn():
    return html.Div(
    children=[
        # First Row
        html.Div(
            children=[
                html.H1("Las Obras del Centro Dramático Nacional", id="titulo-teatro", className="text-center"),
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
                            figure= fig_1,
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

        # Third Row
        html.Div(
            children=[
                # First Column
                html.Div(
                    children=[
                        dcc.Graph(
                            figure= fig_3,
                            id="figura-3",
                        ),
                    ],
                    className="col-md-12 mb-4",
                ),

            ],
            className="row",
        ),



        # Fourth row
                html.Div(
                    children=[
                    # First Column
                    html.Div(
                        children=[

                            html.Div(
                                children=[
                                    html.H1("Predición de las entradas vendidas", id="titulo-modelo"),
                                ],
                                className="row mb-4",
                            ),

                            html.P(
                                """
                                   Con este modelo analizamos cuales son las variables del dataset que más influyen en el 
                                   número de entradas vendidas. Como vemos en el gráfico de la derecha, el número de días 
                                   que está la obra en cartelera es la variable que más influye en el cálculo. El resto de 
                                   variables no son especialmente significativas. Habría que recoger más datos para encontrar 
                                   posibles correlaciones. Pero con este estudio, podemos ver que la fecha y los teatros no
                                   tienen una gran influencia en el número de entradas vendidas.
                                   """, id="p-modelo"),

                        ],
                        className="col-md-5 mb-2",
                    ),

                # Add space between graphs
                html.Div(className="col-md-2"),


                # Second Column
                html.Div(
                    children=[
                        dcc.Graph(
                            figure= fig_model,
                            id="figura-modelo"
                        ),
                    ],
                    className="col-md-5 mb-2",
                ),
            ],
            className="row",
        ),

        # Fith row
        html.Div(
            children=[
                # First Column
                html.Div(
                    children=[
                        html.H2(
                            children=["Contactanos en este correo para saber más sobre tus datos:"],
                            id="titulo_contacto",
                        ),
                    ],
                    className="col-md-6 mb-4",
                ),

                # Second Column
                html.Div(
                    children=[
                        html.P(
                            children=["contacto.mipaginadash@gmail.com"],
                            id="correo_contacto",
                        ),
                    ],
                    className="col-md-6 mb-4",
                ),
            ],
            className="row",
        ),
    ],
    id="primera_fila",
    className="container",
)


