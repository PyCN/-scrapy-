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
    __slots__ = ('url', 'method', 'cache','formdata', 'headers', 'use_cookie')

    def __init__(self, **kwargs):
        self.url = kwargs.pop('url')
        self.method = kwargs.pop('method')
        self.cache = kwargs.pop('cache_obj')
        temp_dict = kwargs.get('formdata', None)
        if temp_dict:
            self.formdata = [(k, v) for k, v in temp_dict.iteritems()]
        self.headers = kwargs.get('headers', None)
        self.use_cookie = kwargs.get('use_cookie', None)

class response_obj(object):
    __slots__ = ('text', 'cookie')

    def __init__(self, response_str = None, cookie = None):
        self.response_string = response_str
        self.cookie = cookie

    @property
    def text(self):
        return self.string
    @text.setter
    def text(self, value):
        if not isinstance(value, str):
            raise 'response_obj type error!!'
        self.response_string = value

    @property
    def cookie(self):
        return self.cookie
    @cookie.setter
    def cookie(self, value):
        self.cookie = value


