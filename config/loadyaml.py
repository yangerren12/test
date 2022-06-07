#专门取yaml文件数据
import yaml
def loadyaml(filename):
    #打开文件数据
    steam= open(filename,'r',encoding='utf-8')
    #读取文件数据
    data = yaml.load(steam,yaml.FullLoader)
    return data
