import pandas as pd


folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\MJE after wk2.xlsx"

sum_column_list = ["Transaction Code 1","Transaction Code 2", "Transaction Code 3", "Transaction Code 4", "Transaction Code 5", "Transaction Code 6"
                   , "Transaction Code 7", "Transaction Code 8", "Transaction Code 9", "Transaction Code 10", "Transaction Code 11", "Transaction Code 12", "Transaction Code 13"
                   , "Transaction Code 14", "Transaction Code 15", "Transaction Code 16", "Transaction Code 17", "Transaction Code 18", "Transaction Code 19", "Transaction Code 20"
                   , "Transaction Code 21", "Transaction Code 22", "Transaction Code 23", "Transaction Code 24", "Transaction Code 25"]


def fct_MJE_WK2(generate_csv):
    df1 = pd.read_excel(folder_path, sheet_name="MJE > WK2")

    df1[sum_column_list] = df1[sum_column_list].fillna(0)

    df1[sum_column_list] = df1[sum_column_list].astype(int)

    df1 ["Sum_of_transaction_codes"] = df1[sum_column_list].sum(axis=1)

    if generate_csv==True:
        df1.to_csv(path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_MJE_WK2.csv", index=False)

    return df1

df10 = fct_MJE_WK2(generate_csv=True)
print("hello")