# -*- coding: utf-8 -*-
import cx_Oracle

#常量
username="drp"
userpwd="drp360kad"
host="192.168.1.23"
port=1521
dbname="kaderp"
managecookies_insert = "insert into drp.managecookies(id,username,kadtoken) values('%s','%s','%s')"
managecookies_query="select * from drp.managecookies where username='%s'"
managecookies_Update="update drp.managecookies set kadtoken='%s',localtime=to_date('%s','yyyy-mm-dd hh24:mi:ss') where username='%s'"
managecookies_queryall="select * from drp.managecookies"

userlogintoken_query="select * from drp.userlogintoken where username='%s'"
userlogintoken_Update="update drp.userlogintoken set kadtoken='%s',localtime=to_date('%s','yyyy-mm-dd hh24:mi:ss') where username='%s'"




#连接数据库
def ConnectionOpen(sql):
    dsn=cx_Oracle.makedsn(host, port, dbname)
    connection=cx_Oracle.connect(username, userpwd, dsn)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()

def ConnectionCursor():
    dsn=cx_Oracle.makedsn(host, port, dbname)
    connection=cx_Oracle.connect(username, userpwd, dsn)
    cursor = connection.cursor()
    return  cursor




#增删改查
def InsertToken(self, ds, uns, kadts):
    sql = managecookies_insert% (ds, uns, kadts)
    ConnectionOpen(sql)


def Query():
    username = []
    sql=managecookies_queryall
    Qucursor=ConnectionCursor()
    Qucursor.execute(sql)
    result = Qucursor.fetchall()
    for row in result:
        username = row[1]
    return username
    cursor.close()
    connection.close()


def QueryToken(username):
    sql=managecookies_query%(username)
    Qucursor=ConnectionCursor()
    Qucursor.execute(sql)
    result = Qucursor.fetchall()
    for row in result:
        id = row[0]
        username = row[1]
        kadtoken = row[2]
    return kadtoken
    cursor.close()
    connection.close()



def UpdateToken( token, time,name):
    sql = managecookies_Update% (token, time,name)
    ConnectionOpen(sql)


#接口获取操作


def IFUpdateToken( token, time,name):
    sql = userlogintoken_Update% (token, time,name)
    ConnectionOpen(sql)


def IFQueryToken(username):
    sql=userlogintoken_query%(username)
    Qucursor=ConnectionCursor()
    Qucursor.execute(sql)
    result = Qucursor.fetchall()
    for row in result:
        id = row[0]
        username = row[1]
        kadtoken = row[2]
    return kadtoken
    cursor.close()
    connection.close()