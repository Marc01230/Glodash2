source =r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_Trade_Spend_aged_open_items.csv"

import pandas as pd

df = pd.read_csv(source)
df.to_csv(path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_Trade_Spend_aged_open_items.csv" ,index=False)

import pandas as pd

# Load the CSV file
df = pd.read_csv('your_file.csv')

# Display the row at position 20
print(df.iloc[19])  # Note that Python uses zero-based indexing
