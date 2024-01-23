import pandas as pd
from dateutil.relativedelta import relativedelta


source_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_BS_Open_items.csv"
destination_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\investigation_files\GLs.csv"

def fct_BS_Open_items_greater_than_6_months(generate_csv):

    df1 = pd.read_csv(source_path)

    df1 = df1[['G/L']]

    df1 = df1.drop_duplicates()

    df1 = df1.reset_index(drop=True)

    if generate_csv == True:
        df1.to_csv(destination_path, index=False)

    return df1

df10 = fct_BS_Open_items_greater_than_6_months(generate_csv=True)

print("Hello")