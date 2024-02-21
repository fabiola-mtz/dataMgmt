import os
import pandas as pd

# Class: Removes specified columns from multiple CSV files 
class removeSpecifiedCols:

    # constructor
    def __init__(self, CSVpath, saveCSVpath):
        self.CSVpath = CSVpath
        self.saveCSVpath = saveCSVpath
                
    def removecols(self):
        ext = ('.csv')
        # Lists all files with, concatenating its given CSVpath
        for filename in os.listdir(self.CSVpath):
            f = os.path.join(self.CSVpath, filename)
            # selects only .csv files from list
            if f.endswith(ext):
                head_tail = os.path.split(f) 
                head_tail1 = 'C:/Users/HP/Desktop/Remove_Columns_Python/Output' 
                k = head_tail[1] 
                r = k.split(".")[0]
            
                p = head_tail1 + "/" + r + " - Output.csv" 

                mydata = pd.read_csv(f, encoding = 'latin1')
                
                new = mydata[["Field_1","Field_5","Field_30","Field_33","Field_40","Field_44","Field_61"]]
                new.to_csv(p ,index=False)

# leer CSVpath y ext
#p = removeSpecifiedCols('C:/Users/HP/Desktop/Remove_Columns_Python/Output')


