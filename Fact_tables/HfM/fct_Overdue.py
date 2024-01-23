import pandas as pd
from ETL_log import generate_initial_variables_for_ETL_log
from ETL_log import generate_final_variables_for_ETL_log
from ETL_log import ingest_ETL_log_data




folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\FSSC_Glowdash.xlsx"
output_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_Overdue.csv"

summary_folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\Projects_ETL_log\Projects_ETL_log.xlsx"

def fct_Overdue(generate_csv, generate_ETL_report):

    table_name, num_input_rows, run_date, start_time, input_size = generate_initial_variables_for_ETL_log(output_path)

    df1 = pd.read_excel(folder_path, sheet_name="01.FSSC_Glowdash", skiprows=3)

    naming_dictionary = {"Trade receivables gross amounts: PD 1 week": "Trade_rec_gross_1_week",
                         "Trade receivables gross amounts: PD 2 week": "Trade_rec_gross_2_week",
                         "Trade receivables gross amounts: PD < 30 days": "Trade_rec_gross_<_30",
                         "Trade receivables gross amounts: PD 30 < 90 days": "Trade_rec_gross_<_30_<_90",
                         "Trade receivables gross amounts: PD 90 < 180 days": "Trade_rec_gross_<_90_<_180",
                         "Trade receivables gross amounts: PD > 180 days": "Trade_rec_gross_>_180",
                         "Trade receivables gross amounts" : "Trade_rec_gross",
                         "Unnamed: 1": "CXO_Entity"}

    sum_list_total_overdue_0 = ["Trade_rec_gross_1_week",
                              "Trade_rec_gross_2_week",
                              "Trade_rec_gross_<_30",
                              "Trade_rec_gross_<_30_<_90",
                              "Trade_rec_gross_<_90_<_180",
                              "Trade_rec_gross_>_180"]

    sum_list_total_overdue_15 = ["Trade_rec_gross_<_30",
                              "Trade_rec_gross_<_30_<_90",
                              "Trade_rec_gross_<_90_<_180",
                              "Trade_rec_gross_>_180"]

    sum_list_total_overdue_90 = ["Trade_rec_gross_<_90_<_180",
                              "Trade_rec_gross_>_180"]

    df1.rename(columns= naming_dictionary, inplace=True)

    df1['Total_Overdue_>0'] = df1[sum_list_total_overdue_0].sum(axis=1)
    df1['Total_Overdue_>15'] = df1[sum_list_total_overdue_15].sum(axis=1)
    df1['Total_Overdue_>90'] = df1[sum_list_total_overdue_90].sum(axis=1)

    #df1["CXO_Entity"] = df1["CXO_Entity"].str[2:]

    df1["CXO_Entity"] = df1["CXO_Entity"].str.lstrip()

    #mask = df1["CXO_Entity"] == "BelTrading Sell"

    #df1.loc[mask, "CXO_Entity"] += df1.groupby("CXO_Entity").cumcount().add(1).astype(str)

    df1["CXO_Entity"] = df1["CXO_Entity"].replace({"BelTrading Sell": "BelTrading Sell1.0"})

    if generate_csv == True:
        df1.to_csv(path_or_buf=output_path, index=False)

    dfSummary = generate_final_variables_for_ETL_log(output_path, start_time, num_input_rows, run_date, table_name, input_size)


    if generate_ETL_report== True:

        ingest_ETL_log_data(dfSummary)

    return df1

df10 = fct_Overdue(generate_csv=True,  generate_ETL_report=False)

print("hello")



