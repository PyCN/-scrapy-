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
    __slots__ = ('url', 'method', 'cache','formdata')

    def __init__(self, **kwargs):
        self.url = kwargs.pop('url')
        self.method = kwargs.pop('method')
        self.cache = kwargs.pop('cache_obj')
        temp_dict = kwargs.pop('formdata') if kwargs.pop('formdata') else None
        self.formdata = [(k, v) for k, v in temp_dict.iteritems()]