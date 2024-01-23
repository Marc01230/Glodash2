import pandas as pd
import csv

folder_path1 = r"C:\Users\kemenm02\FrieslandCampina\Global SSC - Finance - Overview entities FSSC\Global overview entities FSSC.xlsx"
folder_path2 = r"C:\Users\kemenm02\FrieslandCampina\Corporate Finance Systems (FACT) - 1 Metadata overview\HFM_Metadata_20231214.xlsm"


integer_list = ["Profit_center_(PE1)"]

data_type_dict = {"CoCode": 'Int64',
                  "Profit_Center": 'Int64',
                  "Company": 'Int64',
                  "Vendor": 'Int64',
                  "Customer": 'Int64'}

def dim_Global_Overview(generate_csv):

    df1 = pd.read_excel(folder_path1, sheet_name="FSSC", skiprows=1)

    df1.columns = map(lambda x: x.replace(" ", "_"), df1.columns)

    df1 = df1.rename(columns={"HFM_entity": "HFM_Entity_Label"})

    df1.replace(to_replace='\n', value="", regex=True, inplace=True)

    df1.dropna(how="all", inplace=True)

    df1.drop(df1.tail(2).index, inplace=True)

    df2 = pd.read_excel(folder_path2, sheet_name="Entity H", skiprows=1)

    df2 = df2[["Member", "Description=English"]]

    df2 = df2.rename(columns={"Member": "HFM_Entity_Label"})
    df2 = df2.drop_duplicates(subset=["HFM_Entity_Label"])

    df1 = df1.merge(df2, how='left', on='HFM_Entity_Label')

    start = ord('A')  # starting ASCII value
    step = 1  # step between ASCII values
    mask2 = df1['Description=English'].isna()  # create a boolean mask for missing values

    df1.loc[mask2, 'Description=English'] = df1.loc[mask2, 'Description=English'].index.map(
        lambda i: chr(start + step * i)
    )

    df1["CoCode"] = df1["CoCode"].replace({3850: "AMC1"})

    #df1["CoCode"] = df1["CoCode"].replace({"B700": 700})

    df1.loc[df1["HFM_Entity_Label"] == "NGADSTICPROF", "CoCode"] = "2"

    df1.loc[df1["HFM_Entity_Label"] == "AFRICAICPROF", "CoCode"] = "3"

    df1.loc[df1["HFM_Entity_Label"] == "MILKUBATOR", "CoCode"] = "4"

    df1.loc[df1["HFM_Entity_Label"] == "UKRFCCPUkraine", "CoCode"] = "5"

    df1.loc[df1["HFM_Entity_Label"] == "NLD0413_03106499", "CoCode"] = "11"

    df1.loc[df1["HFM_Entity_Label"] == "NLD0413_03106499", "Profit_center_(PE1)"] = "11"

    df1.loc[df1["HFM_Entity_Label"] == "NLD0561WatZuiv", "CoCode"] = "12"

    #df1.loc[df1["HFM_Entity_Label"] == "UAE3170_PC100504", "Profit_center_(PE1)"] = "10"

    #df1.loc[df1["HFM_Entity_Label"] == "UAE3170_PC100504", "CoCode"] = "10"

    #df1.loc[df1["HFM_Entity_Label"] == "UAE3170_PC100505", "Profit_center_(PE1)"] = "9"

    #df1.loc[df1["HFM_Entity_Label"] == "UAE3170_PC100505", "CoCode"] = "9"

    df1.loc[df1["HFM_Entity_Label"] == "NLD3130_PC100865", "CoCode"] = "13"
    df1.loc[df1["HFM_Entity_Label"] == "NLD3130_PC100865", "Profit_center_(PE1)"] = "13"

    new_df = df1[df1['HFM_Entity_Label'] == "NLD4050_PC100784"].copy()
    new_df.loc[new_df["HFM_Entity_Label"] == "NLD4050_PC100784", "HFM_Entity_Label"] = "NLD4050_PC100784B"
    new_df.loc[new_df["HFM_Entity_Label"] == "NLD4050_PC100784B", "FSSC"] = "FSSC EMEA"
    new_df.loc[new_df["HFM_Entity_Label"] == "NLD4050_PC100784B", "Profit_center_(PE1)"] = "999999"
    df1 = df1.append(new_df, ignore_index=True)

    df1.loc[df1["HFM_Entity_Label"] == "NLD4050_PC100784", "FSSC"] = "FSSC ASIA"

    df1["New_PC"] = df1["HFM_Entity_Label"].str.extract("PC(\d+)", expand=False).astype(float)

    df1["Profit_center_(PE1)"] = df1["Profit_center_(PE1)"].fillna(0)

    df1.loc[df1["Profit_center_(PE1)"] == 0, "Profit_center_(PE1)"] = df1.loc[df1["Profit_center_(PE1)"] == 0, "New_PC"]

    df1["HFM_entity_description"] = df1["HFM_entity_description"].fillna(0)

    df1.loc[df1["HFM_entity_description"] == 0, "HFM_entity_description"] = df1.loc[df1["HFM_entity_description"] == 0, "Legal_entity"]

    df1["Profit_center_(PE1)"] = df1["Profit_center_(PE1)"].fillna(0)

    df1['Profit_center_(PE1)'] = df1['Profit_center_(PE1)'].astype(int)

    df1['CoCode_+_Profit_Center'] = df1['CoCode'].astype(str)+":"+df1['Profit_center_(PE1)'].astype(str)

    df1['CoCode_+_Company_name'] = df1['CoCode'].astype(str) + "-" + df1["HFM_entity_description"].astype(str)

    mask = df1["Description=English"].duplicated(keep="first")

    df1.loc[mask, "Description=English"] += df1.groupby("Description=English").cumcount().add(1).astype(str)

    #-----Temporary P92 request-------------------------------------

    df1.loc[df1["HFM_Entity_Label"] == "BEL9325_03201501", "In_scope_AR"] = "full scope"

    df1.loc[df1["HFM_Entity_Label"] == "DEU_04904201", "In_scope_AR"] = "full scope"

    df1.loc[df1["HFM_Entity_Label"] == "NLD0418_03100101", "In_scope_AR"] = "full scope"

    df1.loc[df1["HFM_Entity_Label"] == "NLD0418_03105501", "In_scope_AR"] = "full scope"

    df1.loc[df1["HFM_Entity_Label"] == "NLD0418_03107303", "In_scope_AR"] = "full scope"

    #--------------------------------------------------------------------------------------------

    #mask = df1["Description=English"] == "BelTrading Sell"

    #df1.loc[mask, "Description=English"] += df1.groupby("Description=English").cumcount().add(1).astype(str)

    #df1["Description=English"].fillna(method='ffill', limit=None, inplace=True)


    if generate_csv == True:
        df1.to_csv(sep='|', path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\DIM_DATA\dim_Global_FSSC_Overview.csv", index=False)

    return df1


df10 = dim_Global_Overview(generate_csv=True)

print("hello")