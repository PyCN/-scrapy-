# -*- coding: UTF-8 -*-

import threading
from lxml import etree
#from __Threading import ThreadManager, ScrapyWorker
from threading import Thread

from Schedule import schedule
from Spiders import spider
from Mylogging import INFO,WARNING


class engine_Manager(object):

    def __init__(self):
        self.request_object = None
        self.request_list = []

    def sendToSchedule(self, res = ""):
        if (not res):
            request_object = spider.start_request()
            print type(request_object)
        else:
            request_object = res

        while True:
            try:
                res_object = request_object.next()
                if(res_object.method == "GET"):
                    schedule.AddTodo_Get(res_object)
                elif(res_object.method == "POST"):
                    schedule.AddTodo_Post(res_object)
                elif(res_object.method == "DOWNLOAD"):
                    schedule.Download(res_object)


            except StopIteration:
                INFO("[engine] [senToSchedule] generation is empty")
                break


    def GetfromSchedule(self):

        while (not schedule.Judge_empty_get()):
            item = schedule.Get_result_Get()
            print len(item)
            self.callback_func(lis = item)


    def callback_func(self, lis):
        if (not isinstance(lis, list)):
            return
        print len(lis)
        response = lis[0]
        callback = lis[1]

        request_next = callback(response)
        if (not request_next):
            WARNING("[engine] [callback_func] nothing to call back")
            return
        
        self.sendToSchedule(res = request_next)
       

engine = engine_Manager()







