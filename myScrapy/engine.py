import threading
from lxml import etree
#from __Threading import ThreadManager, ScrapyWorker
from threading import Thread


class engine_Manager(object):

    def __init__(self):
        self.request_object = None
        self.request_list = []
        self.Thread_Scrapy = ThreadManager()

    def Crawer(self):
        request_object = spider.start_request()
        while True:
            try:
                if(res_object.method == "GET"):
                    res_object = request_object.next()
                    self.request_list.append(res_object)

                elif(res_object.method == "POST"):
                    self.request_list.append(res_object)

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
                    if(isinstance(response_next, object)):
                        self.engine.Crawer_next(response_next)

            except StopIteration as e:
                pass
                break



class ScrapyWorker(threading.Thread, engine_Manager):
    def __init__(self, workQueue, resultQueue, **kwargs):
        super(ScrapyWorker,self).__init__(self, **kwargs)
        self.engine = super(threading.Thread, self)
        self.workQueue = workQueue
        self.resultQueue = resultQueue

    def run(self):
        while (not self.workQueue.empty()):
            res = self.workQueue.get(False)
            if (res.method == "GET"):
                res_url = res.get()
            elif (res.method == "POST"):
                res_url = res.post()
            html = etree.HTML(res_url.lower.decode("utf-8"))
            response = res.func(html)
            if (isinstance(response, object)):
                self.engine.Crawer_next(response)





