import pandas as pd
from dateutil.relativedelta import relativedelta
from pandas.tseries.offsets import MonthEnd


source_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_RAW_DATA\FCT_RAW_DATA\SAP_RAW\fct_BS_Open_Items_RAW.csv"
destination_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_BS_Open_items.csv"

rates_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\DIM_DATA\dim_Rates.csv"

float_list = ['CCode_Curr_Value', 'Value_in_EUR']

def fct_BS_Open_items_greater_than_6_months(generate_csv):

    df1 = pd.read_csv(source_path, sep=",")

    df_rates = pd.read_csv(rates_path, sep=";")

    df_rates["Exchange_rate"] = df_rates["Exchange_rate"].astype(float)

    exchange_rate_dict = dict(zip(df_rates["Currency_code"], df_rates["Exchange_rate"]))

    df1.columns = map(lambda x: x.replace(" ", "_"), df1.columns)

    #df1['CCode_Curr_Value'] = df1['CCode_Curr_Value'].str.replace(',', '')
    df1['Company_Code_Currency_Value'] = df1['Company_Code_Currency_Value'].astype(float)

    df1 = df1.rename(columns={"Company_Code_Currency_Value": "CCode_Curr_Value", "Fiscal_Yr": "Year", 'DB_Rows': 'Database_Rows'})

    df1['Profit_Ctr'] = df1['Profit_Ctr'].fillna(0)

    df1['Profit_Ctr'] = df1['Profit_Ctr'].astype(int)

    df1['Company_Code_+_Profit_Ctr'] = df1['CoCode'].astype(str) + ":" + df1['Profit_Ctr'].astype(str)

    df1['Value_in_EUR'] = df1["CCode_Curr_Value"]*df1['CCodeCurr'].map(exchange_rate_dict)

    df1[float_list] = df1[float_list].round(decimals = 2)

    df1.loc[df1['Period'] == 13, 'Year'] += 1
    df1.loc[df1['Period'] == 13, 'Period'] = 1

    df1.loc[df1['Period'] == 14, 'Year'] += 1
    df1.loc[df1['Period'] == 14, 'Period'] = 2

    df1.loc[df1['Period'] == 15, 'Year'] += 1
    df1.loc[df1['Period'] == 15, 'Period'] = 3

    df1.loc[df1['Period'] == 16, 'Year'] += 1
    df1.loc[df1['Period'] == 16, 'Period'] = 4


    df1["Open_item_date"] = "01" + "/" + df1["Period"].astype(str) + "/" + df1["Year"].astype(str)

    df1["Open_item_date"] = pd.to_datetime(df1["Open_item_date"], format="%d/%m/%Y")

    df1["Open_item_date"] = pd.to_datetime(df1["Open_item_date"])

    current_date = pd.Timestamp.now().date()
    last_day_previous_month = (current_date.replace(day=1) - pd.offsets.MonthEnd(1)).date()
    #df1["Download_date"] = last_day_previous_month
    df1["Download_date"] = pd.to_datetime(df1["Download_date"])

    df1["Aging_months"] = (df1['Download_date'] - df1['Open_item_date']).dt.days.astype(int)/30
    df1['Aging_months'] = df1['Aging_months'].round()

    df1.loc[df1["Company_Code_+_Profit_Ctr"] == "4050:100784", "Company_Code_+_Profit_Ctr"] = "4050:100784B"

    #df1["Aging_months"] = (df1['Download_date'] - df1['Open_item_date'])

    #df1["Aging_months"] = df1["Aging_months"].astype(int)

    def get_aging_bucket(row):
        diff = abs(row["Download_date"] - row["Open_item_date"]).months
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

    column_order = ['CoCode', 'Profit_Ctr', 'Year', 'Period', 'G/L', 'Database_Rows', 'CCode_Curr_Value', 'CCodeCurr', 'Download_date', 'Company_Code_+_Profit_Ctr', 'Value_in_EUR', 'Open_item_date', 'Aging_months']

    df1 = df1.reindex(columns=column_order)

    if generate_csv == True:
        df1.to_csv(destination_path, mode="a", index=False, header=False)

    return df1

df10 = fct_BS_Open_items_greater_than_6_months(generate_csv=False)

print("Hello")