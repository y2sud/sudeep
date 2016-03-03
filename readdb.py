#!/usr/bin/python

print 'hello 1'

#import MySQLdb
import os

print 'hello 2'

DB_IP = os.environ.get('EXTERNAL_MYSQL_SERVICE_SERVICE_HOST','127.0.0.1')
DB_IP2 = os.environ.get('MYSQL_SERVICE_HOST','127.0.0.1')

DB_PORT = int(os.environ.get('EXTERNAL_MYSQL_SERVICE_SERVICE_PORT',3306))
DB_USER = os.environ.get('MYSQL_USER','sudeep')
DB_PWD = os.environ.get('MYSQL_PASSWORD','Hello_AWS')
DB_NAME = os.environ.get('MYSQL_DATABASE','Hello_AWS')

print 'db_ip ' + DB_IP
print 'db_ip2 ' + DB_IP2
print 'db_name ' + DB_NAME

conn = MySQLdb.connect(host=DB_IP,    # your host, usually localhost
			port=DB_PORT,
                     user=DB_USER,         # your username
                     passwd=DB_PWD,  # your password
                     db=DB_NAME)        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = conn.cursor()

# SQL select
cur.execute("SELECT * FROM soccer")


for row in cur.fetchall():
    print row

db.close()

