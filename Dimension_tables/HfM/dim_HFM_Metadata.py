import pandas as pd
import csv

folder_path1 = r"C:\Users\kemenm02\FrieslandCampina\Corporate Finance Systems (FACT) - 1 Metadata overview\HFM_Metadata_20231214.xlsm"

def dim_HFM_Metadata(generate_csv):
    df1 = pd.read_excel(folder_path1, sheet_name="Entity H", skiprows=1)

    df1 = df1[["Member", "Description=English"]]

    df1 = df1.rename(columns={"Member": "HFM_Entity_Label"})

    df1 = df1.tail(-2)

    if generate_csv==True:
        df1.to_csv(path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\DIM_DATA\dim_HfM_Metadata.csv", index=False)

    return df1


df10 = dim_HFM_Metadata(generate_csv=True)

print("hello")