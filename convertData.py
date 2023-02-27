#!/usr/bin/env python
print("Content-Type: text/html;charset=utf-8")
print ("Content-type:text/html\r\n")

#-*- coding:utf-8 -*- 

import cgitb
import cgi 
import sys
import mysql.connector
import MySQLdb
from mysql.connector import Error
from mysql.connector import errorcode

cgitb.enable()

#Pegando Dados da requisição CGI
fs = cgi.FieldStorage()
for key in fs.keys():
    retorno = fs[key].value

# Abrindo Conexão com Banco MYSQL
db = MySQLdb.connect(host="", user="", passwd="", db="", charset="utf8", use_unicode = True)
cursor_mysql = db.cursor()

#Executando SELECT no BD
cursor_mysql.execute(""" SELECT 
CASE 
	WHEN (select data_util from dias_uteis where data_util = %s) IS NOT NULL AND
		 (select data from calendariorecesso where data = %s) IS NULL THEN %s
		 
    WHEN (select data_util from dias_uteis where data_util = DATE_ADD(%s, INTERVAL -2 DAY)) IS NOT NULL AND
		 (select data from calendariorecesso where data = DATE_ADD(%s, INTERVAL -2 DAY)) IS NULL THEN DATE_ADD(%s, INTERVAL -2 DAY)
		 
	WHEN (select data_util from dias_uteis where data_util = DATE_ADD(%s, INTERVAL -3 DAY)) IS NOT NULL AND
		 (select data from calendariorecesso where data = DATE_ADD(%s, INTERVAL -3 DAY)) IS NULL THEN DATE_ADD(%s, INTERVAL -3 DAY)
		 
	WHEN (select data_util from dias_uteis where data_util = DATE_ADD(%s, INTERVAL -4 DAY)) IS NOT NULL AND
		 (select data from calendariorecesso where data = DATE_ADD(%s, INTERVAL -4 DAY)) IS NULL THEN DATE_ADD(%s, INTERVAL -4 DAY) 	 
ELSE 'ERRO' END """, (retorno,retorno,retorno,retorno,retorno,retorno,retorno,retorno,retorno,retorno,retorno,retorno))

myresult = cursor_mysql.fetchone()

print(myresult[0])
#print("Hello, World!\n")

