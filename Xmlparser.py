import xml.dom.minidom
#使用minidom解析器打开 XML 文档
DOMTree = ''
def initXML():
    global DOMTree
    if(DOMTree==''):
      DOMTree = xml.dom.minidom.parse("config/genConfig.xml")

def getItmes():#获取要生成表配置
    initXML()
    collection = DOMTree.documentElement
    return collection.getElementsByTagName("item")

def getDependencies(element): #读取依赖表
    return element.getElementsByTagName("dependency")

def getConncetionInfo():
    initXML()
    collection = DOMTree.documentElement
    a={};
    element=collection.getElementsByTagName("dbConnection")[0]
    a['host']=attrValue(element,"host")
    a['port']=attrValue(element,"port")
    a['db']=attrValue(element,"db")
    a['userName']=attrValue(element,"userName")
    a['password']=attrValue(element,"password")
    return a

def attrValue(element,atrrName): #读取属性值
    if element.hasAttribute(atrrName):
        return element.getAttribute(atrrName)
    else:
        return ''