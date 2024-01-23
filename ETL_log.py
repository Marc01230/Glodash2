import pandas as pd
import time
import csv
import datetime
import os
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows


summary_folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\Projects_ETL_log\Projects_ETL_log.xlsx"

def generate_initial_variables_for_ETL_log(path):

    table_name = os.path.splitext(os.path.basename(path))[0]
    input_size = os.path.getsize(path)

    with open(path, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        num_input_rows = len(list(reader))

    run_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    start_time = time.monotonic()

    return table_name, num_input_rows, run_date, start_time, input_size

def generate_final_variables_for_ETL_log (output_path, start_time, num_input_rows, run_date, table_name, input_size):
    end_time = time.monotonic()
    output_size = os.path.getsize(output_path)
    ETL_duration = round((end_time - start_time) / 60, 4)

    with open(output_path, encoding="utf-8") as csvfile2:
        reader2 = csv.reader(csvfile2)
        num_output_rows = len(list(reader2))

    num_of_new_records = num_output_rows - num_input_rows
    Data_Load_Size = (output_size-input_size)/(1024 * 1024)

    dfSummary = pd.DataFrame({"Run_Date": [run_date],
                              "Project_name": "Glodash",
                              "Table_name": [table_name],
                              "Num_of_new_records": [num_of_new_records],
                              "ETL_duration": [ETL_duration],
                              "Data_Load_Size_(MB)" : [Data_Load_Size]})

    return dfSummary

def ingest_ETL_log_data(dfSummary):
    wb = openpyxl.load_workbook(summary_folder_path)
    ws = wb.active

    for r in dataframe_to_rows(dfSummary, index=False, header=False):
        ws.append(r)

    wb.save(summary_folder_path)