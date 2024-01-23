from Fact_tables.HfM.fct_Overview_Status_Phase_123_Promotion import fct_Overview_Status_Phase_123_Promotion
from Fact_tables.User_excel_files.fct_FTE_Data import fct_FTE_Template
from Fact_tables.HfM.fct_Overdue import fct_Overdue
from Dimension_tables.dim_Global_Overview import dim_Global_Overview
from Dimension_tables.dim_Deadlines import dim_Deadlines
from Fact_tables.Celonis.fct_Blocked_sales_orders import fct_Blocked_sales_orders
from Dimension_tables.dim_FSSCs import dim_FSSC
from Dimension_tables.HfM.dim_HFM_Metadata import dim_HFM_Metadata
from Trash.dim_ZFM_PCTRI import dim_ZFM_PCTRI
from Dimension_tables.SAP.dim_Company_Codes import dim_Company_Codes
from Fact_tables.Celonis.fct_Active_Customers import fct_Active_customer
from Fact_tables.SAP.fct_Trade_spend_open_items_via_vendor import fct_Trade_spend_open_items_via_vendor
from Fact_tables.SAP.fct_Trade_Spend_aged_open_items import fct_Trade_Spend_Aged_open_items
from Fact_tables.HfM.fct_Global_IC_matching_report import fct_Global_IC_matching_report
from Fact_tables.HfM.fct_DataAudit_log_manual_corrections import fct_DataAudit_log_manual_corrections
from Fact_tables.User_excel_files.fct_Global_BS_submission_track import fct_Global_BS_submission_track
from Fact_tables.SAP.fct_Total_MJE import fct_Total_MJE
from Fact_tables.SAP.fct_MJE_WK2 import fct_MJE_WK2
from Fact_tables.User_excel_files.fct_Targets_for_FSSCs import fct_Targets_for_FSSCs
from Fact_tables.SAP.fct_BS_Open_Items_greater_than_6_months import fct_BS_Open_items_greater_than_6_months
from Fact_tables.User_excel_files.fct_ICF_masterfile import fct_ICF_masterfile
from Dimension_tables.dim_Company_Codes2 import dim_Company_Codes_new
from Dimension_tables.dim_GL_Account_ownership import dim_GL_framework

def generate_SAP_AFO_based_fact_tables():

    fct_Active_customer(generate_csv=True)

    fct_BS_Open_items_greater_than_6_months(generate_csv=True)

    fct_Overview_Status_Phase_123_Promotion(generate_csv=True)

    fct_Total_MJE(generate_csv=True)

    fct_MJE_WK2(generate_csv=True)

    fct_Trade_Spend_Aged_open_items(generate_csv=True)

    fct_Trade_spend_open_items_via_vendor(generate_csv=True)

def generate_CXO_HfM_based_Fact_Tables():

    #Robot:
    fct_Overdue(generate_csv=False, generate_ETL_report=True)

    fct_Overview_Status_Phase_123_Promotion(generate_csv=False, generate_ETL_report=True)

    #Robot:
    fct_Global_IC_matching_report(generate_csv=False, generate_ETL_report=True)

    fct_DataAudit_log_manual_corrections(generate_csv=False, generate_ETL_report=True)

def generate_Celonis_based_fact_tables():

    fct_Blocked_sales_orders(generate_csv=True)

def generate_user_based_fact_tables():

    fct_FTE_Template(generate_csv=True)

    fct_Global_BS_submission_track(generate_csv=True)

    fct_Targets_for_FSSCs(generate_csv=True)

    fct_ICF_masterfile(generate_csv=True)

def generate_SAP_based_dimension_tables():
    dim_ZFM_PCTRI(generate_csv=True)

    dim_Company_Codes(generate_csv=True)

def generate_HfM_based_dimenstion_tables():

    dim_HFM_Metadata(generate_csv=True)

def generate_user_based_dimension_tables():

    dim_Global_Overview(generate_csv=True)

    dim_Deadlines(generate_csv=True)

    dim_FSSC(generate_csv=True)


#dim_GL_framework(generate_csv=True)

#dim_FSSC(generate_csv=True)

#fct_Overdue(generate_csv=True, generate_ETL_report=True)

#dim_Company_Codes_new(generate_csv=True)

#fct_Global_IC_matching_report(generate_csv=True, generate_ETL_report=True)

#dim_HFM_Metadata(generate_csv=True)

#dim_ZFM_PCTRI(generate_csv=True)

#fct_FTE_Template(generate_csv=True)

fct_Trade_Spend_Aged_open_items(generate_csv=True)

#fct_DataAudit_log_manual_corrections(generate_csv=True, generate_ETL_report=True)

#fct_Overview_Status_Phase_123_Promotion(generate_csv=True, generate_ETL_report=True)

#fct_Global_BS_submission_track(generate_csv=True)

#fct_Trade_spend_open_items_via_vendor(generate_csv=True)

#fct_BS_Open_items_greater_than_6_months(generate_csv=True)

#fct_Blocked_sales_orders(generate_csv=True)

#dim_Global_Overview(generate_csv=True)

#fct_Total_MJE(generate_csv=True)

#fct_MJE_WK2(generate_csv=True)

#fct_Overdue(generate_csv=False,generate_ETL_report=True)

#fct_Overview_Status_Phase_123_Promotion(generate_csv=True)

#dim_ZFM_PCTRI(generate_csv=True)









