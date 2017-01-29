import threading
import Queue
import urllib2
import urllib
import cookielib

from lxml import etree

from Cache import response_obj
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
        while not self.workQueue.empty():
            item_obj = self.workQueue.get()
            url = item_obj.url
            method = item_obj.method if item_obj.method else 'GET'
            cache = item_obj.cache
            headers = item_obj.headers or {}
            meta = item_obj.cookieJar or None
            cookie = None

            if not isinstance(meta, dict):
                WARNING('meta should be a dict')
            else:
                cookie = meta.get('cookieJar', None)

            try:
                formdata = item_obj.formdata if item_obj.formdata else None
            except:
                formdata = None

            if method == 'GET':
                response = response_obj()
                http_response, http_cookie = self.get_url(url, headers, cookie)
                response.cookie = http_cookie
                response.response_string = self.deal_response_with_xpath(http_response)
                cache.Response_Cache = response

            if method == 'POST':
                response = response_obj()
                http_response, http_cookie = self.get_url(url, formdata, headers, cookie)
                response.cookie = http_cookie
                response.response_string = self.deal_response_with_xpath(http_response)
                cache.Response_Cache = response


    def get_url(self, url, headers, cookie):

        if not isinstance(url, str):
            raise 'url or cookie type error!!'
        req = urllib2.Request(url, None, headers)
        try:
            if not isinstance(cookie, cookielib.CookieJar) and cookie is None:
                response = urllib2.urlopen(req)
            elif not isinstance(cookie, cookielib.CookieJar) and cookie is not None:
                cookie = cookielib.CookieJar()
                handler = urllib2.HTTPCookieProcessor(cookie)
                opener = urllib2.build_opener(handler)
                response = opener.open(req)
            elif isinstance(cookie, cookielib.CookieJar):
                handler = urllib2.HTTPCookieProcessor(cookie)
                opener = urllib2.build_opener(handler)
                response = opener.open(req)

        except urllib2.HTTPError:
            raise 'get url error!!'
        the_page = response.read()

        return the_page, cookie

    def deal_response_with_xpath(self, content):
        html = etree.HTML(content.decode('utf-8'))
        return html

    def post_url(self, url, formdata, headers, cookie):
        if not isinstance(url, str):
            raise 'url must be a string and fordata must be a dict'
        data = urllib.urlencode(formdata)
        req = urllib2.Request(url, data, headers)
        try:
            if not isinstance(cookie, cookielib.CookieJar) and cookie is None:
                response = urllib2.urlopen(req)
            elif not isinstance(cookie, cookielib.CookieJar) and cookie is not None:
                cookie = cookielib.CookieJar()
                handler = urllib2.HTTPCookieProcessor(cookie)
                opener = urllib2.build_opener(handler)
                response = opener.open(req)
            elif isinstance(cookie, cookielib.CookieJar):
                handler = urllib2.HTTPCookieProcessor(cookie)
                opener = urllib2.build_opener(handler)
                response = opener.open(req)

        except urllib2.HTTPError:
            raise 'get url error!!'
        the_page = response.read()

        return the_page, cookie


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


    @property
    def obj_content(self):
        return self.workQueue

    @obj_content.setter
    def obj_content(self, obj_content):
        if not isinstance(obj_content, list):
            raise TypeError("url_content must be list type")

        for obj_item in obj_content:
            self.workQueue.put(obj_item)

    def start_thread(self):
        for w in self.workers:
            w.start()



