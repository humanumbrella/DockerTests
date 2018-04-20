import MySQLdb

f = open("read-from-file.txt","r")

lines = f.read()

print lines.rstrip()

db = MySQLdb.connect(host="host.docker.internal",port=8889,user="asdf", passwd="asdf", db="asdf")

print "connected to db!"

cur_db = db.cursor()

cur_db.execute("SELECT * FROM fdsa")

cc = cur_db.fetchall()

print cc


print "we did it test slack integratiossssn"
