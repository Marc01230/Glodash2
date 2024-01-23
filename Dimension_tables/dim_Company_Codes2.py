import pandas as pd
import os


folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\DIM_DATA\dim_Global_FSSC_Overview.csv"
folder_path2 = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\DIM_DATA\dim_Global_FSSC_Overview.csv"


def dim_Company_Codes_new(generate_csv):

    df1 = pd.read_csv(folder_path, usecols=["CoCode", "HFM_entity_description", "FSSC", "In_scope_AR"], delimiter= "|")

    df2 = pd.read_csv(folder_path, usecols=["CoCode", "HFM_entity_description", "FSSC"], delimiter= "|")

    #df1 = df1.drop_duplicates(subset=["CoCode"]).reset_index()

    df1["In_scope_AR"] = df1["In_scope_AR"].fillna("0")

    dfX = df1.loc[df1["In_scope_AR"].str.contains("CR|full scope")]

    dfX = dfX.drop_duplicates(subset=["CoCode"]).reset_index()

    dfX = dfX.loc[:, ["CoCode", "In_scope_AR"]]

    df1 = df1.drop_duplicates(subset=["CoCode"]).reset_index(drop=True)

    df1 = df1.merge(dfX, on="CoCode", how="left")

    df1["In_scope_AR_y"] = df1["In_scope_AR_y"].fillna("0")

    #df1.loc[df1['In_scope_AR_y'].str.contains('TS'), 'In_scope_AR_x'] = df1.loc[df1['In_scope_AR_y'].str.contains('TS'),'In_scope_AR_y']

    df1 = df1.drop(columns="In_scope_AR_x")

    df1 = df1.rename(columns={"In_scope_AR_y": "In_scope_AR"})

    df1["CoCode"] = df1["CoCode"].astype(str)

    df1["Company_Code_+_Company_name"] = df1["CoCode"] + "-" + (df1["HFM_entity_description"])

    if generate_csv == True:
        df1.to_csv(path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\DIM_DATA\dim_Company_Codes2.csv", index=False)

    return df1

#df10 = dim_Company_Codes_new(generate_csv=True)
#print("hello")