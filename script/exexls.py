# __author__ = 'shuai'
# -*- coding: UTF-8 -*-
import os

import xlrd as excel

from base import gl


# filepath = os.path.join(gl.dataPath,'login.xls').decode('utf-8')
# print filepath
# data = excel.open_workbook(filename=filepath)
# table = data.sheet_by_name('login')
# nrows = table.nrows
# ncols = table.ncols
#
# colnamesindex = 0
# colnames = table.row_values(colnamesindex)
# #print colnames
# list= []
# for nr in range(1,nrows):
#     row = table.row_values(nr)
#     if row:
#         app = {}
#         for i in range(len(colnames)):
#             app[colnames[i]] = row[i]
#         list.append(app)
# print list
#
# a = list[0]
# print a
# b = a['username']
# c = a['password']
# print b
# print c



# class TestExcel(object):
#
#     def __init__(self,filepath):
#         self.filepath = filepath
#
#     @property
#     def open(self,filepath,file='login.xls'):
#         try:
#             self.filepath = filepath
#             datafile = excel.open_workbook(filename=self.filepath)
#             return datafile
#         except Exception as ex:
#             print str(ex)
#
#     def getdata(self,colnamesindex):
#         data = excel.open_workbook(filename=filepath)
#         table = data.sheet_by_name('login')
#         nrows = table.nrows
#         ncols = table.ncols
#         colnamesindex = 0
#         colnames = table.row_values(colnamesindex)
#         list = []
#         for nr in range(1, nrows):
#             row = table.row_values(nr)
#             if row:
#                 app = {}
#                 for i in range(len(colnames)):
#                     app[colnames[i]] = row[i]
#                 list.append(app)
#         return list
#
#     @property
#     def texecel(self):
#         self.getdata(self.open)

class TestExcel:
    def __init__(self, filepath, sheetname):
        self.data = excel.open_workbook(filepath)
        self.table = self.data.sheet_by_name(sheetname)
        self.colnames = self.table.row_values(0)
        self.nrows = self.table.nrows
        self.ncols = self.table.ncols

    def getdata(self):
        list = []
        for nr in range(1, self.nrows):
            row = self.table.row_values(nr)
            if row:
                app = {}
                for i in range(len(self.colnames)):
                    app[self.colnames[i]] = row[i]
                list.append(app)
        return list


if __name__ == "__main__":
    filepath = os.path.join(gl.dataPath, 'login.xls').decode('utf-8')
    sheetname = 'login'
    data = TestExcel(filepath, sheetname)
    print data.getdata()
