import pandas as pd
import os


folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\DIM_DATA\dim_Global_FSSC_Overview.csv"
folder_path2 = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\DIM_DATA\dim_Global_FSSC_Overview.csv"


def dim_Company_Codes_3(generate_csv):

    df1 = pd.read_csv(folder_path, usecols=["CoCode", "HFM_entity_description", "FSSC", "In_scope_AR"], delimiter= "|")

    df2 = pd.read_csv(folder_path, usecols=["CoCode", "HFM_entity_description", "FSSC"], delimiter= "|")

    additional_cocodes = [
        "7074", "7070", "7000", "7092", "7090", "7080", "7079", "7078", "7076", "7075",
        "3420", "7088", "4090", "7091", "7008", "7005", "3930", "3220"
    ]

    # Filter df1 for the additional CoCodes
    additional_df1 = df1[df1['CoCode'].isin(additional_cocodes)]

    additional_df1 = additional_df1.drop_duplicates(subset='CoCode')

    #df1 = df1.drop_duplicates(subset=["CoCode"]).reset_index()

    df1["In_scope_AR"] = df1["In_scope_AR"].fillna("0")

    dfASIA = df1.loc[df1["FSSC"] == "FSSC ASIA"]

    dfASIA = dfASIA.loc[dfASIA['In_scope_AR'].str.contains('full scope')]

    dfASIA = dfASIA.loc[:, ["HFM_entity_description", "CoCode", "FSSC", "In_scope_AR"]]

    dfASIA = dfASIA.drop_duplicates(subset=["CoCode"]).reset_index(drop=True)

    dfEMEA = df1.loc[df1["FSSC"].isin(["FSSC EMEA", "FSSC NL"])]

    dfEMEA = dfEMEA.loc[dfEMEA["In_scope_AR"].str.contains("TS|CR|full scope|Full scope")]

    dfEMEA = dfEMEA.drop_duplicates(subset=["CoCode"]).reset_index()

    dfEMEA = dfEMEA.loc[:, ["HFM_entity_description", "CoCode", "FSSC", "In_scope_AR"]]

    df_Total = pd.concat([dfASIA, dfEMEA], axis=0)

    #dfX = df1.loc[df1["In_scope_AR"].str.contains("TS|CR|full scope")]

    #dfX = dfX.drop_duplicates(subset=["CoCode"]).reset_index()

    #dfX = dfX.loc[:, ["CoCode", "In_scope_AR"]]

    #df1 = df1.drop_duplicates(subset=["CoCode"]).reset_index(drop=True)

    #df1 = df1.merge(dfX, on="CoCode", how="left")

    # df1["In_scope_AR_y"] = df1["In_scope_AR_y"].fillna("0")
    #
    # df1.loc[df1['In_scope_AR_y'].str.contains('TS'), 'In_scope_AR_x'] = df1.loc[df1['In_scope_AR_y'].str.contains('TS'),'In_scope_AR_y']
    #
    # df1 = df1.drop(columns="In_scope_AR_y")
    #
    # df1 = df1.rename(columns={"In_scope_AR_x": "In_scope_AR"})
    #
    df_Total["CoCode"] = df_Total["CoCode"].astype(str)
    #
    df_Total["Company_Code_+_Company_name"] = df_Total["CoCode"] + "-" + (df_Total["HFM_entity_description"])

    df_Total = pd.concat([df_Total, additional_df1], ignore_index=True)

    if generate_csv == True:
        df_Total.to_csv(path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\DIM_DATA\dim_Company_Codes2.csv", index=False)

    return df_Total

df10 = dim_Company_Codes_3(generate_csv=True)
print("hello")