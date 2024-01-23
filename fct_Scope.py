import pandas as pd
import datetime
from Dimension_tables.dim_Global_Overview import dim_Global_Overview
import os


folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\DIM_DATA\dim_Global_FSSC_Overview.csv"


def Scope_data(generate_csv):

    df1 = dim_Global_Overview(generate_csv=False)

    df1['Timestamp'] = pd.to_datetime(datetime.datetime.now())

    df1['Timestamp'] = df1['Timestamp'].dt.strftime('%Y-%m-%d')

    if generate_csv == True:
        df1.to_csv(path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\SCOPE_DATA\fct_Scope.csv", sep='|', index=False, mode='a', header=False)

    return df1
