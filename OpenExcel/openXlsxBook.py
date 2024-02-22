import pandas as pd

save_path = "C:/Users/I746992/Desktop/Remove_Columns_Python/"
# read sheet of an excel file
file = "C:/Users/I746992/OneDrive - SAP SE/General - Data Intelligence LAC/1. Mexico/2. Target List/3. Target Lists - Reports/MasterFile- MX.xlsx"
#file = "C:/Users/I746992/OneDrive - SAP SE/General - Data Intelligence LAC/LOB-PE_ID-PE_name.xlsx"
df = pd.read_excel(file, sheet_name="Efectivas") 
df.to_pickle(save_path + "dummyEfectivas.pkl", compression='zip')
#df.to_excel(save_path + "efectivas.xlsx", index = False)
# print(dataframe1)