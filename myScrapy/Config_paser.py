from ConfigParser import SafeConfigParser
from Mylogging import INFO,WARNING
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
	INFO("[Config_paser] num_threading = {}".format(num_threading))

	locate = parser.get('system', 'locate')
	INFO("[Config_paser] locate path = {}".format(locate))

	headers = parser.get('system', 'headers')
	INFO("[Config_paser] headers = {}".format(headers))


