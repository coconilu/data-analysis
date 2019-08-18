import mysql.connector

bayesConn = mysql.connector.connect(
    host="localhost",       # 数据库主机地址
    user="root",    # 数据库用户名
    passwd="adsl",   # 数据库密码
    database="bayes_db"
)

bayesCursor = bayesConn.cursor()


def getConn():
    return bayesConn


def getCursor():
    return bayesCursor
