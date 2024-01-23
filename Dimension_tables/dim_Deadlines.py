import pandas as pd

folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\Deadlines.xlsx"


def dim_Deadlines(generate_csv):
    df1 = pd.read_excel(folder_path, sheet_name="Sheet1")

    df1.columns = map(lambda x: x.replace(" ", "_"), df1.columns)

    if generate_csv == True:
        df1.to_csv(path_or_buf=r"C:\Users\kemenm02\OneDrive - FrieslandCampina\Desktop\GloDashDocumentation\Final files\python_csvs\dim_Deadlines.csv", index=False)

    return df1

