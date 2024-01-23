import pandas as pd
from Dimension_tables.HfM.dim_HFM_Metadata import dim_HFM_Metadata

folder_path1 = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_RAW_DATA\DIM_RAW_DATA\ZFM_PRCTRI PE1 (2023.02.20).xlsx"
folder_path2 = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\HFM_Metadata_20230323.xlsx"
folder_path3 = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_RAW_DATA\DIM_RAW_DATA\dim_ZFM_PCTRI.xlsx"
folder_path4 = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_RAW_DATA\DIM_RAW_DATA\ZFM_PRCTRI PE9 (2023.02.20).xlsx"

integer_list = ["Company_Code",
                "Profit_Ctr",
                "Co.",
                "Vendor",
                "Customer",
                "FSSC"]

data_type_dict = {"Company_Code": 'Int64',
                  "Profit_Center": 'Int64',
                  "Company": 'Int64',
                  "Vendor": 'Int64',
                  "Customer": 'Int64'}

def PE1_Table():
    PE1df = pd.read_excel(folder_path1, sheet_name="Sheet1", skiprows=0)

    PE1df.columns = map(lambda x: x.replace(" ", "_"), PE1df.columns)

    # The Name_1 column represents the HFM Entity Label

    PE1df = PE1df.rename(columns={"Name_1": "HFM_Entity_Label", "CoCd": "Company_Code", "FSSC_Desc": "FSSC_Description"})

    PE1df[integer_list] = PE1df[integer_list].fillna(0)

    PE1df[integer_list] = PE1df[integer_list].astype(int)

    # We take into scope what is assigned to any of the FSSCs

    PE1df = PE1df[(PE1df["FSSC_Description"] == "FSSC EMEA") | (PE1df["FSSC_Description"] == "FSSC ASIA") | (PE1df["FSSC_Description"] == "FSSC NL")].reset_index().drop("index", axis=1)

    # We need only the active ones.

    PE1df = PE1df[(PE1df["FM_Stat_Desc"] == "ACTIVE")].reset_index().drop("index", axis=1)

    # I discovered that there is one empty entity, so we drop that one:

    PE1df = PE1df[PE1df["Legal_Entity"] != "EMPTY_L22"].reset_index().drop("index", axis=1)

    return PE1df

def PE9_Table():
    PE9df = pd.read_excel(folder_path4, sheet_name="Sheet1", skiprows=0)

    PE9df.columns = map(lambda x: x.replace(" ", "_"), PE9df.columns)

    #For the concatenation we need the column names to be identical with PE1
    # The Name_1 column represents the HFM Entity Label

    PE9df = PE9df.rename(
        columns={"Name_1": "HFM_Entity_Label", "CoCd": "Company_Code", "FSSC_Desc": "FSSC_Description",
                 "FM_Desc": "FM_Stat_Desc", "OPCO_lvl1": "OPCO_Lvl_1", "OPCO_Desc": "OPCO_Lvl_Desc"})


    PE9df[integer_list] = PE9df[integer_list].fillna(0)

    PE9df[integer_list] = PE9df[integer_list].astype(int)

    # We take into scope what is assigned to any of the FSSCs

    PE9df = PE9df[(PE9df["FSSC_Description"] == "FSSC EMEA") | (PE9df["FSSC_Description"] == "FSSC ASIA") | (PE9df["FSSC_Description"] == "FSSC NL")].reset_index().drop("index", axis=1)

    # We need only the active ones.

    PE9df = PE9df[(PE9df["FM_Stat_Desc"] == "ACTIVE")].reset_index().drop("index", axis=1)

    return PE9df

def dim_ZFM_PCTRI(generate_csv):

    PE1 = PE1_Table()

    PE9 = PE9_Table()

    PE1PE9 = pd.concat([PE1, PE9], ignore_index=True)

    General_scope = pd.read_excel(folder_path3, sheet_name="Sheet1")

    General_scope = General_scope[["HFM_Entity_Label", "RTR_Scope", "AR_Scope"]]

    PE1PE9 = PE1PE9.merge(General_scope, on= "HFM_Entity_Label", how="left")

    #PE1PE9 = PE1PE9.drop("Description=English", axis=1)

    PE1PE9[["AR_Scope","RTR_Scope"]] = PE1PE9[["AR_Scope", "RTR_Scope"]].fillna("Missing_Scope_Input")

    dim_HFM = dim_HFM_Metadata(generate_csv=False)

    dim_HFM = dim_HFM.drop_duplicates(subset=["HFM_Entity_Label"])

    PE1PE9 = PE1PE9.merge(dim_HFM, how = 'left', on="HFM_Entity_Label")

    mask = PE1PE9["Description=English"] == "BelTrading Sell"

    PE1PE9.loc[mask, "Description=English"] += PE1PE9.groupby("Description=English").cumcount().add(1).astype(str)

    #Based on the feedback of our collegues from the business side, we can introduce the following convention for the legacy entities:

    PE1PE9["HFM_Entity_Label"] = PE1PE9["HFM_Entity_Label"].astype(str)

    PE1PE9.loc[PE1PE9["Sys_Desc"] == "GPF550", "Company_Code"] = 50

    PE1PE9.loc[PE1PE9["Sys_Desc"] == "HPF570", "Company_Code"] = 70

    PE1PE9.loc[PE1PE9["Sys_Desc"] == "FF400", "Company_Code"] = 700

    #-------------------------------------------------------------------------------------
    # Where we have 0 company codes we extract from the HFM_Label the number:

    PE1PE9["Company_Code"] = PE1PE9["Company_Code"].mask(PE1PE9["Company_Code"]==0, PE1PE9["HFM_Entity_Label"].str.extract(r'^.{3}(.{4})', expand=False))

    PE1PE9["Profit_Ctr"] = PE1PE9["Profit_Ctr"].fillna(0)

    #PE1PE9["Profit_Ctr"] = PE1PE9["Profit_Ctr"].mask(PE1PE9["Profit_Ctr"] == 0, PE1PE9["HFM_Entity_Label"].str.extract(r'PC(.*)'))

    PE1PE9["New_PC"] = PE1PE9["HFM_Entity_Label"].str.extract("PC(\d+)", expand=False).astype(float)

    PE1PE9.loc[PE1PE9["Profit_Ctr"] == 0, "Profit_Ctr"] = PE1PE9.loc[PE1PE9["Profit_Ctr"] == 0, "New_PC"]

    PE1PE9.loc[PE1PE9["HFM_Entity_Label"] == "DEU_04904201", "Company_Code"] = "1"

    PE1PE9.loc[PE1PE9["HFM_Entity_Label"] == "NGADSTICPROF", "Company_Code"] = "2"

    PE1PE9.loc[PE1PE9["HFM_Entity_Label"] == "AFRICAICPROF", "Company_Code"] = "3"

    PE1PE9.loc[PE1PE9["HFM_Entity_Label"] == "MILKUBATOR", "Company_Code"] = "4"

    PE1PE9.loc[PE1PE9["HFM_Entity_Label"] == "UKRFCCPUkraine", "Company_Code"] = "5"

    #-------------------------------------------------------------------------------
    #Hellas:

    #PE1PE9.loc[PE1PE9["HFM_Entity_Label"] == "GRCFrHellas_FS", "Company_Code"] = "6"

    #--------------------------------------------------------------------------------

    PE1PE9.loc[PE1PE9["HFM_Entity_Label"] == "NLD0418_03105501", "Company_Code"] = "7"

    PE1PE9.loc[PE1PE9["HFM_Entity_Label"] == "NLD0418_03105501", "Profit_Ctr"] = "7"

    PE1PE9.loc[PE1PE9["HFM_Entity_Label"] == "NLD0418_03107303", "Company_Code"] = "8"

    PE1PE9.loc[PE1PE9["HFM_Entity_Label"] == "NNLD0418_03107303", "Profit_Ctr"] = "8"

    PE1PE9.loc[PE1PE9["HFM_Entity_Label"] == "NLD0418_03100101", "Company_Code"] = "9"

    PE1PE9.loc[PE1PE9["HFM_Entity_Label"] == "NLD0418_03100101", "Profit_Ctr"] = "9"

    #------------------------------------------------------------------------
    #Kievit:

    #PE1PE9.loc[PE1PE9["HFM_Entity_Label"] == "DEU_04910801", "Company_Code"] = "10"

    #-----------------------------------------------------------------------

    PE1PE9.loc[PE1PE9["HFM_Entity_Label"] == "NLD0413_03106499", "Company_Code"] = "11"

    PE1PE9.loc[PE1PE9["HFM_Entity_Label"] == "NLD0413_03106499", "Profit_Ctr"] = "11"

    PE1PE9.loc[PE1PE9["HFM_Entity_Label"] == "NLD0561WatZuiv", "Company_Code"] = "12"

    PE1PE9["Profit_Ctr"] = PE1PE9["Profit_Ctr"].fillna(PE1PE9["Company_Code"])

    PE1PE9["Company_Code"] = PE1PE9["Company_Code"].astype(str)

    PE1PE9["Company_Code"] = PE1PE9["Company_Code"].astype(str)

    PE1PE9["Company_Name"] = PE1PE9["Company_Name"].fillna("Missing Company name")

    PE1PE9.loc[PE1PE9["Company_Name"] == "Missing Company name", "Company_Name"] = PE1PE9.loc[PE1PE9["Company_Name"] == "Missing Company name", "Name_2"]

    PE1PE9["Company_Code_+_Company_name"] = PE1PE9["Company_Code"].str.cat(PE1PE9["Company_Name"], sep="-")

    PE1PE9["Profit_Ctr"] = PE1PE9["Profit_Ctr"].fillna(0)

    PE1PE9["Profit_Ctr"] = PE1PE9["Profit_Ctr"].astype(int)

    PE1PE9["Profit_Ctr"] = PE1PE9["Profit_Ctr"].astype(str)

    PE1PE9["Company_Code_+_Profit_Ctr"] = PE1PE9["Company_Code"].str.cat(PE1PE9["Profit_Ctr"], sep=":")


    if generate_csv == True:
        PE1PE9.to_csv(
            path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\DIM_DATA\dim_ZFM_PCTRI.csv", index=False)

    return PE1PE9

df10 = dim_ZFM_PCTRI(generate_csv=False)
print(df10)
