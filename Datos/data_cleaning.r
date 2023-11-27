library(tidyverse)
library(dplyr)
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

salas_teatro <- read.csv("salas_teatro.csv", sep = ";")

salas_cine <- read.csv("salas_cine.csv", sep = ";")


salas_conciertos <- read.csv("salas_conciertos.csv", sep = ";")


eventos <- read.csv("eventos-culturales-100.csv", sep = ";")

centros_enventos <- unique(eventos["NOMBRE.INSTALACION"])


eventos_teatro <- 
  



# Your list of strings
instalaciones <- c("Teatro Municipal de Vallecas", "Teatro Municipal de Títeres. Parque de El Retiro", "Teatro Español")

# Filter the dataset
filtered_dataset <- eventos %>%
  filter(NOMBRE.INSTALACION %in% instalaciones)


# Specify the file path where you want to save the CSV file
csv_file_path <- "eventos_teatro.csv"

# Save the filtered dataset to a CSV file
write.csv(filtered_dataset, file = csv_file_path, row.names = FALSE)

# Print a message to confirm the save
cat("Filtered dataset saved to", csv_file_path, "\n")
