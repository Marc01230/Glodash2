import pandas as pd


folder_path1 = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_RAW_DATA\DIM_RAW_DATA\dim_FSSCs.xlsx"

def dim_FSSC(generate_csv):


    df=pd.read_excel(folder_path1, sheet_name="Sheet1")

    if generate_csv == True:
        df.to_csv(
            path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\DIM_DATA\dim_FSSCs.csv", index=False)

    return df


dfx = dim_FSSC(generate_csv=True)