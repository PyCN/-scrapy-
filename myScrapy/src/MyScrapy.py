from myScrapy import Myscrapy
from myScrapy import Request

app = Myscrapy(__name__)

class test(object):
    def start_request(self):
        yield Request(url = 'https://www.baidu.com/', method = 'GET')

app.run(execute_app = test())
