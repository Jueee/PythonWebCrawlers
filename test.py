import xlwt 
wbk = xlwt.Workbook(encoding = 'gbk')
sheet = wbk.add_sheet('sheet 1')
print(help(sheet.write))