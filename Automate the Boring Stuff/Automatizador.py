from pynubank import Nubank
import openpyxl

nu = Nubank("09499570977", "donotwant1")
card_statements = nu.get_card_statements()
wb = openpyxl.load_workbook('nubank1.xlsx')
sheet = wb.get_sheet_by_name('Plan1')
x = 0
y = 1

while x < 30000:
    sheet.cell(row = y, column = 1).value = card_statements[x]['amount']
    x += 1
    y += 1

wb.save('nubank1.xlxs')
