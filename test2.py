import pandas as pd
from dateutil.relativedelta import relativedelta


source_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_BS_Open_items.csv"
destination_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_BS_Open_items.csv"

def fct_BS_Open_items_greater_than_6_months(generate_csv):

    df1 = pd.read_csv(source_path)

    if generate_csv == True:
        df1.to_csv(destination_path, index=False)


fct_BS_Open_items_greater_than_6_months(generate_csv=False)