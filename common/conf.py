import yaml

class conf():
    #获取配置
    @staticmethod
    def get_config():
        f = open('config.yaml',encoding='utf-8')
        res = yaml.load(f)
        return res