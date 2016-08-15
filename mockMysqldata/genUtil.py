
from . import  Dbopt ,Xmlparser
import random
from datetime import datetime, timedelta
def getFields(tableName,pkName):#获取表字段信息
    connection=Xmlparser.getConncetionInfo()
    cur=Dbopt.exeQuery("select column_name,data_type,CHARACTER_MAXIMUM_LENGTH from information_schema.COLUMNS where table_name = '"+tableName+"' and table_schema = '"+connection['db']+"' ORDER BY ORDINAL_POSITION  ")
    b=[]
    for row in cur:
        if(row[0].lower()!=''+pkName.lower()+''):
            b.append([row[0],row[1],row[2]])
    return b
def getRows(tableName):#获取表记录数
    cur=Dbopt.exeQuery("select count(0) from "+tableName)
    for row in cur:
        rows=row[0]
    return int(rows)
def getPkValues(tableName,pkName,rows):
    cur=Dbopt.exeQuery("select "+pkName+" from "+tableName+" limit "+str(rows))
    a=[]
    for row in cur:
        a.append(row[0])
    return a
def mockData(flelds,rows,fkValues):#伪造数据更具字段数据类型
    fld=[]#字段数组
    fldData={}#字段值，候选值values key-value
    for a in flelds :
        fld.append(a[0])
        if(a[0] in fkValues.keys() and len(fkValues[a[0]])>0):
            fldData[a[0]]=fkValues[a[0]]
        else:
            #各个列生成策略单独类
            colmock=ColumnMockStrategy();
            fldData[a[0]]=colmock.mockColumData(a,rows)
    batch_list = []
    for i in range(rows):
        ret = []
        for a in flelds:
            p=fldData[a[0]][i]
            if isinstance(p, (int, float, bool)):
                ret.append(str(p))
            elif isinstance(p, (str)):
                ret.append('"' + p + '"')
            else:
                ret.append(p)
        batch_list.append('(' + ','.join(ret) + ')')
    return (batch_list,fld);
def testf():
    print('tttt')
def arryEnlarge(arr,n):#数组放大 n倍
    r=[]
    for i in arr:
        for j in range(n):
            r.append(i)
    return r;

class ColumnMockStrategy:
    def __init__(self):
        return
    def __genInt(self,rows,columnInfo):
        a=[]
        for i in range(rows):
            a.append(random.randint(1,rows));
        return a
    def __genVarchar(self,rows,columnInfo):
        a=[]
        lth =int(columnInfo[2])
        for i in range(rows):
            r=str(i)+columnInfo[0]
            if(len(r)>lth):
              a.append(r[0:lth])
            else:
              a.append(r)
        return a
    def __genDateTime(self,rows):
        days=-rows;
        a=[]
        for i in range(days,0):
            day = datetime.now()+ timedelta(days=(i+1))
            a.append(day.strftime('%Y-%m-%d %H:%M:%S'))
        return a
    def __genDouble(self,rows):
            a=[]
            for i in range(rows):
               a.append(float(random.randint(0,rows)*0.1))
            return a
    def __genOhters(self,rows):
        a=[]
        for i in range(rows):
            a.append(1);
        return a

    def mockColumData(self,columnInfo,rows):
       if(str(columnInfo[1])=='varchar'):
          return self.__genVarchar(rows,columnInfo)
       elif(str(columnInfo[1]).find('int')>=0):
          return self.__genInt(rows,columnInfo)
       elif(str(columnInfo[1])=='datetime'):
          return self.__genDateTime(rows)
       elif(str(columnInfo[1])=='double'):
          return self.__genDouble(rows)
       elif(str(columnInfo[1])=='float'):
          return self.__genDouble(rows)
       elif(str(columnInfo[1])=='decimal'):
          return self.__genDouble(rows)
       else:
          return self.__genOhters(rows)
    def test(self,rows):
        print(self.__genInt(rows))
