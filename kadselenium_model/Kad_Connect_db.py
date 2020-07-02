# -*- coding: utf-8 -*-
#import MySQLdb
from selenium.webdriver.common.by import By
from MySQLdb_125.MySQLdb import release
#from MySQLdb_125 import MySQLdb
import MySQLdb




class MyConnection():

        def ConnectionOpen(self,sql):
                conn = MySQLdb.connect(host='192.168.1.26', port=5566, user='lihuaming', passwd='123456', db='kad_po',charset='utf8')
                cur = conn.cursor()
                cur.execute(sql)
                cur.close()
                conn.commit()
                conn.close()






#2.0后台登录信息保存到MySQL数据库
class KadModel():

      def InsertToken(self,ds,uns,kadts):
            sql = "insert into kad_po.managecookies(id,username,kadtoken) values('%s','%s','%s')"%(ds,uns,kadts)
            conne = MyConnection()
            conne.ConnectionOpen(sql)



      def QueryToken(self,name):
            conn = MySQLdb.connect(host='192.168.1.26', port=5566, user='lihuaming', passwd='123456', db='kad_po',charset='utf8')
            sql="select * from kad_po.managecookies where username='%s'"%(name)
            cur = conn.cursor()
            cur.execute(sql)
            results = cur.fetchall()
            for row in results:
                    id = row[0]
                    username = row[1]
                    kadtoken = row[2]
            return kadtoken
            cur.close()
            conn.commit()
            conn.close()



      def UpdateToken(self,token,name):
           sql = "update kad_po.managecookies set kadtoken='%s' where username='%s'"%(token,name)
           conne=MyConnection()
           conne.ConnectionOpen(sql)




#首营商品档案商品查询
      def WaerQuery(self):
            list = [];
            conn = MySQLdb.connect(host='192.168.1.26', port=5566, user='lihuaming', passwd='123456', db='kad_po',
                                   charset='utf8')
            sql = 'select RegisTrationNumber,maxcount from kad_po.UV_WI_FIRSTOPERATIONGOOD'
            cur = conn.cursor()
            cur.execute(sql)
            results = cur.fetchall()
            for row in results:
                RegisTrationNumber = row[0]
                list.append(RegisTrationNumber)
            return list
            cur.close()
            conn.commit()
            conn.close()



#首营商品档案商品条数
      def MaxCount(self,max):
            conn = MySQLdb.connect(host='192.168.1.26', port=5566, user='lihuaming', passwd='123456', db='kad_po',
                                   charset='utf8')
            sql = "select maxcount from kad_po.UV_WI_FIRSTOPERATIONGOOD where RegisTrationNumber='%s'"%(max)
            cur = conn.cursor()
            cur.execute(sql)
            results = cur.fetchall()
            for row in results:
                maxcount=row[0]
            return maxcount
            cur.close()
            conn.commit()
            conn.close()