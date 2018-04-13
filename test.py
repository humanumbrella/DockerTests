import MySQLdb
import pandas
import numpy
import matplotlib
import paramiko

f = open("read-from-file.txt","r")

lines = f.read()

print lines.rstrip()

