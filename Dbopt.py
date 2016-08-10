__author__ = 'wannshan@163.com'
import sys
import pymysql
import Xmlparser
cur =''
def connDB(): #连接数据库函数
    conntionInfo=Xmlparser.getConncetionInfo()
    conn = pymysql.connect(host=conntionInfo['host'], port=int(conntionInfo['port']), user=conntionInfo['userName'], passwd=conntionInfo['password'], db=conntionInfo['db'],charset='utf8')
    conn.autocommit(1)
    global cur
    cur= conn.cursor()
    return (conn,cur)

def exeUpdate(sql):#更新语句，可执行update,insert语句
    global cur
    sta=cur.execute(sql);
    return(sta);

def exeQuery(sql):#查询语句
    global cur
    cur.execute(sql);
    return (cur);

def connClose(conn,cur):#关闭所有连接
    cur.close();
    conn.close();
