# -*- coding: utf-8 -*-
import cx_Oracle

#常量
username="drp"
userpwd="drp360kad"
host="192.168.1.23"
port=1521
dbname="kaderp"
Py_SMSValidateCodeCacheKey_insert = "insert into drp.Py_SMSValidateCodeCacheKey(id,username,kadtoken) values('%s','%s','%s')"





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
def TsetDbInsert(self, ds, uns, kadts):
    sql = Py_SMSValidateCodeCacheKey_insert% (ds, uns, kadts)
    ConnectionOpen(sql)







