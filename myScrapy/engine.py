# -*- coding: UTF-8 -*-

import threading
from lxml import etree
#from __Threading import ThreadManager, ScrapyWorker
from threading import Thread

from Schedule import schedule
import Mylogging


class engine_Manager(object):

    def __init__(self):
        self.request_object = None
        self.request_list = []
        self.Thread_Scrapy = ThreadManager()

    def sendToSchedule(self, res = ""):
        if (not res):
            request_object = spider.start_request()
        else:
            request_object = res

        while True:
            try:
                if(res_object.method == "GET"):
                    res_object = request_object.next()
                    schedule.AddTodo_Get(res_object)
                elif(res_object.method == "POST"):
                    res_object = request_object.next()
                    schedule.AddTodo_Post(res_object)

            except StopIteration:
                INFO("[engine] [senToSchedule] generation is empty")
                break


    def GetfromSchedule(self):
        item = []

        while (not Judge_empty_get()):
            item = schedule.Get_result_Get()
            self.callback_func(list = item)


    def callback_func(self, list):
        if (not isinstance(list, list)):
            return

        response = list[0]
        callback = list[1]

        request_next = callback(response)
        if (not request_next):
            WARNING("[engine] [callback_func] nothing to call back")
            return
        
        self.sendToschedule(res = request_next)
       

  







