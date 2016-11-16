# -*- coding: UTF-8 -*-
import os
import sys

import Mylogging
from Schedule import schedule

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

class DownloadWorker(threading.Thread):
    def __init__(self, workQueue):
        self.workQueue = workQueue

    def run(self):


    def download_picture(self, url, path = ""):
    	if(not path):
    		path = os.getcwd()

    	




class Download(object):
    def __init__(self, num_threading = 10):
        self.workQueue = Queue.Queue()
        self.workers = []
        self._initThread(num_threading)

    def _initThread(self, num_threading):
    	for i in range(num_threading):
    		downloader = DownloadWorker(workQueue = self.workQueue)
    		self.workers.append(downloader)

    def start_download(self):
    	for item in self.workers:
    		item.start()

    def GetTodown(self):
    	list = schedule.GetToDownload()
    	while (not list.empty()):
    		item = list.pop()
    		self.workQueue.put(item)



