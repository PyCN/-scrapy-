import threading
from lxml import etree
from __Threading import ThreadManager, ScrapyWorker
from threading import Thread


class engine_Manager(object):

    def __init__(self):
        self.engine = engine_Manager()
        self.request_object = None
        self.request_list = []
        self.Thread_Scrapy = self.ScrapyManager()

    def Crawer(self):
        request_object = spider.start_request()
        while True:
            try:
                res_object = request_object.next()
                self.request_list.append(res_object)
                # if (res_object.method == "GET"):
                #     response = res_object.get()
                #     html = etree.HTML(response.lower.decode("utf-8"))
                #     response = res_object.func(html)
                #     if(isinstance(response, object)):
                #         self.engine.Crawer_next(response)


                elif(res_object.method == "POST"):
                self.request_list.append(res_object)
                    # response = res_object.post()
                    # html = etree.HTML(response.lower.decode("utf-8"))
                    # res_object.func(html)
                    # if (isinstance(response, object)):
                    #     self.engine.Crawer_next(response)

            except StopIteration:

                break
        self.Crawer_start()

    def Crawer_start(self):
        if not self.request_list.empty():
            threading.Thread(self.Thread_Scrapy.add_func(func = self.request_list)).start()


    def Crawer_next(self, response):
        while True:
            try:
                res_object = response.next()
                if(res_object.method == "GET"):
                    response_next = res_object.get()
                    html = etree.HTML(response_next.lower.decode("utf-8"))
                    response_next = res_object.func(html)
                    if(isinstance(response_next, object)):
                        self.engine.Crawer_next(response_next)

                elif(res_object.method == "POST"):
                    response_next = res_object.post()
                    html = etree.HTML(response_next.lower.decode("utf-8"))
                    response_next = response_next.func(html)
                    if(isinstance(response_next,object)):
                        self.engine.Crawer_next(response_next)

            except StopIteration as e:
                pass
                break





