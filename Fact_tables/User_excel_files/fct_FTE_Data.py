import pandas as pd


folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\FTEs.xlsx"


def fct_FTE_Template(generate_csv):

    df1 = pd.read_excel(folder_path, sheet_name="FTE template", skiprows=0)


    if generate_csv==True:
        df1.to_csv(path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_FTE_Template.csv", index=False)

    return df1

fct_FTE_Template(generate_csv=True)
print("hello")
