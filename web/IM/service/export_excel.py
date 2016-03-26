'''
Created on Sep 28, 2015
Use xlwt to write an excel one by one.
@author: wuw7
'''
import xlwt

class Writer():
    @staticmethod
    def export_excel(data, file_path):
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('sheet1')
        r_index = 0
        c_index = 0
        for row in data:
            for col in row:
                sheet.write(r_index, c_index, col)
                c_index += 1
            r_index += 1
            c_index = 0
        workbook.save(file_path)
        
#writer = Writer()
#data = [[0,1,2], [0,1,2],[0,1,2], [0,1,2,3]]
#file_path = 'sheeet.xlsx'
#writer.export_excel(data, file_path)
