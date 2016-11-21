# -*- coding: UTF-8 -*-

from Mylogging import INFO,WARNING
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
    __slots__ = ['encoding','formdata','url','method','headers','callback','filename','download_type']
    def __init__(self, *args, **kwargs):

        try:
            self.url = kwargs.pop('url')
            INFO("[request] url to Crawer = {}".format(self.url))
        except Exception:
            self.url = None
            WARNING("[request] without url???, this request will be stopped!!")
            return

        try:
            self.method = kwargs.pop('method')
        except Exception:
            self.method = None
            WARNING("[request] without method auto set method to 'GET'")
            self.method = 'GET'

        try:
            formdata = kwargs.pop('formdata')
            if(self.method == "GET"):
                WARNING("[request] ...there exists dict of formdata turn 'GET' to 'POST'")
                self.method = 'POST'
        except Exception:
            formdata = None
            if(self.method == 'POST'):
                WARNING("[request]...formdata is empty auto turn 'POST' to 'GET'")
                self.method = 'GET'

        if formdata:
            items = formdata.iteritems() if isinstance(formdata, dict) else formdata
            self.formdata = [(str_to_unicode(k, encoding = 'utf-8'), str_to_unicode(v, encoding = 'utf-8')) \
                    for k,v in items]

        try:
            self.headers = kwargs.pop('headers')
        except Exception:
            self.headers = None
            INFO("[request] without header, set header to None")

        try:
            self.callback = kwargs.pop('callback')
        except Exception:
            self.callback = None
            INFO("[request] nothing to callback!!")

        try:
            self.filename = kwargs.pop('filename')
        except Exception:
            self.filename = None
            INFO("[request] without filename.......")

        try:
            self.download_type = kwargs.pop('download_type')
        except Exception:
            if self.method == "DOWNLOAD":
                WARNING("[request] method is download,but there isn't exists and method??, stop it!!")
                return





