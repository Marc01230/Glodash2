import pandas as pd
from Trash.dim_ZFM_PCTRI import dim_ZFM_PCTRI
import pandas as pd
from ETL_log import generate_initial_variables_for_ETL_log
from ETL_log import generate_final_variables_for_ETL_log
from ETL_log import ingest_ETL_log_data

folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\GLOBAL_IC_MATCHING_REPORT.xlsx"

output_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_Global_IC_matching_report.csv"

summary_folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\Projects_ETL_log\Projects_ETL_log.xlsx"


def fct_Global_IC_matching_report(generate_csv,generate_ETL_report):

    table_name, num_input_rows, run_date, start_time, input_size = generate_initial_variables_for_ETL_log(output_path)

    df1 = pd.read_excel(folder_path, sheet_name="Nisa", skiprows=13)
    df1.columns = map(lambda x: x.replace(" ", "_"), df1.columns)

    df1 = df1.drop(index=0)

    df2 = dim_ZFM_PCTRI(generate_csv=False)

    df1 = df1.loc[df1["Entity"] != "Grand Total"]

    df1 = df1.merge(df2[["HFM_Entity_Label", "FSSC_Description"]], how = 'left', left_on="Entity", right_on="HFM_Entity_Label")

    df1 = df1.rename(columns= {"FSSC_Description": "FSSC_Merged_on_Entity"})

    df1 = df1.merge(df2[["HFM_Entity_Label", "FSSC_Description"]], how = "left", left_on = "Partner", right_on = "HFM_Entity_Label")

    df1 = df1.rename(columns= {"FSSC_Description" : "FSSC_Merged_on_Partner"})

    df1 = df1.drop(columns=["HFM_Entity_Label_x", "HFM_Entity_Label_y"])

    df1.loc[(df1["FSSC_Merged_on_Entity"] == "FSSC NL") | (df1["FSSC_Merged_on_Partner"] == "FSSC NL"), "FSSC_NL"] = 1

    df1.loc[(df1["FSSC_Merged_on_Entity"] == "FSSC EMEA") | (df1["FSSC_Merged_on_Partner"] == "FSSC EMEA"), "FSSC_EMEA"] = 1

    df1.loc[(df1["FSSC_Merged_on_Entity"] == "FSSC ASIA") | (df1["FSSC_Merged_on_Partner"] == "FSSC ASIA"), "FSSC_ASIA"] = 1

    dfSummary = generate_final_variables_for_ETL_log(output_path, start_time, num_input_rows, run_date, table_name, input_size)

    if generate_csv==True:
        df1.to_csv(path_or_buf=output_path, index=False)

    if generate_ETL_report== True:

        ingest_ETL_log_data(dfSummary)

    return df1


df10=fct_Global_IC_matching_report(generate_csv=True, generate_ETL_report=True)
print("hello")
