# new workbook, write data, save

from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "world!"

workbook.save(filename="hello_world.xlsx")

# new sheet
ws1 = wb.create_sheet("Mysheet") # insert at the end (default)
ws2 = wb.create_sheet("Mysheet", 0) # insert at first position
ws3 = wb.create_sheet("Mysheet", -1) # insert at the penultimate position

# properties: title, tabcolor
ws.title = "New Title"
ws.sheet_properties.tabColor = "1072BA"

get it as a key of the workbook:
ws3 = wb["New Title"]

# first sheet, sheet index
from openpyxl import load_workbook
wb = load_workbook("./hello.xlsx")
ws = wb[wb.sheetnames[0]]
