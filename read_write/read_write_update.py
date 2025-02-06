#text file

# with open("textfile.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("textfile.txt", "w") as file:
#     file.write("Written text")

# with open("textfile.txt", "a") as file:
#     file.write("Appended text")


#csv file
# import csv

# with open("csvfile.csv", "r") as csvfile:
#     content = csv.reader(csvfile)
#     for row in content:
#         print(row)
        
# with open("csvfile.csv", "w") as csvfile:
#     content = csv.writer(csvfile)
#     content.writerow(["Baman","24","22-03-2002"])

# with open("csvfile.csv","a") as csvfile:
#     content = csv.writer(csvfile)
#     content.writerow(["Chaman","25","30-07-2003"])


#excel
## not working for excel
import pandas as pd
from openpyxl import Workbook

wb = Workbook()  
sheet = wb.active  

sheet['A1'] = "Naman"  
sheet['A2'] = 24  
sheet['A3'] = "10-10-2002"  

wb.save(filename="excel.xlsx")