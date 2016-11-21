# -*- coding: UTF-8 -*-
import os
import sys
 
import requests

from Mylogging import INFO,WARNING
from Schedule import schedule
import Config_paser

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
        while not self.workQueue.empty():
            item = self.workQueue.get()
            if not isinstance(item, list):
                WARNING("[Download] error type, return!!")
                return

            try:
                url = item[0]
            except Exception:
                WARNING("[Download] url isn't exists, return !!")
                return

            try:
                download_type = item[1]
            except Exception:
                WARNING("[Download] error in download_type!!, return!!")
                return

            method = item[2]
            filename = item[3]

            if download_type == "picture":
                self.download_picture(image_url = url, filename = filename)
            elif download_type == "anything":
                self.download_anything(image_url = url, filename = filename)
            elif download_type == "custom":
                pass

    def download_anything(self, down_url, path = "", filename = ""):
        if path is None:
            if Config_paser.locate is None:
                path = os.path.getcwd()
            else:
                path = Config_paser.locate

        INFO("[Download] [download_anthing] the file will be downloaded in {}".format(path))

        if filename is not None:
            file = filename.split('.')
            if file[1] is None:
                filename += '.dat'
        else:
            filename = down_url + '.dat'

        os.path.join(path, filename)    

        try:
            result = requests.get(down_url, stream = True)
            with open(path, 'wb') as things:
                things.write(result.content)
        except Exception as e:
            WARNING(e)


    def download_picture(self, image_url, path = "", filename = ""):
    	if path is None:
    		if Config_paser.locate is None:
                path = os.path.getcwd()
            else:
                path = Config_paser.locate

        INFO("[Download] the picture will be downloaded in {}".format(path))

        if filename is not None:
            os.path.join(path, '{}.jpg'.format(filename))
        else:
            os.path.join(path, '{}.jpg'.format(image_url))

    	try:
            image = requests.get(image_url, stream = True)
            with open(path, 'wb') as img:
                img.write(image.content)
        except Exception as e:
            WARNING(e)


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
    	items = schedule.GetToDownload()
    	while not len(items):
    		item = items.pop()
    		self.workQueue.put(item)

    def waitForallThreadcompelete(self):
        while len(self.workers):
            worker = self.workers.pop()
            worker.join()
            if worker.isAlive() and not len(self.workers):
                self.workers.append(worker)



