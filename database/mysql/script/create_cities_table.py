import sys
sys.path.append("..")

from useBayesDB import getCursor

bc = getCursor()

print(bc)

bc.execute("CREATE TABLE if not exists cities (id INT AUTO_INCREMENT PRIMARY KEY, shortkey VARCHAR(10), pronunciation VARCHAR(120), shortname VARCHAR(120), displayname VARCHAR(120), priority INT)")
