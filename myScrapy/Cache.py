class Cache(object):
    Response_Cache = []

    def __init__(self):
        pass
    @property
    def cache(self):
        if 0 == len(Response_Cache):
            raise EnvironmentError('cache is empty!!')

        return Response_Cache

    @cache.setter
    def cache(self, response):
        if not isinstance(response, str):
            raise ValueError('response is not string type')
        Response_Cache.append(response)


class Trans(object):
    __slots__ = ('url', 'method', 'cache','formdata', 'headers', 'cookieJar')

    def __init__(self, **kwargs):
        self.url = kwargs.pop('url')
        self.method = kwargs.pop('method')
        self.cache = kwargs.pop('cache_obj')
        temp_dict = kwargs.get('formdata', None)
        if temp_dict:
            self.formdata = [(k, v) for k, v in temp_dict.iteritems()]
        self.headers = kwargs.get('headers', None)
        self.cookieJar = kwargs.get('cookieJar', None)

class response_obj(object):
    #__slots__ = ('_response_string', '_cookie')
    _response_string = None
    _cookie = None

    def __init__(self):
        pass

    @property
    def response_string(self):
        return self._response_string

    @response_string.setter
    def response_string(self, value):
        self._response_string = value

    @property
    def cookie(self):
        return self._cookie
    @cookie.setter
    def cookie(self, value):
        self._cookie = value


