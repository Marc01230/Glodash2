import pandas as pd


folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_RAW_DATA\FCT_RAW_DATA\Manual_Excel_files\fct_FSSC_targets_RAW.xlsx"



def fct_Targets_for_FSSCs(generate_csv):
    df1 = pd.read_excel(folder_path, sheet_name="fct_Targets_for_FSSCs")


    if generate_csv==True:
        df1.to_csv(r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_Targets_for_FSSCs.csv", index=False)

    return df1


fct_Targets_for_FSSCs(generate_csv=True)