from getConn import getConn

mydb = getConn()

cs = mydb.cursor()


def getCursor():
    return cs
