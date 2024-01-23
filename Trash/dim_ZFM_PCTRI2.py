import pandas as pd
from Dimension_tables.HfM.dim_HFM_Metadata import dim_HFM_Metadata

folder_path1 = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_RAW_DATA\DIM_RAW_DATA\ZFM_PRCTRI PE1 (2023.02.20).xlsx"
folder_path2 = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\HFM_Metadata_20230323.xlsx"
folder_path3 = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_RAW_DATA\DIM_RAW_DATA\dim_ZFM_PCTRI.xlsx"
folder_path4 = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_RAW_DATA\DIM_RAW_DATA\ZFM_PRCTRI PE9 (2023.02.20).xlsx"





def dim_ZFM_PCTRI(generate_csv):



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
