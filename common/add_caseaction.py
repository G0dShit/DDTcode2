from common.excelaction import excelaction
from common.conf import conf

class add_caseaction():
    @staticmethod
    def add_cases():
        #读取配置文件
        result = conf.get_config()
        excelpath=result['Environments'][result['Environments']['env']]['excelpath']
        sheetname = excelaction.get_all_sheets(excelpath)
        test_suite = []
        # 如果配置中设置全量执行
        if result['Run_all']['Whether'] == True:
            for i in range(len(sheetname)):
                sh = sheetname[i]
                # 获取每个sheet行数
                rows,sh1 = excelaction.openexcel(excelpath, sh)
                for j in range(rows-1):
                    #返回单挑测试用例数据
                    testData = excelaction.getexcelparams(excelpath, sh,j+1)
                    test_suite.append(testData)
            return test_suite
        elif result['Run_all']['Whether'] == False:
            for i in (result['Moudle']):
                sheetname = result['Moudle'][str(i)]['sheetname']
                beginrow = result['Moudle'][str(i)]['start']  # 起始执行ID
                # 如果起始ID为空，从第二行执行
                if beginrow == None:
                    beginrow = 2
                endrow = result['Moudle'][str(i)]['end']  # 结束ID
                for j in range(beginrow, endrow + 1):
                    testData = excelaction.getexcelparams(excelpath, sheetname, j-1)
                    test_suite.append(testData)
            return test_suite
        else:
            print('执行模式 Run_all Whether 配置错误只能为true/false')