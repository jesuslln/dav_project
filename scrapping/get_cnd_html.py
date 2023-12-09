from bs4 import BeautifulSoup
import requests

cnd_plays_2023 = "https://dramatico.mcu.es/programacion/"
cnd_plays_2022 = "https://dramatico.mcu.es/espectaculos/"
cnd_plays_2021 = "https://dramatico.mcu.es/temporada-2021-2022-espectaculos-temporada-2021-2022/"


# Making a GET request
r_2023 = requests.get(cnd_plays_2023)
r_2022 = requests.get(cnd_plays_2022)
r_2021 = requests.get(cnd_plays_2021)


# check status code for response received
# success code - 200
print(r_2023)
print(r_2022)
print(r_2021)


soup_2023 = BeautifulSoup(r_2023.content.decode('utf-8'), 'html.parser')
soup_2022 = BeautifulSoup(r_2022.content.decode('utf-8'), 'html.parser')
soup_2021 = BeautifulSoup(r_2021.content.decode('utf-8'), 'html.parser')

# Convert BeautifulSoup object to a string
soup_2023_str = soup_2023.prettify()
soup_2022_str = soup_2022.prettify()
soup_2021_str = soup_2021.prettify()

# Save the string to a text file
with open('output_2023.txt', 'w', encoding='utf-8') as file:
    file.write(soup_2023_str)

with open('output_2022.txt', 'w', encoding='utf-8') as file:
    file.write(soup_2022_str)

with open('output_2021.txt', 'w', encoding='utf-8') as file:
    file.write(soup_2021_str)

