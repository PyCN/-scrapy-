# -*- coding: UTF-8 -*-
import copy
from Queue import Queue

from Mylogging import INFO,WARNING
from request import Request


class Schedule(object):
	def __init__(self):
		self.Works_get = []
		self.Works_post = []

		self.result_get = []
		self.result_post = []

		self.download_list = []
		''' 
		Addto_GET函数用来get请求的参数写入队列里面，等待调度

		'''
	def AddTodo_Get(self, object):
		if not isinstance(object, Request):
			WARNING("[Schedule] [GET]the wrong params!!")
			return
		obj = object
		item = []

		if obj.url is None:
			WARNING("[Schedule] [GET] without url ??")
			return

		item.append(obj.url)
		item.append(obj.method)
		item.append(obj.headers)
		item.append(obj.callback)
		INFO("[Schedule] [GET] url = {}, method = {}, hearders = {}".format(obj.url, obj.method, obj.headers))
		self.Works_get.append(item)
		print len(self.Works_get)

	def GetfromWorks_Get(self):
		item_Que = Queue()
		print len(self.Works_get)
		print "ll"
		while (len(self.Works_get)):
			item = self.Works_get.pop()
			print item[0],item[1]
			item_Que.put(item)

		return item_Que

	def GetfromWorks_Post():
		item_Que = Queue()

		while (not self.Works_post.empty()):
			item = self.Works_post.pop()
			item_QUe.put(item)

		return item_Que

	def AddTodo_Post(self, object):
		if not isinstance(object, object):
			WARNING("[Schedule] [POST] [POST]the wrong params!!")
			return

		obj = object
		item = []

		if (obj.url is None or obj.request is None):
			WARNING("[Schedule] [POST] without url or request??")
			return

		item.append(obj.url)
		item.append(obj.method)
		item.append(obj.request)
		item.append(obj.headers)
		item.append(obj.func)
		INFO("[Schedule] [POST] url = %s, method = %s, request = %s, headers = %s", obj.url, obj.method, obj.request, obj.headers)
		self.Works_post.append(item)

	def Putresult_Get(self, response):
		if not isinstance(response, list):
			WARNING("[Schedule] [result] the wrong params!!")
			return
		print len(response)
		print "mm"
		self.result_get.append(response)

	def Get_result_Get(self):

		item = self.result_get.pop()
		item_list = copy.deepcopy(item)
		print 'xx'
		print len(self.result_get)
		print len(item_list)
		INFO("[Schedule] [result] get result !!")
		return item_list

	def Get_result_Post(self):

		item_list = copy.deepcopy(self.result_post)
		INFO("[Schedule] [result] get post result !!")
		return item_list

	def Putresult_Post(self, response):
		if not isinstance(object, str):
			WARNING("[Schedule] [result] the wrong params!!")
			return

		self.result_post.append(response)

	def Judge_empty_get(self):
		if not len(self.result_get):
			return True
		else:
			return False

	def Judge_empty_post(self):
		if self.result_post.empty():
			return True
		else:
			return False

	def PutToDownload(self, object):
		obj = object
		self.download_list.append(obj)

	def GetToDownload(self):
		list = []
		list = copy.deepcopy(self.download_list)
		return list


schedule = Schedule()




