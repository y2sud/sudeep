#!/usr/bin/python

print 'hello 1'


import os

print 'hello 2'

DB_IP = os.environ.get('EXTERNAL_MYSQL_SERVICE_SERVICE_HOST','127.0.0.1')
DB_IP2 = os.environ.get('MYSQL_SERVICE_HOST','127.0.0.1')

DB_PORT = int(os.environ.get('MYSQL_SERVICE_PORT',3306))
DB_USER = os.environ.get('MYSQL_SERVICE_USER','?')
DB_PWD = os.environ.get('MYSQL_PASSWORD','??')
DB_NAME = os.environ.get('MYSQL_SERVICE_DATABASE','???')

DB_NAME = 'db01'
DB_USER = 'baadal_sql'
DB_PWD = 'merasql'

print 'db_ip ' + DB_IP
print 'db_ip2 ' + DB_IP2
print 'db_name ' + DB_NAME
print 'db_user ' + DB_USER

import MySQLdb
#import MySQL-python


def test():
	conn = MySQLdb.connect(host=DB_IP2,    # your host, usually localhost
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
	
	conn.close()
	print 'close'
	return row

if __name__ == '__main__':
	test()
