import os
import sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)


from bs4 import BeautifulSoup
from utils.utils import get_containers_data



# Read the content back from the files
with open('output_2023.txt', 'r', encoding='utf-8') as file:
    saved_content_2023 = file.read()

# Read the content back from the files
with open('output_2022.txt', 'r', encoding='utf-8') as file:
    saved_content_2022 = file.read()

# Read the content back from the files
with open('output_2021.txt', 'r', encoding='utf-8') as file:
    saved_content_2021 = file.read()


# Create a new BeautifulSoup object from the saved content
soup_2023 = BeautifulSoup(saved_content_2023, 'html.parser')
soup_2022 = BeautifulSoup(saved_content_2022, 'html.parser')
soup_2021 = BeautifulSoup(saved_content_2021, 'html.parser')

temporada_2023_obras_actuales = soup_2023.find_all('div', class_ = 'item item-event-resume evento-programacion col-lg-4 col-md-6')
temporada_2023_obras_pasadas = soup_2023.find_all('div', class_='item item-event-resume evento-programacion item-event-old col-lg-4 col-md-6')
temporada_2022_obras_pasadas = soup_2022.find_all('div', class_='item item-event-resume evento-programacion item-event-old col-lg-4 col-md-6')
temporada_2021_obras_pasadas = soup_2021.find_all('div', class_='item item-event-resume evento-programacion item-event-old col-lg-4 col-md-6')



### Bucle
#### The last container is a video and we are not interested
temporada_2023_obras_actuales.pop()

# get_containers_data(play_containers=temporada_2023_obras_actuales, excel_file_path="plays_data_2023_actuales.xlsx")
# get_containers_data(play_containers=temporada_2023_obras_pasadas, excel_file_path="plays_data_2023_pasadas.xlsx")

#get_containers_data(play_containers=temporada_2022_obras_pasadas, excel_file_path="plays_data_2022_pasadas.xlsx")
get_containers_data(play_containers=temporada_2021_obras_pasadas, excel_file_path="plays_data_2021_pasadas.xlsx")
