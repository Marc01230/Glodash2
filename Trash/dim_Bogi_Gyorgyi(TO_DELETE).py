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

data_type_dict = {"Company_Code": 'Int64',
                  "Profit_Center": 'Int64',
                  "Company": 'Int64',
                  "Vendor": 'Int64',
                  "Customer": 'Int64'}

def dim_PE1():

    RAW_PE1df = pd.read_excel(folder_path2, sheet_name="Sheet1", skiprows=0)

    RAW_PE1df.columns = map(lambda x: x.replace(" ", "_"), RAW_PE1df.columns)

    # The Name_1 column represents the HFM Entity Label

    RAW_PE1df = RAW_PE1df.rename(
        columns={"Name_1": "HFM_Entity_Label", "CoCd": "Company_Code", "FSSC_Desc": "FSSC_Description"})

    RAW_PE1df[integer_list] = RAW_PE1df[integer_list].fillna(0)

    RAW_PE1df[integer_list] = RAW_PE1df[integer_list].astype(int)

    # We take into scope what is assigned to any of the FSSCs

    RAW_PE1df = RAW_PE1df[(RAW_PE1df["FSSC_Description"] == "FSSC EMEA") | (RAW_PE1df["FSSC_Description"] == "FSSC ASIA") | (
            RAW_PE1df["FSSC_Description"] == "FSSC NL")].reset_index().drop("index", axis=1)

    # We need only the active ones.

    RAW_PE1df = RAW_PE1df[(RAW_PE1df["FM_Stat_Desc"] == "ACTIVE")].reset_index().drop("index", axis=1)

    # I discovered that there is one empty entity, so we drop that one:

    RAW_PE1df = RAW_PE1df[RAW_PE1df["Legal_Entity"] != "EMPTY_L22"].reset_index().drop("index", axis=1)

    return RAW_PE1df


def dim_PE9():

    RAW_PE9df = pd.read_excel(folder_path1, sheet_name="Sheet1", skiprows=0)

    RAW_PE9df.columns = map(lambda x: x.replace(" ", "_"), RAW_PE9df.columns)

    # For the concatenation we need the column names to be identical with PE1
    # The Name_1 column represents the HFM Entity Label

    RAW_PE9df = RAW_PE9df.rename(
        columns={"Name_1": "HFM_Entity_Label", "CoCd": "Company_Code", "FSSC_Desc": "FSSC_Description",
                 "FM_Desc": "FM_Stat_Desc", "OPCO_lvl1": "OPCO_Lvl_1", "OPCO_Desc": "OPCO_Lvl_Desc"})

    RAW_PE9df[integer_list] = RAW_PE9df[integer_list].fillna(0)

    RAW_PE9df[integer_list] = RAW_PE9df[integer_list].astype(int)

    # We take into scope what is assigned to any of the FSSCs

    RAW_PE9df = RAW_PE9df[(RAW_PE9df["FSSC_Description"] == "FSSC EMEA") | (RAW_PE9df["FSSC_Description"] == "FSSC ASIA") | (
            RAW_PE9df["FSSC_Description"] == "FSSC NL")].reset_index().drop("index", axis=1)

    # We need only the active ones.

    RAW_PE9df = RAW_PE9df[(RAW_PE9df["FM_Stat_Desc"] == "ACTIVE")].reset_index().drop("index", axis=1)

    return RAW_PE9df

def Current_scope():

    current_scope_df = pd.read_csv(folder_path3)

    current_scope_df = current_scope_df[["HFM_Entity_Label", "RTR_Scope", "AR_Scope"]]

    return current_scope_df


def dim_RAW_PE1PE9(generate_csv):

    PE1 = dim_PE1()
    #PE1 = PE1.reset_index(drop=True)
    #PE1 = PE1.sort_index()


    PE9 = dim_PE9()
    #PE9.reset_index(inplace=True)
    #PE9.index = range(468, 468+len(PE9))
    #PE9.drop("index", axis=1, inplace=True)
    #PE9 = PE9.sort_index()

    #Current_scope  = pd.read_csv(folder_path3)



    RAW_PE1PE9 = pd.concat([PE1, PE9], ignore_index=True)

    RAW_PE1PE9 = RAW_PE1PE9.merge(Current_scope, on= "HFM_Entity_Label", how="left")



    if generate_csv == True:
        RAW_PE1PE9.to_excel(
            r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_RAW_DATA\DIM_RAW_DATA\dim_ZFM_PCTRI_X.xlsx",
            index=False)

    return RAW_PE1PE9


df11 = Current_scope()
df10 = dim_RAW_PE1PE9(generate_csv=False)
print("hello")