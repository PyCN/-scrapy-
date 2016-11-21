import threading
import Queue

import requests
from lxml import etree

from Schedule import schedule
from Mylogging import INFO,WARNING



def str_to_unicode(text, encoding='utf-8'):
    """
    convert string to unicode
    """
    if isinstance(text, str):
        return text.decode(encoding)
    elif isinstance(text, unicode):
        return text
    else:
        raise TypeError('str_to_unicode must receive a str or unicode object, got %s' % type(text).__name__)

class ScrapyWorker(threading.Thread):
    def __init__(self, workQueue, resultQueue, **kwargs):
        super(ScrapyWorker,self).__init__(**kwargs)
        self.workQueue = workQueue
        self.resultQueue = resultQueue

    def run(self):
        while (not self.workQueue.empty()):
            res = self.workQueue.get(False)
            print res.qsize()
            
            while not res.empty():
                list = res.get()
                method = list[1]

                if (method == "GET"):
                    url = list[0]
                    method = list[1]
                    headers = list[2]
                    callback = list[3]

                    item = []

                    response = self.get(url = url, method = method, headers = headers).content
                    final_res = etree.HTML(response.lower().decode("utf-8"))
                    item.append(final_res)
                    item.append(callback)
                    schedule.Putresult_Get(item)

                elif(method == "POST"):
                    url = list[0]
                    method = list[1]
                    request = list[2]
                    headers = list[3]
                    callback = list[4]

                    item = []

                    response = self.post(url = url, method = method, request = request, headers = headers)
                    final_res = etree.HTML(response.lower.decode("utf-8"))
                    INFO('final_res = {}'.format(final_res))
                    item.append(final_res)
                    item.append(callback)
                    schedule.Putresult_Post(item)

    def get(self, url, method, headers):
        http = str_to_unicode(text = url, encoding = 'utf-8')
        response = requests.get(url = http, headers = headers)
        response.encoding = 'utf-8'
        return response


    def post(self, url, method, request, headers):
        http = str_to_unicode(text = url, encoding = 'utf-8')
        response = requests.post(url = http, data = request , headers = headers)
        response.encoding = 'utf-8'
        return response


class ThreadManager(object):
    def __init__(self, num_threading = 10):
        self.workQueue = Queue.Queue()
        self.resultQueue = Queue.Queue()
        self.workers = []
        self._initThread(num_threading)

    def _initThread(self, num_threading):
        for i in range(num_threading):
            works = ScrapyWorker(workQueue=self.workQueue, resultQueue=self.resultQueue)
            self.workers.append(works)

    def waitForallThreadcompelete(self):
        while len(self.workers):
            worker = self.workers.pop()
            worker.join()
            if worker.isAlive() and not len(self.workers):
                self.workers.append(worker)


    def add_func_get(self):
        item = schedule.GetfromWorks_Get()
        self.workQueue.put(item)
        print item.qsize()

    def add_func_post(self):
        item = schedule.GetfromWorks_Post()
        self.workQueue.put(item)

    def start_thread(self):
        for w in self.workers:
            w.start()



