import pandas as pd
from ETL_log import generate_initial_variables_for_ETL_log
from ETL_log import generate_final_variables_for_ETL_log
from ETL_log import ingest_ETL_log_data


folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\2021 Nov - 2022 Jan_HFM_DataAudit_manual_adj.xlsx"
output_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_DataAudit_log_manual_corrections.csv"


summary_folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\Projects_ETL_log\Projects_ETL_log.xlsx"


def fct_DataAudit_log_manual_corrections(generate_csv,generate_ETL_report):

    table_name, num_input_rows, run_date, start_time, input_size = generate_initial_variables_for_ETL_log(output_path)

    df1 = pd.read_excel(folder_path, sheet_name="DataAudit Log")

    df1 = df1[(df1["Activity"] == "Data Entry")]

    #Finance dimension category.....
    def check_FDM_category(Account):
        #Customer Intercompany Invoice account IC
        if Account == "A50400":
            return "IC"
        #Supplier Intercompany Invoice iC
        elif Account == "L50400":
            return "IC"
        #PL selling, general and administrative(SGA) expenses accounts
        elif Account.startswith("ISCS"):
            return "SG&A Schedule"
        #
        elif Account.startswith("3D"):
            return "3D"
        #Cost of goods sold
        elif Account.startswith("ISMS"):
            return "Cogs Schedule"
        #Income statement
        elif Account.startswith("IS"):
            return "Income Statement"
        #Asset side of the balance sheet
        elif Account.startswith("A"):
            return "Balance_Sheet"
        #Liability side of the balance sheet
        elif Account.startswith("L"):
            return "Balance_Sheet"
        else:
            return "N/A"

    def Financing_group_co(Account):
        #Subsidiary intercompany company cashflow
        if Account == "A60100":
            return "Yes"
        elif Account == "L60100":
            return "Yes"
        else:
            return "No"

    def Deconsolidation(Custom1):
        #Determines movements
        if Custom1 == "DC":
            return "Yes"
        else:
            return "No"

    def FDM_account(row):
        if row["Deconsolidation"] == "Yes":
            return "N/A"
        elif row["Financing_group_co"] == "Yes":
            return "N/A"
        elif row["Movement_schedule"] == "Yes":
            return "Movement Schedules"
        else:
            return row["FDM_category"]

    #Obligatory movement reporting for auditing (starting and closing balance delta manual adjustments)
    def Movement_schedule(row):
        #EOP are the cells that you can not modify manually so we have to exclude because no manual adjustment is possible
        if row["FDM_category"] == "Balance_Sheet" and row["Custom1"] != "EOP":
            return "Yes"
        else:
            return "No"

    df1.loc[df1["Entity"] == "NLD4050_PC100784", "Entity"] = "NLD4050_PC100784B"

    df1["FDM_category"] = df1["Account"].apply(check_FDM_category)
    df1["Financing_group_co"] = df1["Account"].apply(Financing_group_co)
    df1["Deconsolidation"] = df1["Custom1"].apply(Deconsolidation)
    df1["Movement_schedule"] = df1.apply(Movement_schedule, axis=1)
    df1["FDM_account"] = df1.apply(FDM_account, axis=1)

    if generate_csv == True:
        df1.to_csv(path_or_buf=output_path, index= False)

    dfSummary = generate_final_variables_for_ETL_log(output_path, start_time, num_input_rows, run_date, table_name, input_size)

    if generate_ETL_report== True:

        ingest_ETL_log_data(dfSummary)

    return df1

df10 = fct_DataAudit_log_manual_corrections(generate_csv=True, generate_ETL_report=False)
print("hello")
#Custom2 determines brand Custom3 MGA GAAP Custom4 Country