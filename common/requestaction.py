import requests,json


class requestsaction():
        @staticmethod
        #发起请求
        def excute_case(domain, data, **kwargs):
            print(u'用例名称: ' + data['用例名称'])
            do = data['接口地址（名称）'] #方法名
            method = data['方法'] #请求方式
            payload = data['入参'].encode("utf-8") #请求参数
            if 'params' in kwargs:
                payload = payload  + '&' +  kwargs['params']
            if 'headers' in kwargs:
                headers_t = kwargs['headers']
                print(u"自定义请求头为"+headers_t)
                headers_t=headers_t.replace("'", "\"")
                headers=json.loads(headers_t)
            else:
                headers={'Content-type':'application/x-www-form-urlencoded'}
            if domain[-1] != '/' and do[0] !='/':
                host=domain + '/' + do
            else :
                host=domain+do
            session = requests.session()
            if method.upper() == 'GET':
                res=session.request('GET',host,params=payload,headers=headers,timeout=8)
                return res
            elif method.upper() == 'POST':
                res=session.request('POST',host, data=payload, headers=headers,timeout=8)
                return res
            else:
                print(u'请求方式错误，只能为get/post,现为' + method.upper())
                raise AssertionError
