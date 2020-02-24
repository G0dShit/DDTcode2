import pymysql


class checkdbaction():

    def _todict(self, db):
        try:
            redb=eval('dict(%s)' % db)
        except:
            return (u'数据库配置错误')
        return redb

    # 数据库校验方法
    @staticmethod
    def checkdb(data, **kwargs):
        if data['SQL语句'] != '':
            db = checkdbaction._todict(kwargs['db'])
            sqlscript = data[5]
            expectedvalue = data[6]
            if sqlscript:
                conn = pymysql.connect(
                    host=db['host'],
                    port=int(db['port']),
                    user=db['user'],
                    passwd=db['password'],
                    db=db['dbname'],
                    charset='utf8'
                )
                cur = conn.cursor()
                try:
                    size = cur.execute(sqlscript)
                except:
                    print(u'用例'+data['用例名称'] + u'是否检查数据库输入不合法')
                    raise RuntimeError
                cur.close()
                conn.commit()
                conn.close()
                if size > 0:
                    print(u"查询出数据条数为 " + str(size) + u" 条")
                    info = cur.fetchmany(1)
                    infol = list(info[0])
                    arr = expectedvalue.split(',')
                    for i in range(len(infol)):
                        infol[i] = str(infol[i]).encode("utf-8")
                    for i in range(len(arr)):
                        arr[i] = str(arr[i]).encode("utf-8")
                    infol.sort()
                    arr.sort()
                    if infol == arr:
                        print(u"数据库校验通过")
                    else:
                        print(u"数据库校验未通过,预期值: " + str(expectedvalue).replace('.0', ''))
                        print(u"实际值: " + str(info[0][0]))
                        raise AssertionError()
                else:
                    print(u"数据库中没有查询到数据")
                    raise AssertionError
            else:
                print(u"不进入SQL判断")
        else:
            print(u"不进入SQL判断")