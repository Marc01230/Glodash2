import numpy as np
import pandas as pd
import datetime

file_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\TS KPI Customer Trade Spend Aged Open Items .xlsx"
file_path2 = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\FTM_Template_Asia.xlsx"

def fct_Trade_Spend_Aged_open_items(generate_csv):
    dfEMEA = pd.read_excel(file_path, sheet_name="Sheet1")
    dfEMEA.columns = map(lambda x: x.replace(" ", "_"), dfEMEA.columns)
    dfEMEA = dfEMEA.rename(columns={"Profit_Ctr": "Profit_center"})

    dfEMEA['Days'] = (dfEMEA["End_of_Month"] - dfEMEA["Pstng_Date"])


    dfASIA = pd.read_excel(file_path2, sheet_name="Template")
    dfASIA.columns = map(lambda x: x.replace(" ", "_"), dfASIA.columns)
    dfASIA = dfASIA.rename(columns={"End_of_month": "End_of_Month"})

    column_order = ["Date", "CoCd", "Doc._Date","Trade_Spend_check", "Pstng_Date", "End_of_Month", "Days", "Profit_center"]

    dfEMEA = dfEMEA.reindex(columns=column_order)
    dfASIA = dfASIA.reindex(columns=column_order)

    Total = pd.concat([dfEMEA,dfASIA], ignore_index=True)

    Total["Date"] = Total["Date"].fillna(Total['End_of_Month'].dt.strftime('%b %Y'))

    Total['Pstng_Date'] = pd.to_datetime(Total['Pstng_Date'])

    def get_aging_bucket(row):
        diff = abs(row["End_of_Month"] - row["Pstng_Date"]).days
        if diff <= 30:
            return "0-30 days"
        elif diff <= 60:
            return "31-60 days"
        elif diff <= 90:
            return "61-90 days"
        elif diff <= 180:
            return "91-180 days"
        else:
            return "180+ days"

    def get_aging_bucket2(row):
        diff = abs(row['Days'])
        if diff <= 30:
            return "0-30 days"
        elif diff <= 60:
            return "31-60 days"
        elif diff <= 90:
            return "61-90 days"
        elif diff <= 180:
            return "91-180 days"
        else:
            return "180+ days"
    def generate_aging_bucket_data_column(row):
        if row["CoCd"] == "AMC1":
            return get_aging_bucket2(row)
        else:
            return get_aging_bucket(row)

    Total["Aging_Bucket"] = Total.apply(generate_aging_bucket_data_column, axis=1)

    Total["Trade_Spend_check"] = Total["Trade_Spend_check"].fillna("Trade Spend")

    Total["CoCd"] = Total["CoCd"].astype(str)

    Total["Profit_center"] = Total["Profit_center"].fillna(0)

    Total["Profit_center"] = Total["Profit_center"].astype(int)

    Total["Profit_center"] = Total["Profit_center"].astype(str)

    Total.loc[Total["CoCd"] == "AMC1", "Profit_center"] = "100528"

    Total["Company_Code_+_Profit_Ctr"] = Total["CoCd"].str.cat(Total["Profit_center"], sep=":")

    Total = Total.drop('Days', axis = 1)

    #Total["CoCd"] = Total["CoCd"].replace({"B700": 700})

    if generate_csv==True:
        Total.to_csv(path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_Trade_Spend_aged_open_items.csv", index=False)

    return Total


df10 = fct_Trade_Spend_Aged_open_items(generate_csv=True)
print("hello")