import json

# 响应数据校验
class checkdataaction():
    @staticmethod
    def checkdata(data, res):
        descontentreplace = data['预期结果'].replace("\n", "").replace(" ", "").replace("\t", "").replace("\r", "").encode(
            "utf-8")  # 预期结果
        ignorefields = data['忽略字段检查']  # 忽略字段
        print(u'请求参数为:' + str(data['入参']))
        resd = res.content.decode("utf-8")  # 实际响应结果
        if res.status_code != 200:
            print(u"请求失败,statuscode非200，实际响应code为 " + str(res.status_code))
            raise AssertionError
        #去掉实际响应结果特殊符号
        resreplace = resd.replace(" ", "").replace("\n", "").replace("\t", "").replace("\r", "").encode("utf-8")
        ignorefieldsl = ignorefields.split(',')
        if ignorefields:
            try:
                dictdescontent = json.loads(descontentreplace)
                for i in range(len(ignorefieldsl)):
                    dictdescontent.pop(ignorefieldsl[i])
                descontent = json.dumps(dictdescontent, ensure_ascii=False)
            except:
                print(u'预期结果非json格式或预期结果中不包含忽略字段')
                raise RuntimeError
            print(u'忽略校验字段为:' + str(ignorefields))
            resreplacel = json.loads(resreplace)
            for i in range(len(ignorefieldsl)):
                if ignorefieldsl[i] not in json.loads(res.text):  # 判断忽略字段是否被包含
                    print(u"返回内容中无忽略字段,实际返回为" + res.text)
                    raise RuntimeError
                else:
                    resreplacel.pop(ignorefieldsl[i])
            resreplace2 = json.dumps(resreplacel, ensure_ascii=False)
        else:
            print(u'无忽略校验字段')
            descontent = descontentreplace
            resreplace2 = resreplace
        if descontent in resreplace2:
            print(u"接口断言通过")
        else:
            print(u"实际响应数据为:" + resreplace.decode())
            print(u"接口断言与期望不符,执行失败")
            print(u"预期响应结果为:" + descontentreplace.decode())
            raise AssertionError