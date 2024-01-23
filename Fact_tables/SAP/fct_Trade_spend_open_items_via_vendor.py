import numpy as np
import pandas as pd
import datetime


folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\Trade Spend AR.xlsx"
folder_path2 = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\TS Asia.xlsx"

def fct_Trade_spend_open_items_via_vendor(generate_csv):

    df3330 = pd.read_excel(folder_path, sheet_name="3330")
    df3330.columns = map(lambda x: x.replace(" ", "_"), df3330.columns)

    df3820 = pd.read_excel(folder_path, sheet_name="3820")
    df3820.columns = map(lambda x: x.replace(" ", "_"), df3820.columns)
    column_order_3820 = ["Date", "CoCd", "Doc._Date", "Profit_Ctr", "Pstng_Date", "Amount_in_local_cur.",
                         "End_of_Month"]
    df3820 = df3820.reindex(columns=column_order_3820)

    df3650 = pd.read_excel(folder_path, sheet_name="3650")
    df3650.columns = map(lambda x: x.replace(" ", "_"), df3650.columns)
    column_order_3650 = ["Date", "CoCd", "Doc._Date", "Profit_Ctr", "Pstng_Date", "Amount_in_local_cur.",
                         "End_of_Month"]
    df3650 = df3650.reindex(columns=column_order_3650)

    dfTS_Asia = pd.read_excel(folder_path2, sheet_name="Template")
    dfTS_Asia.columns = map(lambda x: x.replace(" ", "_"), dfTS_Asia.columns)

    dfTS_Asia = dfTS_Asia.rename(columns={"Profit_center": "Profit_Ctr", "End_of_month": "End_of_Month"})

    column_order_TS_Asia = ["Date", "CoCd", "Doc._Date", "Profit_Ctr", "Pstng_Date", "Amount_in_local_cur.",
                         "End_of_Month", "Trade_Spend_check"]

    dfTS_Asia = dfTS_Asia.reindex(columns=column_order_TS_Asia)


    df2 = pd.read_excel(folder_path, sheet_name="TS vendor rel list")
    df2.columns = map(lambda x: x.replace(" ", "_"), df2.columns)

    #df3330 = df3330.merge(df2[["Vendor"]], how='left', left_on='Account', right_on="Vendor").dropna()

    df3330 = df3330.merge(df2[["Vendor"]], how='inner', left_on='Account', right_on="Vendor")

    df3330 = df3330.rename(columns={"CoCode": "CoCd", "Amt_in_loc.cur.": "Amount_in_local_cur."})

    column_order_3330 = ["Date", "CoCd", "Doc._Date","Profit_Ctr", "Pstng_Date", "Amount_in_local_cur.", "End_of_Month"]

    df3330 = df3330.reindex(columns=column_order_3330)

    Total = pd.concat([df3330, df3650, df3820, dfTS_Asia], ignore_index=True)

    Total["Trade_Spend_check"] = Total["Trade_Spend_check"].fillna("AR")

    #Total[Total["Trade_Spend_check"] == 0, "Trade_Spend_check"] = "AR"

    def get_aging_bucket(row):
        diff = abs(row["End_of_Month"]-row["Pstng_Date"]).days
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

    Total["Aging_Bucket"] = Total.apply(get_aging_bucket, axis=1)

    Total["CoCd"] = Total["CoCd"].astype(str)

    Total["Profit_Ctr"] = Total["Profit_Ctr"].astype(str)

    Total["Company_Code_+_Profit_Ctr"] = Total["CoCd"].str.cat(Total["Profit_Ctr"], sep=":")

    if generate_csv==True:
        Total.to_csv(path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_Trade_spend_open_items_via_vendor.csv", index=False)

    return Total

df10 = fct_Trade_spend_open_items_via_vendor(generate_csv=True)
print("hello")