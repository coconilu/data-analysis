from useBayesDB import getCursor

bc = getCursor()

tables = bc.execute('show tables')
print(tables)
# for table in tables:
#   print(table)