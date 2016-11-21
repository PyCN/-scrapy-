# -*- coding: UTF-8 -*-

import threading
from lxml import etree
from threading import Thread

from Schedule import schedule
from Spiders import spider
from Mylogging import INFO,WARNING
import __Threading
import Download


class engine_Manager(object):

    def __init__(self):
        self.request_object = None
        self.request_list = []
        self.thread = __Threading.ThreadManager()
        self.download = Download.Download()
        self.request_buf = []

    def engine_start(self, res = None):
        if res is None:
            request_object = spider.start_request()
        else:
            request_object = res

        while True:
            try:
                res_object = request_object.next()
                if(res_object.method == "GET"):
                    schedule.AddTodo_Get(res_object)
                    INFO("[engine_Manager] send http for get!!")

                elif(res_object.method == "POST"):
                    schedule.AddTodo_Post(res_object)
                    INFO("[engine_Manager] send http for post!!")

                elif(res_object.method == "DOWNLOAD"):
                    schedule.PutToDownload(res_object)
                    INFO("[engine_Manager] send download message!!")

            except StopIteration:
                INFO("[engine] [senToSchedule] generation is empty")
                break

        if res_object.method == "GET":
            self.thread.add_func_get()
            self.thread.start()
            self.thread.waitForallThreadcompelete()

        elif res_object.method == "POST":
            self.thread.add_func_post()
            self.thread.start()
            self.thread.waitForallThreadcompelete()

        elif res_object.method == "DOWNLOAD":
            self.download.GetTodown()
            self.download.start()
            self.download.waitForallThreadcompelete()

        self._GetfromSchedule()


    def _GetfromSchedule(self):

        while not schedule.Judge_empty_get():
            item = schedule.Get_result_Get()
            self._callback_func(lis = item)


    def _callback_func(self, lis):
        if not isinstance(lis, list):
            return

        response = lis[0]
        callback = lis[1]

        request_next = callback(response)
        if request_next is None:
            WARNING("[engine] [callback_func] nothing to call back")
            return

        self.request_buf.append(request_next)

        if schedule.Judge_empty_get():
            while len(self.request_buf):
                tmp = self.request_buf.pop()
                self.engine_start(tmp)
       

engine = engine_Manager()







