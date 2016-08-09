import Dbopt
import Xmlparser
import genUtil
from functools import reduce

def getInsertFieldSql(f1,f2):
    return f1+","+f2

def genSingleTable(domcument,miniRows,fkValues):
    tableName=Xmlparser.attrValue(domcument,"tableName")
    pkName=Xmlparser.attrValue(domcument,"pk")
    rows=int(Xmlparser.attrValue(domcument,"rows"))
    if(miniRows>0 and rows<miniRows):
        rows=miniRows
    if(int(genUtil.getRows(tableName))>=rows):
        print(tableName,'已有数据无需生成')
        return
    else:
        rows=rows-int(genUtil.getRows(tableName))
        fieldsInfo=genUtil.getFields(tableName,pkName)
        batch_list,fld=genUtil.mockData(fieldsInfo,rows,fkValues);
    sql="insert into "+tableName+"("+reduce(getInsertFieldSql,fld)+") values %s"%','.join(batch_list)
    print(sql)
    Dbopt.exeQuery(sql)
    print(tableName,'表生成数据',rows,"条")


