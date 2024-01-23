import pandas as pd

folder_path1 = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_RAW_DATA\DIM_RAW_DATA\2023.03.21 ZFM_PRCTRI PE9_.xlsx"
folder_path2 = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_RAW_DATA\DIM_RAW_DATA\2023.03.21 ZFM_PRCTRI PE1_.xlsx"
folder_path3 = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\DIM_DATA\dim_ZFM_PCTRI.csv"

integer_list = ["Company_Code",
                "Profit_Ctr",
                "Co.",
                "Supplier",
                "Customer",
                "FSSC"]

PE1_column_list = ['Number', 'System', 'Sys_Desc', 'FM_Stat', 'FM_Stat_Desc',
       'Company_Code', 'Company_Name', 'Legal_Entity',
       'Legal_Entity_Description', 'Profit_Ctr', 'Area', 'Long_Text', 'Co.',
       'HFM_Entity_Label', 'Name_2', 'Supplier', 'Name_1.1', 'Customer',
       'Name_1.2', 'BG_Group', 'Business_Desc', 'OPCO_Lvl_1', 'OPCO_Lvl_Desc',
       '30_Characters', 'OPCO_Level_Description', '30_Characters.1',
       'OPCO_Level_Description.1', '30_Characters.2',
       'OPCO_Level_Description.2', '30_Characters.3',
       'FSSC', 'FSSC_Description']

PE9_column_list = ['Number', 'System', 'Sys_Desc', 'FM_Stat', 'FM_Stat_Desc',
       'Company_Code', 'Company_Name', 'Legal_Entity',
       'Legal_Entity_Description', 'Profit_Ctr', 'Area', 'Long_Text', 'Co.',
       'HFM_Entity_Label', 'Name_2', 'Supplier', 'Name_1.1', 'Customer',
       'Name_1.2', 'BG_Group', 'Business_Desc', 'OPCO_lvl1', 'OPCO_Lvl_Desc',
       '30_Characters', 'OPCO_Level_Description', '30_Characters.1',
       'OPCO_Level_Description.1', '30_Characters.2',
       'OPCO_Level_Description.2', '30_Characters.3',
       'FSSC', 'FSSC_Description']


def PE1():

    PE1df = pd.read_excel(folder_path2)

    PE1df.columns = map(lambda x: x.replace(" ", "_"), PE1df.columns)

    # The Name_1 column represents the HFM Entity Label

    PE1df = PE1df.rename(
        columns={"Name_1": "HFM_Entity_Label", "CoCd": "Company_Code", "FSSC_Desc": "FSSC_Description"})

    PE1df = PE1df[PE1_column_list]

    PE1df[integer_list] = PE1df[integer_list].fillna(0)

    PE1df[integer_list] = PE1df[integer_list].astype(int)

    # We take into scope what is assigned to any of the FSSCs

    PE1df = PE1df[(PE1df["FSSC_Description"] == "FSSC EMEA") | (PE1df["FSSC_Description"] == "FSSC ASIA") | (
            PE1df["FSSC_Description"] == "FSSC NL")].reset_index().drop("index", axis=1)

    # We need only the active ones.

    PE1df = PE1df[(PE1df["FM_Stat_Desc"] == "ACTIVE")].reset_index().drop("index", axis=1)

    # I discovered that there is one empty entity, so we drop that one:

    PE1df = PE1df[PE1df["Legal_Entity"] != "EMPTY_L22"].reset_index().drop("index", axis=1)

    return PE1df



def PE9():

    PE9df = pd.read_excel(folder_path1)

    PE9df.columns = map(lambda x: x.replace(" ", "_"), PE9df.columns)

    # For the concatenation we need the column names to be identical with PE1
    # The Name_1 column represents the HFM Entity Label

    PE9df = PE9df.rename(
        columns={"Name_1": "HFM_Entity_Label", "CoCd": "Company_Code", "FSSC_Desc": "FSSC_Description",
                 "FM_Desc": "FM_Stat_Desc"})

    PE9df = PE9df[PE9_column_list]

    #"OPCO_lvl1": "OPCO_Lvl_1", "OPCO_Desc": "OPCO_Level_Description

    PE9df[integer_list] = PE9df[integer_list].fillna(0)

    PE9df[integer_list] = PE9df[integer_list].astype(int)

    # We take into scope what is assigned to any of the FSSCs

    PE9df = PE9df[(PE9df["FSSC_Description"] == "FSSC EMEA") | (PE9df["FSSC_Description"] == "FSSC ASIA") | (
            PE9df["FSSC_Description"] == "FSSC NL")].reset_index().drop("index", axis=1)

    # We need only the active ones.

    PE9df = PE9df[(PE9df["FM_Stat_Desc"] == "ACTIVE")].reset_index().drop("index", axis=1)

    return PE9df


def Current_scope():

    current_scope_df = pd.read_csv(folder_path3)

    current_scope_df = current_scope_df[["HFM_Entity_Label", "RTR_Scope", "AR_Scope"]]

    return current_scope_df


def RAW_PE1_PE9(generate_csv):

    PE1df = PE1()
    PE9df = PE9()

    current_scope_df1 = Current_scope()

    RAW_PE1_PE9df = pd.concat([PE1df, PE9df], ignore_index=True)

    RAW_PE1_PE9df = RAW_PE1_PE9df.merge(current_scope_df1, on="HFM_Entity_Label", how="left")

    RAW_PE1_PE9df[["RTR_Scope", "AR_Scope"]] = RAW_PE1_PE9df[["RTR_Scope", "AR_Scope"]].fillna("Missing_Scope_Input")

    if generate_csv == True:
        RAW_PE1_PE9df.to_csv(path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_RAW_DATA\DIM_RAW_DATA\RAW_dim_ZFM_PCTRI.csv", index=False)

    return RAW_PE1_PE9df

df12 = RAW_PE1_PE9(generate_csv=False)
df10 = PE1()
df11 = PE9 ()
print("hello")