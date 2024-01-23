import pandas as pd


folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\BS track format.xlsx"

def fct_Global_BS_submission_track(generate_csv):
    df1 = pd.read_excel(folder_path, sheet_name="Sheet2")

    if generate_csv==True:
        df1.to_csv(path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_Global_BS_submission_track.csv", index=False)

    return df1

df10 = fct_Global_BS_submission_track(generate_csv=True)
print("hello")
