import pandas as pd
from ETL_log import generate_initial_variables_for_ETL_log
from ETL_log import generate_final_variables_for_ETL_log
from ETL_log import ingest_ETL_log_data


folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\Overview Status Phase 1-2-3 Promotion.xlsx"
folder_path2 = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_RAW_DATA\DIM_RAW_DATA\dim_Deadlines.xlsx"
output_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_Overview_Status_Phase_1-2-3_Promotion.csv"

summary_folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\Projects_ETL_log\Projects_ETL_log.xlsx"


def fct_Overview_Status_Phase_123_Promotion(generate_csv, generate_ETL_report):

    table_name, num_input_rows, run_date, start_time, input_size = generate_initial_variables_for_ETL_log(output_path)

    df1 = pd.read_excel(folder_path, sheet_name="Report")

    df1.columns = map(lambda x: x.replace(" ", "_"), df1.columns)

    df1["Month_name"] = pd.DatetimeIndex(df1['Date.1']).month_name()
    df1["Reporting_Month_+_Phase"] = df1["Year"].astype(str) + " " +df1["Month_name"] + ":" + df1["Phase"].astype(str)
    df1 = df1[df1["New_State"] == "Review Level2"]
    df1 = df1[df1["Action"] == "Promote"]

    df2 = pd.read_excel(folder_path2, sheet_name="dim_Deadlines")

    #df1 = df1.merge(df2, left_on='Reporting_Month_+_Phase', right_on='Reporting_Month_+_Phase', how="left")

    df1 = df1.merge(df2[["Reporting_Month_+_Phase",'Deadline']], how = 'left',
        on = 'Reporting_Month_+_Phase')

    if generate_csv == True:
        df1.to_csv(path_or_buf=output_path, index=False)

    dfSummary = generate_final_variables_for_ETL_log(output_path, start_time, num_input_rows, run_date, table_name, input_size)

    if generate_ETL_report== True:

        ingest_ETL_log_data(dfSummary)

    return df1

df10 = fct_Overview_Status_Phase_123_Promotion(generate_csv=True, generate_ETL_report=True)

print("hello")