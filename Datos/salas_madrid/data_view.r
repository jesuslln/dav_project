library(tidyverse)
library(openxlsx)
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

my_data <- read.csv("ocio_salas_no_comas.csv", sep = ";")

# Replace semicolons within fields with a different character (e.g., "|")
read_file <- readLines("ocio_salas - Copy.csv", warn = FALSE)
read_file <- gsub('("[^"]*);([^"]*")', '\\1|\\2', read_file, perl = TRUE)
con <- textConnection(read_file)
data <- read.csv(con, sep = ";", header = TRUE)
close(con)


# Define the number of columns (adjust as needed)
num_columns <- 32

# Read the problematic CSV file line by line
file_path <- "ocio_salas.csv"

# Create a data frame to store clean data
cleaned_data <- data.frame(matrix(NA, ncol = num_columns, nrow = 0))

# Create a data frame to store problematic rows
problematic_rows <- data.frame(matrix(NA, ncol = num_columns, nrow = 0))

# Open the file and read it line by line
con <- file(file_path, "r", encoding = "UTF-8")
while (length(line <- readLines(con, n = 1, warn = FALSE)) > 0) {
  tryCatch({
    # Split the values in each line by semicolon
    values <- unlist(strsplit(line, ";"))
    
    # Trim leading and trailing whitespaces
    #values <- trimws(values)
    
    # Append the values to the cleaned_data data frame
    cleaned_data <- rbind(cleaned_data, values)
  }, error = function(e) {
    print(paste("Problematic Line:", line))
    # If an error occurs, store the problematic row
    problematic_rows <- rbind(problematic_rows, line)
  })
}

# Close the file connection
close(con)

# Print the cleaned data
print(cleaned_data)

# Print the problematic rows
print(problematic_rows)

# Save the cleaned data to a new CSV file
write.csv(cleaned_data, "cleaned_data.csv", row.names = FALSE)

# Save the problematic rows to a new Excel file
write.xlsx(problematic_rows, "problematic_rows.xlsx")
