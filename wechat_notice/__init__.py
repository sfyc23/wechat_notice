# -*- coding: utf-8 -*-
"""
Project: wechat-notice
Creator: DoubleThunder
Create time: 2019-10-06 03:06
Introduction:
"""

# from wechat_notice.core import (
#     wubi, single_wubi, conbin_wubi
# )

__title__ = 'wechat_notice'
__version__ = '0.0.1'
__author__ = 'sfyc23'
__license__ = 'MIT'
__copyright__ = '''
MIT License

Copyright (c) 2019 Thunder Bouble

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''


class WechatNotice(object):
    return_success = {'isSuccess': True, 'msg': ''}
    return_fail = {'isSuccess': False, 'msg': '未知'}

    def send(self, title, content, receivers):
        raise NotImplementedError()

    def __getitem__(self, id):
        return self.get(id)

    def __setitem__(self, id, session):
        self.set(id, session)

    def __delitem__(self, id):
        self.delete(id)
