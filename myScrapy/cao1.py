# class test(object):
#     def __init__(self, *args):
#         self.a = 1
#         print args
# class test1(object):
#     pass
# obj1 = test1()
# obj = test(obj1)
# import urllib2
#
# response = urllib2.urlopen('http://www.baidu.com/')
# print response.read()

# class test(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             orig = super(test, cls)
#             cls._a = orig.__new__(cls, *args, **kwargs)
#         return cls._a
#
# class MyClass(test):
#     a = 1
#
# one = MyClass()
# two = MyClass()
#
# two.a = 3

# class example(object):
#     pass
#
# example.a = 1
# obj = example()
# print example.a
# print obj.b

# def f(x):
#     return x + x
# print map(f, [1,2,3,4,5])
import cookielib
import urllib2

cookie = cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value