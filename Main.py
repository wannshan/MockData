__author__ = 'wanshan@163.com'

from mockMysqldata import *

def startGen():
    for item in Xmlparser.getItmes():
        if(Xmlparser.getDependencies(item)==[]):
            Service.genSingleTable(item,0,{})
        else:
            dependenciesItems=Xmlparser.getDependencies(item);
            rows =int(Xmlparser.attrValue(item,"rows"))
            if(Xmlparser.attrValue(item,"type")=="info"):
                fkValue={}
                #生成被依赖表
                for ditem in dependenciesItems:
                    Service.genSingleTable(ditem,rows,{})
                    fkValue[Xmlparser.attrValue(ditem,"fk")]=genUtil.getPkValues(Xmlparser.attrValue(ditem,"tableName"),Xmlparser.attrValue(ditem,"pk"),rows)
                #生成依赖表
                Service.genSingleTable(item,0,fkValue)
            else:#type=="relation" 1对n关系表
                fk=''
                a=[]
                fkValue={}
                for ditem in dependenciesItems:
                    if(Xmlparser.attrValue(ditem,"relationPostion")=='1'):
                        Service.genSingleTable(ditem,rows,{})
                        a=genUtil.getPkValues(Xmlparser.attrValue(ditem,"tableName"),Xmlparser.attrValue(ditem,"pk"),rows)
                        fk=Xmlparser.attrValue(ditem,"fk");

                    else:
                        nvalue=int(Xmlparser.attrValue(ditem,"nvalue"))
                        Service.genSingleTable(ditem,rows*nvalue,{})
                        fkValue[Xmlparser.attrValue(ditem,"fk")]=genUtil.getPkValues(Xmlparser.attrValue(ditem,"tableName"),Xmlparser.attrValue(ditem,"pk"),rows*nvalue)
                        #生成依赖表
                fkValue[fk]=genUtil.arryEnlarge(a,nvalue)#数组放大
                Service.genSingleTable(item,0,fkValue)

conn,cur=Dbopt.connDB()
startGen()
Dbopt.connClose(conn,cur)
# mockMysqldata.funcinit()
# print('223')

