import sqlite3
import time


def convertor(country_name):
	name = country_name
	conn = sqlite3.connect('country_code.db')
	c = conn.cursor()
	with conn:
		c.execute("SELECT * FROM country_code WHERE names = '{}'".format(name))
		output = c.fetchone()[3]
	conn.close()
	return output



## This program takes in name of a country and returns its country code
##it 1st fetches by name and returns a tuple which has that country's name,
##alpha_code,alpha_code2 and code, we return only its code using line 11
## use example print(convertor('Albania'))