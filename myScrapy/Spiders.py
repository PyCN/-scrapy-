


from __Threading import ThreadManager
from Download import Download
from Cache import Cache, Trans
import Config_paser

class Myscrapy(object):
    # Get response from website
    ReqtoWeb = ThreadManager(num_threading = 10)#int(Config_paser.num_threading)#)
    # This is for download files
    Downloader = Download
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

                if req.callback is not None:
                    self.callback_func.append(req.callback)

                Trans_obj = self.Trans(url = url, cache_obj = self.Cache, method = method)
                self.content.append(Trans_obj)

        self._SendRequest()

    def _SendRequest(self):
        if 0 == len(self.content):
            raise ValueError('url to scrapy is empty')

        self.ReqtoWeb.obj_content = self.content
        self.ReqtoWeb.start_thread()
        self.ReqtoWeb.waitForallThreadcompelete()

        del self.content[:]
        self._getResponse()

    def _getResponse(self):
        response = self.Cache.Response_Cache
        if len(self.callback_func) > 0:
            for func in callback_func:
                generator = func(response = response)
                self._dealCallBack(generator)

            del self.callback_func[:]


    def _dealCallBack(self, req_generator):

        for req in req_generator:
            if req.url and req.method:
                url = req.url
                method = req.method

                if req.callback is not None:
                    self.callback_func.append(req.callback)

                Trans_obj = self.Trans(url, method)

                self.callback_func.append(Trans_obj)

        self._SendRequest()















