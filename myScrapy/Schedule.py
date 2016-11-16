# -*- coding: UTF-8 -*-
import copy
import Queue.Queue

import Mylogging



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
		if not isinstance(object, object):
			WARNING("[Schedule] [GET]the wrong params!!")
			return
		obj = object
		item = []

		if not exists obj.url:
			WARNING("[Schedule] [GET] without url ??")
			return

		item.append(obj.url)
		item.append(obj.method)
		item.append(obj.headers)
		item.append(obj.func)
		INFO("[Schedule] [GET] url = %s, method = %s, hearders = %s",obj.url, obj.method, obj.headers)
		self.Works_get.append(item)

	def GetfromWorks_Get():
		item_Que = Queue()

		while (not self.Works_get.empty()):
			item = self.Works_get.pop()
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

		if not (exists obj.url or exists obj.request):
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
		if not isinstance(response, str):
			WARNING("[Schedule] [result] the wrong params!!")
			return

		self.result_get.append(response)

	def Get_result_Get():
		item_list = []

		item_list = copy.deepcopy(self.result_get)
		INFO("[Schedule] [result] get result !!")
		return item_list

	def Get_result_Post():
		item_list = []

		item_list = copy.deepcopy(self.result_post)
		INFO("[Schedule] [result] get post result !!")
		return item_list

	def Putresult_Post(self, response):
		if not isinstance(object, str):
			WARNING("[Schedule] [result] the wrong params!!")
			return

		self.result_post.append(response)

	def Judge_empty_get(self):
		if self.result_get.empty:
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




