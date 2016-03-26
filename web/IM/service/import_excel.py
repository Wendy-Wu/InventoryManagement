'''
Created on Sep 27, 2015
Use xlrd to read excel(only one sheet) one by one, add the data into database
@author: wuw7
'''
import xlrd
from dao.InvDao import InvDao
from model.Inventory import Inventory

class Parser():
    
    @staticmethod
    def parse_by_row(datafile):
        workbook = xlrd.open_workbook(datafile)
        sheet = workbook.sheet_by_index(0)
        inv_args = []
        for row in range(sheet.nrows):
            for col in range(sheet.ncols):
                inv_args.append(sheet.cell_value(row, col))
            print inv_args   
            print InvDao.add_inventory(inv_args[0], inv_args[1], inv_args[2], inv_args[3], inv_args[4], inv_args[5], inv_args[6], inv_args[7])
            inv_args=[]
