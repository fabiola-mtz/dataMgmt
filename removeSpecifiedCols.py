import os
import pandas as pd

# Class: Removes specified columns from multiple CSV files 
class removeSpecifiedCols:

    # constructor
    def __init__(self, CSVpath, saveCSVpath):
        self.CSVpath = CSVpath
        self.saveCSVpath = saveCSVpath
    
    def create_path(self, ext):
        # Lists all files within given path
        for filename in os.listdir(self.CSVpath):
            # Concatenate in 'f' its given CSVpath
            f = os.path.join(self.CSVpath, filename)
            # selects only .csv files from list
            if f.endswith(ext):
                # splits current path into a tuple [head, tail]
                head_tail = os.path.split(f) 
                # tail is the last pathname component a.k.a the name of the file (with ext)
                tail = head_tail[1]                 
                # name of the file whithout the ext (i.e. from 'data.csv', splits (data, csv), then take the name (data))
                filenameNoExt = tail.split(".")[0]
                # p: propose new path and name for the file
                save_path = self.saveCSVpath + "/" + filenameNoExt + " - Output.csv" 
                return [f, save_path]
                
    def select_cols(self):
        # create path
        f, save_path = self.create_path(self, '.csv')
        csv_data = pd.read_csv(f, encoding = 'latin1')
        # selects needed columns and create new csv
        new = csv_data[["Field_1","Field_5","Field_30","Field_33","Field_40","Field_44","Field_61"]]
        new.to_csv(save_path, index = False)            
                

# run code
# 1.- Open bash
# 2.- Type "py removespecifiedCols.py [findCSV] [saveCSV]" 
# where [findCSV] is the path where CSV files can be found (place where saved)
# and [saveCSV] is the path where new CSV files are going to be saved                          
findCSV = 'C:\Users\I746992\OneDrive - SAP SE\General - Data Intelligence LAC\1. Mexico\2. Target List\3. Target Lists - Reports\7. Listados - 2024\Q2 - 2024\Rodrigo Lecanda'
saveCSV = 'C:/Users/HP/Desktop/Remove_Columns_Python/Output' 
remove = removeSpecifiedCols(findCSV, saveCSV)

