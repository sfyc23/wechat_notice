Send Wechat a message at any time.(任何时刻给微信发送消息)
=============================
[![pypi](https://img.shields.io/badge/pypi-0.0.3-yellow.svg)](https://pypi.org/project/wechat-notice/) 
![python_vesion](https://img.shields.io/badge/python-%3E3-green.svg)  

   
主要用于服务器与微信之间的通信。
实现方法：通过邮箱、公众号给微信发送消息。

## 关于

* GitHub: https://github.com/sfyc23/wechat_notice  
* License: MIT license  
* PyPI: https://pypi.org/project/wechat-notice/  
* Python version: 3

## 所使用的库

    requests
    yagmail

## 安装

    $ pip install wechat-notice

## 使用示例

1、 使用邮箱。    

需要微信绑定 『QQ邮箱提醒』。  
绑定方法：设置 -> 通用 -> 辅助功能 -> QQ邮箱提醒 。

```
from wechat_notcie import EmailNotice
notice = EmailNotice(user="token", password='',
                            host='',to_emails=['1@163.com','2@qq.com'])
notice.send('title','content')
```

2、使用 Server 酱。  

Server 酱官网：http://sc.ftqq.com/3.version。需要关注公众号并申请 sckey。  
```
from wechat_notcie import ServerChanNotice
notice = ServerChanNotice(sckey='你申请的sckey')
notice.send('这是一个标题','这是内容')
```

3、使用推了噜。  

面包多官网：https://m.niucodata.com/tui。需要关注公众号并申请 openid。    
```
from wechat_notcie import ServerChanNotice
notice = NiucodataChanNotice(openid='你申请的openid')
notice.send('这是一个标题','这是内容')
```



## Lincese

    MIT License
    
    Copyright (c) 2019 Thunder Bouble
    
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
