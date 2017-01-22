# class test(object):
#     def __init__(self, *args):
#         self.a = 1
#         print args
# class test1(object):
#     pass
# obj1 = test1()
# obj = test(obj1)
import urllib2

response = urllib2.urlopen('http://www.baidu.com/')
print response.read()