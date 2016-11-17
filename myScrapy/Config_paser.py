from ConfigParser import SafeConfigParser
import logging

global num_threading
global locate
global headers

num_threading = ""
locate = ""
headers = ""

def start_parser():

	global num_threading
	global locate
	global headers

	parser = SafeConfigParser()
	parser.read("config.ini")
	num_threading = parser.get('system', 'num_threading')
	locate = parser.get('system', 'locate')
	headers = parser.get('system', 'headers')


