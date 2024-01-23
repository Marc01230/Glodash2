import pandas as pd


folder_path1 = r"C:\Users\kemenm02\FrieslandCampina\Global SSC - Finance - Balance Sheet Clearing Global Policy and Procedure\GL account settings and clearing framework FSSC_v20Feb2023.xlsx"

def dim_GL_framework(generate_csv):

    df=pd.read_excel(folder_path1, sheet_name="Framework")

    if generate_csv == True:
        df.to_csv(
            path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\DIM_DATA\dim_GL_Framework.csv", index=False)

    return df

dfx = dim_GL_framework(generate_csv=True)

