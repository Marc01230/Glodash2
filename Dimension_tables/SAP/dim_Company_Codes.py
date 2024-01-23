import pandas as pd
import os


folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\DIM_DATA\dim_ZFM_PCTRI.csv"

Blocked_sales_order_company_code_list = [3100,5120,5100,4010,3130,5090,5000,3000,3640,4320,4220,4050,3230,3330,3520,3540,3550,3560,3660,3650,3820, 3080,3160,3580,3590,3600,3610,3850,3860,3870,3900,3910,4290,4330,5170,5180]

def dim_Company_Codes(generate_csv):

    df1 = pd.read_csv(folder_path)

    df1 = pd.read_csv(folder_path, usecols=["Company_Code","Company_Name","FSSC_Description"])

    df1 = df1.drop_duplicates(subset=["Company_Code"])

    def Blocked_sales_orders(x):
        if x in Blocked_sales_order_company_code_list:
            return "Blocked sales orders"
        else:
            return "Other"

    df1["Blocked_sales_order_scope"] = df1["Company_Code"].apply(Blocked_sales_orders)

    df1["Company_Code"] = df1["Company_Code"].astype(str)

    df1["Company_Code_+_Company_name"] = df1["Company_Code"] + "-" + (df1["Company_Name"])

    if generate_csv == True:
        df1.to_csv(path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\DIM_DATA\dim_Company_Codes.csv", index=False)

    return df1

#df10 = dim_Company_Codes(generate_csv=False)

#print("hello")