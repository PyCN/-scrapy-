import threading
import Queue

from lxml import etree

import engine_Manager

class ScrapyWorker(threading.Thread, engine_Manager):
    def __init__(self, workQueue, resultQueue, **kwargs):
        super(ScrapyWorker,self).__init__(self, **kwargs)
        self.engine = super(threading.Thread,self)
        self.workQueue = workQueue
        self.resultQueue = resultQueue

    def run(self):
        while (not self.workQueue.empty()):
            res = self.workQueue.get(False)
            res_url = res.get()
            html = etree.HTML(res_url.lower.decode("utf-8"))
            response = res.func(html)
            if (isinstance(response, object)):
                self.engine.Crawer_next(response)


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
            if worker.isAlive() and not self.workers.empty():
                self.workers.append(worker)


    def add_func(self, func):
        if(isinstance(func, list)):
            while not func.empty():
                item = func.pop()
                self.workQueue.put(item)
        self.start_thread()

    def start_thread(self):
        for w in self.workers:
            w.start()



