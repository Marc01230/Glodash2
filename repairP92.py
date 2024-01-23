import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file

file_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_BS_Open_items.csv"
# Read the CSV file into a DataFrame
data = pd.read_csv(file_path)

# Specify company codes to delete

# Filter rows where 'company code' is in the specified list and keep the rest
data = data[data['Download_date'] != '2023-11-30']

data.to_csv(file_path, index=False)

print("hello")