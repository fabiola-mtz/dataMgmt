import os
import sys
import glob
import pandas as pd

# Class: Removes specified columns from multiple CSV files 
class removeSpecifiedCols:

    # constructor
    def __init__(self, CSVpath, saveCSVpath):
        self.CSVpath = CSVpath
        self.saveCSVpath = saveCSVpath
    
    def create_path(self, ext):
        # selects only .csv files from files in path
        os.chdir(self.saveCSVpath)
        list_csv_files = glob.glob('*.{}'.format(ext))
        for filename in list_csv_files:
            # Get complete path to access file
            f = os.path.join(self.CSVpath, filename)
            # splits current path into a tuple [head, tail]
            #head_tail = os.path.split(f) 
            # tail is the last pathname component a.k.a the name of the file (with ext)
            #tail = head_tail[1]                 
            # name of the file whithout the ext (i.e. from 'data.csv', splits (data, csv), then take the name (data))
            filenameNoExt = filename.split(".")[0]
            # p: propose new path and name for the file
            save_path = self.saveCSVpath + "/" + filenameNoExt + " - Output.csv" 
            return [f, save_path]
                
    def select_cols(self):
        # create path
        f, save_path = self.create_path(self, '.csv')
        csv_read_data = pd.read_csv(f, encoding = 'latin1', usecols = ['ID', 'INDUSTRY (see Industry List)'])
        csv_read_data.to_csv(save_path, index = False)        
        #csv_data = pd.read_csv(f, encoding = 'latin1')
        # selects needed columns and create new csv
        #new = csv_data[["Field_1","Field_5","Field_30","Field_33","Field_40","Field_44","Field_61"]]
        #new.to_csv(save_path, index = False)            
                

# run code
# 1.- Open bash
# 2.- Type "py removespecifiedCols.py [findCSV] [saveCSV]" 
# where [findCSV] is the path where CSV files can be found (place where saved)
# and [saveCSV] is the path where new CSV files are going to be saved    
#remove = removeSpecifiedCols(sys.argv[1], sys.argv[2]) 
#remove.select_cols()

# OR                          
findCSV = 'C:\Users\I746992\OneDrive - SAP SE\General - Data Intelligence LAC\1. Mexico\2. Target List\3. Target Lists - Reports\7. Listados - 2024\Q2 - 2024\Rodrigo Lecanda'
saveCSV = 'C:\Users\I746992\Desktop\Remove_Columns_Python\Output' 
removeSpecifiedCols(findCSV, saveCSV)
removeSpecifiedCols.select_cols()

