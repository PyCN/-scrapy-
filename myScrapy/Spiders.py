

from request import Request
class mycrawer(object):
    def start_request(self):
        url = "http://www.baidu.com"
        yield Request(url = url, method = 'GET', callback = self.start_parse)

    def start_parse(self, response):
        print response

spider = mycrawer()


