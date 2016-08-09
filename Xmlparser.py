import xml.dom.minidom
#使用minidom解析器打开 XML 文档
def getItmes():#获取要生成表配置
    DOMTree = xml.dom.minidom.parse("config/genConfig.xml")
    collection = DOMTree.documentElement
    return collection.getElementsByTagName("item")

def getDependencies(element): #读取依赖表
    return element.getElementsByTagName("dependency");

def attrValue(element,atrrName): #读取属性值
    if element.hasAttribute(atrrName):
        return element.getAttribute(atrrName)
    else:
        return ''