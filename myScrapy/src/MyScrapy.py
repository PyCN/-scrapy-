from myScrapy import Myscrapy
from myScrapy import Request


app = Myscrapy(__name__)
class test(object):
    def start_request(self):
        for i in xrange(1, 5):
            yield Request(url = 'http://www.baidu.com/', method = 'GET', callback = self.deal_response)

    def deal_response(self, response):
        for i in xrange(1, 5):
            yield Request(url = 'http://www.baidu.com/', method = 'GET', callback = self.deal_response1)

    def deal_response1(self, response):
        print response.xpath("//head/title")[0].text


app.run(execute_app = test())
