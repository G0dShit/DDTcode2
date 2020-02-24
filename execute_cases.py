from common.requestaction import requestsaction
from common.checkdataaction import checkdataaction
from common.checkdbaction import checkdbaction
from common.conf import conf
from common.add_caseaction import add_caseaction
from common.sendemail import send
import unittest,ddt

#获取dtt需要执行用例
testData=add_caseaction.add_cases()

#执行测试用例
@ddt.ddt
class excute_cases(unittest.TestCase):
    #@threads(5)
    @ddt.data(*testData)
    def test_one_case(self,data):
        result = conf.get_config()
        url = result['Environments']['test']['url']
        #发起请求获取实际响应结果
        res=requestsaction.excute_case(url, data)
        #进行数据校验
        checkdataaction.checkdata(data, res)
        # 数据库断言方法
        checkdbaction.checkdb(data)

    #send()