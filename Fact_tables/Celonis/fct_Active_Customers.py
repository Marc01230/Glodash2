import numpy as np
import pandas as pd


folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\Active customers 1.7.2022.xlsx"


def fct_Active_customer(generate_csv):

    df1 = pd.read_excel(folder_path, sheet_name="Sheet1")

    df1.columns = map(lambda x: x.replace(" ", "_"), df1.columns)

    df1["Company_code"] = df1["Company_Code"].str.slice(0,4)

    df1["Company_name"] = df1["Company_Code"].str.slice(5)

    df1 = df1[df1["FSSC_Description"].notnull()]

    #cols = df1.columns.tolist()

    df1 = df1.reindex(columns = ["Company_code", "Company_name", '#_Billings', '#_Items', 'Customers_Open', '#_Open_Billings', '#_Open_Items', 'Total_Value', 'Open_Value', '%', 'Date', 'FSSC_Description'])

    if generate_csv == True:
        df1.to_csv(df1.to_csv(path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_Active_Customers.csv", index=False))

    return df1

#df10 = fct_Active_customer(generate_csv=False)
#print("hello")