import pandas as pd
from bs4 import BeautifulSoup


def save_plays_to_excel(plays_dict, excel_file):
    # Create an empty DataFrame
    df = pd.DataFrame()

    # Iterate over each play in the plays dictionary
    for title, play_data in plays_dict.items():
        # Create a DataFrame for each play_data
        play_df = pd.DataFrame(list(play_data.items()), columns=['Key', 'Value'])

        # Transpose the play_df to have keys in the first column and values in subsequent columns
        play_df_transposed = play_df.set_index('Key').transpose()

        # If the main DataFrame is empty, create columns based on play_df_transposed columns
        if df.empty:
            df = pd.DataFrame(columns=['Titulo', *play_df_transposed.columns])

        # Add a new row to the main DataFrame with the title and play data
        row_data = {'Titulo': [title], **play_df_transposed.to_dict(orient='list')}
        df = pd.concat([df, pd.DataFrame(row_data)], ignore_index=True)

    # Save the DataFrame to an Excel file
    df.to_excel(excel_file, index=False)


def get_containers_data(play_containers, excel_file_path='plays_data_2023_actuales.xlsx'):
    
    plays = dict()
    for i in range(len(play_containers)):
        play_details = play_containers[i].find('div', class_='detail')

        print(i)
        links = play_details.find_all('a')
        link = links[0]['href']
        print(link)

        images = play_containers[i].find_all('img')
        image = images[0]['src']
        print(image)

        titulo = play_details.find('span').get_text()


        info = play_details.find_all('p')
        info_text = info[-1].get_text()
        info_tolist = info_text.split('|')

        teatro = info_tolist[1]
        
        try:
            sala = info_tolist[2]
        except (IndexError):
            sala = ""


        fechas = info_tolist[0]

        ##### Store data
        play_data = dict({'Teatro': teatro, 'Sala' : sala, 'Fechas' : fechas, 'Imagen' : image, 'Link' : link})

        plays[titulo] = play_data

    print(plays)
    save_plays_to_excel(plays, excel_file_path)



def obras_change_date_format(obras):
    # Split "Fechas" column into two columns
    obras[['Fecha_inicio_raw', 'Fecha_final_raw']] = obras['Fechas'].str.split('-', expand=True)

    # Strip any leading or trailing whitespaces
    obras['Fecha_inicio_raw'] = obras['Fecha_inicio_raw'].str.strip()
    obras['Fecha_final_raw'] = obras['Fecha_final_raw'].str.strip()

    # Map Spanish month names to their corresponding numerical values
    spanish_month_names = {
        'ENE': '01', 'FEB': '02', 'MAR': '03', 'ABR': '04',
        'MAY': '05', 'JUN': '06', 'JUL': '07', 'AGO': '08',
        'SEP': '09', 'OCT': '10', 'NOV': '11', 'DIC': '12'
    }

    # Extract day, month, and year from "Fecha_inicio_raw"
    obras[['Dia_inicio', 'Mes_inicio']] = obras['Fecha_inicio_raw'].str.split(' ', expand=True)
    obras['Mes_inicio'] = obras['Mes_inicio'].map(spanish_month_names)
    obras['Fecha_inicio'] = obras['Ano_inicio'].astype(str) + '/' + obras['Mes_inicio'] + '/' + obras['Dia_inicio']

    # Extract day, month, and year from "Fecha_final_raw"
    obras[['Dia_final', 'Mes_final']] = obras['Fecha_final_raw'].str.split(' ', expand=True)
    obras['Mes_final'] = obras['Mes_final'].map(spanish_month_names)
    obras['Fecha_final'] = obras['Ano_inicio'].astype(str) + '/' + obras['Mes_final'] + '/' + obras['Dia_final']

    # Convert "Fecha_inicio" and "Fecha_final" to datetime format
    obras['Fecha_inicio'] = pd.to_datetime(obras['Fecha_inicio'])
    obras['Fecha_final'] = pd.to_datetime(obras['Fecha_final'])

    # Handle cases where the play spans across the year boundary
    obras.loc[obras['Fecha_final'] < obras['Fecha_inicio'], 'Ano_inicio'] += 1

    # Recalculate "Fecha_final" after adjusting the year
    obras['Fecha_final'] = obras['Ano_inicio'].astype(str) + '/' + obras['Mes_final'] + '/' + obras['Dia_final']

    # Convert "Fecha_final" to datetime format
    obras['Fecha_final'] = pd.to_datetime(obras['Fecha_final'])

    # Drop unnecessary columns
    obras = obras.drop(['Fechas', 'Ano_inicio', 'Fecha_inicio_raw', 'Fecha_final_raw', 'Dia_inicio', 'Mes_inicio', 'Dia_final', 'Mes_final'], axis=1)
    return obras