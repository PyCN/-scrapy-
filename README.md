
# -scrapy-
流程图

![image](https://github.com/PyCN/-scrapy-/blob/master/image/image1.png)
这几天工作任务轻松一点了，重新完善这个项目。前段时间学习了flask的源码，个人觉得flask的设计模式很好，我参照flask的设计模式，重新写了一遍引擎部分代码。

***
**2017.1.22更新**
* 今天测试了一下框架可以基本工作了，虽然还有很多功能没有完善，后面会逐步加上的。
* 这个小框架只使用了lxml的第三方库，本来想使用request库的，后来觉得还是尽量减少第三库的依赖就去掉了。
* 本人学习python时间不长，对很多东西理解不深刻，还请各位大佬多多指教。
***
* 下面是基本的使用教程

1.首先介绍一下整个代码的组织结构

```
MyScrapy
|
|----src
|     |
|     MyScrapy.py
|
|
```
* 整个工程都包含在MyScrapy这个目录下面，MyScrapy的根目录下面放置的工程的源代码，src目录下的MyScrapy文件是需要使用这自己编写的。

2.MyScrapy.py文件的编写

```python
from myScrapy import Myscrapy
from myScrapy import Request

app = Myscrapy(__name__)

class test(object):
    def start_request(self):
        yield Request(url = 'http://www.baidu.com/', method = 'GET', callback = self.deal_response)

    def deal_response(self, response):
        print response.xpath("//head/title")[0].text

app.run(execute_app = test())
```
* 这是一个最基本的实例，首先需要导入两个基本的类，Myscrapy和Request。
* 将Myscrapy实例化`app = Myscrapy(__name__)`,这里可以传入一个参数是，是当前爬虫的名字。
* 下面编写一个执行的类，类必须有一个`def start_request`方法，名字不能变。这个方法返回一个Request()实例，上述例子展示了基本用法。但是如果是`POST`方法，增加一个formdata参数用来提交表单`yield Request(url = 'http://www.baidu.com/', method = 'post', formdata = {xxxxx},callback = self.deal_response)`, callback的参数是接受一个函数，来用作返回消息值的回调。
* 等请求提交之后，回返回服务器的相应结果，通过`deal_response`的response参数传入，response参数已经用lxml处理过了，可以直接使用`xpath()`方法来解析，获得相应的结果。
* `app.run()`是爬虫启动指令,接受刚才编写的类的实例
