import threading
import Queue

from lxml import etree
from engine import ScrapyWorker

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



