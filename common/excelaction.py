import xlrd

class excelaction():
    @staticmethod
    def get_all_sheets(excelurl):
        try:
            bk = xlrd.open_workbook(excelurl)
            return bk.sheet_names()
        except:
            print("no excel in %s" % (excelurl))
            exit()

    # 打开excel
    @staticmethod
    def openexcel(excelurl, sheetname):
        try:
            bk = xlrd.open_workbook(excelurl)
        except:
            print("no excel in %s" % (excelurl))
            exit()
        try:
            sh = bk.sheet_by_name(sheetname)
            return sh.nrows,sh
        except:
            print("no sheet in %s named %s" % (excelurl, sheetname))
            exit()

    #读取excel参数
    @staticmethod
    def getexcelparams(exceldir, sheetname,num):
        rows,sh =excelaction.openexcel(exceldir, sheetname)
        if int(num) >= int(rows):
            print(u"所选列超出最大行")
            exit()
        try:
            keys = sh.row_values(0)
            #row_data = sh.row_values(int(beginnum))
            values = sh.row_values(num)
            # keys，values这两个列表一一对应来组合转换为字典
            api_dict = dict(zip(keys, values))
            #listApiData.append(api_dict)
            return api_dict
        except:
            print(u"所选列没有数据")
            exit()