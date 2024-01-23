import pandas as pd


folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_RAW_DATA\DIM_RAW_DATA\dim_CEPC_PE1.xlsx"
folder_path2 = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_RAW_DATA\DIM_RAW_DATA\dim_CEPC_PE9.xlsx"


def dim_CEPC(generate_csv):
    dfPE1 = pd.read_excel(folder_path, sheet_name="Sheet1")

    dfPE1.columns = map(lambda x: x.replace(" ", "_"), dfPE1.columns)

    dfPE1 = dfPE1[["Profit_Ctr", "Name.1", "Long_Text", "PrCtr_text"]]

    dfPE9 = pd.read_excel(folder_path2, sheet_name="Sheet1")

    dfPE9.columns = map(lambda x: x.replace(" ", "_"), dfPE9.columns)

    dfPE9 = dfPE1[["Profit_Ctr", "Name.1", "Long_Text", "PrCtr_text"]]

    df_PE1_PE9 = pd.concat([dfPE1,dfPE9], ignore_index=True)

    df_PE1_PE9 = df_PE1_PE9.drop_duplicates(subset=["Profit_Ctr"])



    if generate_csv == True:
        df_PE1_PE9.to_csv(path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\DIM_DATA\dim_CEPC.csv",
            index=False)

    return df_PE1_PE9


#df10 = dim_CEPC(generate_csv=False)
#print("hello")