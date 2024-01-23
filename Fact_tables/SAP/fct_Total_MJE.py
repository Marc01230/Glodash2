import pandas as pd


folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\2022 - Total MJE.xlsx"

sum_column_list = ["Transaction_Code_1","Transaction_Code_2", "Transaction_Code_3", "Transaction_Code_4", "Transaction_Code_5", "Transaction_Code_6"]

def fct_Total_MJE(generate_csv):

    df1 = pd.read_excel(folder_path, sheet_name="Tabelle1", skiprows=0)

    df1.columns = map(lambda x: x.replace(" ", "_"), df1.columns)

    df1[sum_column_list] = df1[sum_column_list].fillna(0)

    df1[sum_column_list] = df1[sum_column_list].astype(int)

    df1["Sum_of_Transaction_Codes"] = df1[sum_column_list].sum(axis=1)

    #print(df1)

    if generate_csv == True:
        df1.to_csv(path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_Total_MJE.csv", index=False)

    return df1

df10 = fct_Total_MJE(generate_csv=True)
print("hello")