import pandas as pd


folder_path = r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\FTM RTR & AR 001 FSSC Performance Dashboard\ICF Masterfile.csv"


def fct_ICF_masterfile(generate_csv):
    df1 = pd.read_csv(folder_path, sep=",")

    df1.columns = map(lambda x: x.replace(" ", "_"), df1.columns)

    #df1 = df1[df1["ICF_Entity_Name_(GRC)"].str.contains("SSC_FSSC")]

    #df1["FSSC_Entity"] = df1["ICF_Entity_Name_(GRC)"].apply(lambda x: "FSSC NL" if "FSSC NL" in x else ("FSSC EMEA" if "FSSC EMEA" in x else ("FSSC ASIA" if "FSSC ASIA" in x else "check")))

    if generate_csv == True:
        df1.to_csv(path_or_buf=r"C:\Users\kemenm02\FrieslandCampina\SSC Process Innovation & Excellence - Analytics public\Power BI\Workspace documentation Project & Innovations - SSC\GLODASH_DATA\FCT_DATA\fct_ICF_masterfile.csv", index=False, mode='a', sep=";")

    return df1


df10 = fct_ICF_masterfile(generate_csv=True)
#print("hello")itsme