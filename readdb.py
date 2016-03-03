#!/usr/bin/python

print 'hello 1'

#import MySQLdb
import os

print 'hello 2'

DB_IP = os.environ.get('OPENSHIFT_MYSQL_DB_HOST','127.0.0.1')
DB_PORT = int(os.environ.get('OPENSHIFT_MYSQL_DB_PORT',3306))
DB_USER = os.environ.get('OPENSHIFT_MYSQL_DB_USERNAME','sudeep')
DB_PWD = os.environ.get('OPENSHIFT_MYSQL_DB_PASSWORD','Hello_AWS')

conn = MySQLdb.connect(host=DB_IP,    # your host, usually localhost
					 port=DB_PORT,
                     user=DB_USER,         # your username
                     passwd=DB_PWD,  # your password
                     db="db01")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = conn.cursor()

# SQL select
cur.execute("SELECT * FROM soccer")


for row in cur.fetchall():
    print row

db.close()

