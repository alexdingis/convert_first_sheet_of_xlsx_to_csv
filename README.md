# convert_first_sheet_of_xlsx_to_csv
for a directory full of xlsx files, convert the first sheet of the xlsx files to csv files

# Why write this code?
Using pandas to parse an Excel file is considerably slower than parsing a CSV file. For faster performance when needing to iterate through many spreadsheets, it is faster to parse CSV files than standard Excel spreadsheets.
