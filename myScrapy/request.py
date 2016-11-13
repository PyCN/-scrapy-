import requests

"""
this documention deal with request
"""
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


class Request(object):
    __slots__ = ['encoding','request','url','method','headers','callback']

    def __init__(self, *args, **kwargs):

        self.encoding = "utf-8"

        if kwargs:
            try:
                formdata = kwargs.pop('formdata')
            except:
                formdata = None

            try:
                http = kwargs.pop('url')
            except:
                http = None

            try:
                method = kwargs.pop('method')
            except:
                method = None

            try:
                headers = kwargs.pop('headers')
            except:
                headers = None

            try:
                func = kwargs.pop('callback')
            except:
                func = None

            if formdata:
                items = formdata.iteritems() if isinstance(formdata, dict) else formdata
                self.request = [(str_to_unicode(k, self.encoding), str_to_unicode(v, self.encoding)) \
                        for k,v in items]

            self.url = http if http else None
            self.method = method if method else None
            self.func = func if func else  None

    def get():

        http_url = str_to_unicode(self.url, self.encoding)
        response = requests.get(url = http_url, headers = headers)
        response.encoding = 'utf-8'
        return response.text

    def post():

        http_url = str_to_unicode(self.url, self.encoding)
        response = requests.post(url = http_url, data = self.request, headers = self.headers)
        response.encoding = 'utf-8'
        return response.text






