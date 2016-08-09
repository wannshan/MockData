__author__ = 'wannshan@163.com'
import sys
import pymysql
cur=''
def connDB(): #连接数据库函数
    conn = pymysql.connect(host='192.168.64.129', port=3306, user='git', passwd='git', db='test',charset='utf8')
    conn.autocommit(1)
    global cur
    cur= conn.cursor()
    return (conn,cur)

def exeUpdate(sql):#更新语句，可执行update,insert语句
    global cur
    sta=cur.execute(sql);
    return(sta);

def exeDelete(tableName,IDs): #删除语句，可批量删除
    global cur
    for eachID in IDs.split(','):
        sta=cur.execute('delete from '+tableName+' where id =%d'% int(eachID));
    return (sta);

def exeQuery(sql):#查询语句
    global cur
    cur.execute(sql);
    return (cur);

def connClose(conn,cur):#关闭所有连接
    cur.close();
    conn.close();
