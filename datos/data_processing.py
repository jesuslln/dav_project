import os
import sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)


import pandas as pd
import numpy as np
from utils.utils import obras_change_date_format


# Read data
obras = pd.read_excel("./datos/obras/plays_data.xlsx")
data_user1 = pd.read_excel("./datos/fake_users/user1_obras.xlsx")
amigos_user1 = pd.read_excel("./datos/fake_users/user1_amigos.xlsx")
data_user2 = pd.read_excel("./datos/fake_users/user2_obras.xlsx")

print("Data reading completed")


## Cleaning obras dataset
columns_to_clean = ['Titulo', 'Teatro', 'Sala', 'Fechas']
obras[columns_to_clean] = obras[columns_to_clean].replace('\n', '', regex=True)

obras = obras_change_date_format(obras)

obras['Duracion'] = (obras['Fecha_final'] - obras['Fecha_inicio']).dt.days
obras['Titulo'] = obras['Titulo'].str.strip()
obras["Teatro"] = obras["Teatro"].str.strip()
obras["Sala"] = obras["Sala"].str.strip()
obras['Sala'] = obras['Sala'].fillna('Sala Grande')

print("Cleaning obras dataset completed")


## Cleaning users data
data_user1['Titulo'] = data_user1['Titulo'].replace('\n', '', regex=True).str.strip()
data_user2['Titulo'] = data_user2['Titulo'].replace('\n', '', regex=True).str.strip()


def get_obras():
    return obras

def get_data_user1():
    return data_user1

def get_data_user2():
    return data_user2