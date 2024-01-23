import pandas as pd


folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\Open items_2022.xlsx"
destination_path = r"C:\Users\kemenm02\OneDrive - FrieslandCampina\Desktop\GloDashDocumentation\Final files"

float_list = ['CCode_Curr_Value','Value_in_EUR']

def fct_BS_Open_items_greater_than_6_months(generate_csv):

    df1 = pd.read_excel(folder_path, sheet_name="Data", skiprows=0)

    df1.columns = map(lambda x: x.replace(" ", "_"), df1.columns)

    df1[float_list] = df1[float_list].round(decimals=2)

    df1['Company_Code_+_Profit_Ctr'] = df1['CoCode'].astype(str) + ":" + df1['Profit_Ctr'].astype(str)

    #df1["Open_item_date"] = df1["Period"].astype(str) + "/" + "01" + "/" + df1["Year"].astype(str)

    #df1["Open_item_date"] = pd.to_datetime(df1["Open_item_date"], format="%d/%m/%Y")


    def get_aging_bucket(row):
        diff = abs(row["Download_date"] - row["Open_item_date"]).days/30
        if diff > 24:
            return 4
        elif diff > 12:
            return 3
        elif diff > 6:
            return 2
        elif diff > 3:
            return 1
        else:
            return 0

    #df1["Aging_month_range"] = df1.apply(get_aging_bucket, axis=1)

    if generate_csv == True:
        df1.to_csv(r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_BS_Open_items_greater_than_6_months.csv", index=False)

    return df1

df10 = fct_BS_Open_items_greater_than_6_months(generate_csv=True)

print("Hello")