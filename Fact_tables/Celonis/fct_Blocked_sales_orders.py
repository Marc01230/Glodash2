import pandas as pd


folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\Blocked Sales Orders (2).xlsx"


def fct_Blocked_sales_orders(generate_csv):

    df1 = pd.read_excel(folder_path, sheet_name="blocked sales orders", skiprows=0)

    #df1 = df1.rename(columns={'"_CEL_O2C_CASES"."BUKRSVF" AS""': 'Merged'})

    #df1.columns = map(lambda x: x.replace(" ", "_"), df1.columns)
    #df1.columns = map(lambda x: x.replace("'", "|"), df1.columns)

    df1 = df1.rename(columns={'"_CEL_O2C_CASES"."BUKRSVF" AS ""': 'Celonis_code'})

    df1["Company_Code"] = [x[:4] for x in df1['Celonis_code']]

    df1["Company_Code"] = df1["Company_Code"].astype(int)

    df1.loc[df1["Company_Code"]== 8888, "Company_Code"] = "AMC1"

    #df1["Company_Code"] = df1['Celonis_code'][:4]

    #print(df1)

    if generate_csv == True:
        df1.to_csv(path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_Blocked_sales_orders.csv", index= False)


    return df1

df10 = fct_Blocked_sales_orders(generate_csv=True)

print("hello")