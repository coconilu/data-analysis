from getCursor import getCursor

cs = getCursor()

cs.execute("show databases")

for x in cs:
  print(x)