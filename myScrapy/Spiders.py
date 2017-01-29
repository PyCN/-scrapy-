


from __Threading import ThreadManager
#from Download import Download
from Cache import Cache, Trans
import Config_paser

class Myscrapy(object):
    # Get response from website
    ReqtoWeb = ThreadManager(num_threading = 10)#int(Config_paser.num_threading)#)
    # This is for download files
    #Downloader = Download
    #a helper class
    Trans = Trans
    # For storage response temporary
    Cache = Cache()


    def __init__(self, import_name):

        self.spider_name = import_name


        self.content = []
        self.callback_func = []


    def run(self, execute_app):
        if not isinstance(execute_app, execute_app.__class__):
            raise TypeError('app parameter must be a class instance!!')

        for req in execute_app.start_request():
            if req.url and req.method:
                url = req.url
                method = req.method
                formdata = None
                headers = req.headers
                cookieJar = req.meta

                if method == 'POST':
                    formdata = req.formdata

                if req.callback is not None:
                    self.callback_func.append(req.callback)

                Trans_obj = self.Trans(url = url, cache_obj = self.Cache, method = method, headers = headers, cookieJar = cookieJar) \
                    if formdata is None else self.Trans(url=url, cache_obj=self.Cache, method=method, formdata = formdata)
                self.content.append(Trans_obj)

        self._SendRequest()

    def _SendRequest(self):
        if 0 == len(self.content):
            raise ValueError('url to scrapy is empty')

        self.ReqtoWeb.obj_content = self.content
        self.ReqtoWeb.start_thread()
        self.ReqtoWeb.waitForallThreadcompelete()

        self.content.pop(0)
        self._getResponse()

    def _getResponse(self):
        response = self.Cache.Response_Cache
        if len(self.callback_func) > 0:
            for func in self.callback_func:
                if len(self.callback_func) > 0:
                    self.callback_func.pop(0)

                generator = func(response = response)
                self._dealCallBack(generator)

    def _dealCallBack(self, req_generator):
        try:
            for req in req_generator:
                if req.url and req.method:
                    url = req.url
                    method = req.method

                    if req.callback is not None:
                        self.callback_func.append(req.callback)

                    Trans_obj = self.Trans(url= url, method = method, cache_obj = self.Cache)
                    self.content.append(Trans_obj)
                    #self.callback_func.append(req.callback)
                    self._SendRequest()
        except:
            return

    #def _sendCallBack(self):















