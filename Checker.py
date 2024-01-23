import pandas as pd

ZFM_PCTRI = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\DIM_DATA\dim_ZFM_PCTRI.csv"
fct_Overdue = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_Overdue.csv"
fct_DataAudit = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_DataAudit_log_manual_corrections.csv"
fct_Overview_Status_Phase = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_Overview_Status_Phase_1-2-3_Promotion.csv"
fct_BS_Open_Items_greater_than_6_months = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_BS_Open_items_greater_than_6_months.csv"
fct_Total_MJE = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_Total_MJE.csv"


def Check_Dimensions(generate_csv):
    dim_ZFM_PCTRI = pd.read_csv(ZFM_PCTRI)
    dim_ZFM_PCTRI_HFM_Label = dim_ZFM_PCTRI[["HFM_Entity_Label"]].drop_duplicates()
    dim_ZFM_PCTRI_HFM_Name = dim_ZFM_PCTRI[["Description=English"]].drop_duplicates()
    dim_ZFM_PCTRI_CoCode_Profit_Ctr = dim_ZFM_PCTRI[["Company_Code_+_Profit_Ctr"]].drop_duplicates()

#---------OVERVIEW---------------
    fct_Overview_Status_Phase_df = pd.read_csv(fct_Overview_Status_Phase)
    fct_Overview_Status_Phase_df = fct_Overview_Status_Phase_df[["Entity"]].drop_duplicates()

    Overview_missing_df = fct_Overview_Status_Phase_df.merge(dim_ZFM_PCTRI_HFM_Label, left_on="Entity", right_on="HFM_Entity_Label", how="left")

    Overview_missing_df.rename(columns={"Entity": "fct_Overview_Status_Phase_Entity",
                                        "HFM_Entity_Label":"dim_ZFM_PCTRI_HFM_Entity_Label"
                                         }, inplace=True)

    Overview_missing_df = Overview_missing_df[(Overview_missing_df["dim_ZFM_PCTRI_HFM_Entity_Label"].isnull())].reset_index().drop("index", axis=1)

#----------BS-OPEN-ITEMS------------
    fct_BS_Open_Items_df = pd.read_csv(fct_BS_Open_Items_greater_than_6_months, encoding="latin1")
    fct_BS_Open_Items_df = fct_BS_Open_Items_df[["Company_Code_+_Profit_Ctr"]].drop_duplicates()
    fct_BS_Open_Items_df.rename(columns={"Company_Code_+_Profit_Ctr": "fct_BS_Open_items_Company_Code_+_Profit_Ctr"
                                                      }, inplace=True)

    BS_Open_items_missing_entities_df = fct_BS_Open_Items_df.merge(dim_ZFM_PCTRI_CoCode_Profit_Ctr, left_on="fct_BS_Open_items_Company_Code_+_Profit_Ctr", right_on="Company_Code_+_Profit_Ctr", how="left")

    BS_Open_items_missing_entities_df.rename(columns={"Company_Code_+_Profit_Ctr": "dim_ZFM_PCTRI_Company_Code_+_Profit_Ctr",
                                                      }, inplace=True)

    BS_Open_items_missing_entities_df = BS_Open_items_missing_entities_df[(BS_Open_items_missing_entities_df["dim_ZFM_PCTRI_Company_Code_+_Profit_Ctr"].isnull())].reset_index().drop("index", axis=1)
#----------------------------------------------

#-----------------OVERDUE----------------------

    fct_Overdue_df = pd.read_csv(fct_Overdue)
    fct_Overdue_df = fct_Overdue_df[["CXO_Entity"]].drop_duplicates()
    Overdue_missing_df = fct_Overdue_df.merge(dim_ZFM_PCTRI_HFM_Name, left_on="CXO_Entity", right_on="Description=English", how="left")
    Overdue_missing_df = Overdue_missing_df[(Overdue_missing_df["Description=English"].isnull())].reset_index().drop("index", axis=1)
    Overdue_missing_df = Overdue_missing_df.merge(dim_ZFM_PCTRI, left_on="CXO_Entity", right_on="Description=English", how="left")




#------------DATA-AUDIT-LOG------------------
    fct_DataAudit_df = pd.read_csv(fct_DataAudit)
    fct_DataAudit_df = fct_DataAudit_df[["Entity"]].drop_duplicates()
    DataAudit_missing_df = fct_DataAudit_df.merge(dim_ZFM_PCTRI_HFM_Label, left_on = "Entity", right_on = "HFM_Entity_Label")

    DataAudit_missing_df.rename(
        columns={"HFM_Entity_Label": "dim_ZFM_PCTRI_HFM_Entity_Label",
                 "Entity": "fct_DataAudit_Entity"
                 }, inplace=True)

    DataAudit_missing_df = DataAudit_missing_df[(DataAudit_missing_df["dim_ZFM_PCTRI_HFM_Entity_Label"].isnull())].reset_index().drop(
        "index", axis=1)
#------------TOTAL-MJE---------------------
    #fct_Total_MJE_df =


    if generate_csv==True:
        DataAudit_missing_df.to_csv(
            path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\Monthly_Check\DataAudit_Missing_Entities.csv", index=False)
        Overdue_missing_df.to_csv(
            path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\Monthly_Check\Overdue_Missing_Entities.csv", index=False)
        Overview_missing_df.to_csv(
            path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\Monthly_Check\Overview_Status_Missing_Entities.csv", index=False)
        BS_Open_items_missing_entities_df.to_csv(
            path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\Monthly_Check\BS_Open_Items_missing_entities.csv", index=False)


    return Overview_missing_df


df10 = Check_Dimensions(generate_csv=True)
print("hello")