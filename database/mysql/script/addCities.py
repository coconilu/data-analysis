import sys
sys.path.append("..")

from useBayesDB import getCursor, getConn
import json

cursor = getCursor()
conn = getConn()

f = None

def transformToTuple(dict):
  dataList = dict["data"].split("|")
  return (dataList[3], dataList[0], dict["display"], dataList[1], int(dataList[2]))

def cleanDic(dict):
  cityList = []
  cityTupleList = []
  dict.pop("热门")
  print(dict.keys())
  for _list in dict.values():
    for _listCity in _list.values():
      cityList.extend(_listCity)
  for city in cityList:
    _tuple = transformToTuple(city)
    cityTupleList.append(_tuple)
  return cityTupleList

def insertCities(str):
  citiesObj = json.loads(str)
  cityTupleList = cleanDic(citiesObj)
  print(cityTupleList)
  sql = "INSERT INTO cities (shortkey, pronunciation, shortname, displayname, priority) VALUES (%s, %s, %s, %s, %s)"
  cursor.executemany(sql, cityTupleList)
  conn.commit()


try:
  f = open('../../cities.json', 'r', encoding = 'utf-8')
  insertCities(f.read())
finally:
  if f:
    f.close()
