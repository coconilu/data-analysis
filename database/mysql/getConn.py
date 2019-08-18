import mysql.connector

myConn = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd="adsl"   # 数据库密码
)

def getConn():
  return myConn