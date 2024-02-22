import os
import sys
import glob
import pandas as pd

# Class: Removes specified columns from multiple CSV files 
class removeSpecifiedCols:

    def create_path(self, filename):
        filenameNoExt = filename.split(".")[0]
        save_path = self.saveCSVpath + "/" + filenameNoExt + " - Output.csv" 
        return save_path
                
    def select_cols(self):
        os.chdir(self.CSVpath)
        list_csv_files = glob.glob('*.{}'.format('csv'))
        """ Put try catch block for no existing files """
        for filename in list_csv_files:
            save_path = self.create_path(filename)
            f = os.path.join(self.CSVpath, filename)
            csv_read_data = pd.read_csv(f, encoding = 'latin1', usecols = ['User ID'])
            csv_read_data.to_csv(save_path, index = False)   

            #new = csv_data[["Field_1","Field_5","Field_30","Field_33","Field_40","Field_44","Field_61"]]
            #new.to_csv(save_path, index = False)   

    # constructor
    def __init__(self, CSVpath, saveCSVpath):
        self.CSVpath = CSVpath
        self.saveCSVpath = saveCSVpath   


findCSV = 'C:/Users/I746992/OneDrive - SAP SE/General - Data Intelligence LAC/1. Mexico/2. Target List/3. Target Lists - Reports/7. Listados - 2024/Q2 - 2024/Rodrigo Lecanda'
saveCSV = 'C:/Users/I746992/Desktop/Remove_Columns_Python/Output' 
remove = removeSpecifiedCols(findCSV, saveCSV)
remove.select_cols()

