# -*- coding: utf-8 -*-
"""
Project: wechat-notice
Creator: DoubleThunder
Create time: 2019-10-06 00:33
Introduction:
"""
from wechat_notice import WechatNotice
import requests


class ServerChanNotice(WechatNotice):
    """
    Server 酱 ——「程序员」和「服务器」之间的通信软件。(一对多：PushBear)
    官网：http://sc.ftqq.com/3.version
    使用：
    notice = ServerChanNotice(sckey='你申请的sckey')
    yy = notice.set('这是一个标题','这是内容')
    需要安装 requests 才可使用。
    """

    base_url = 'https://sc.ftqq.com/{sckey}.send'

    def __init__(self, sckey=None):
        if sckey:
            self.url = self.base_url.format(sckey=sckey)

    def set(self, title='', content='', receivers=''):
        """
        :param title: str, 消息标题，最长为 256，必填。
        :param content: str, 消息内容，最长 64 Kb，可空，支持 MarkDown。
        :param receivers: str ,（可空）需要发送的 sckey。如果初始化时有定义，则不需要填写
        :return: {'isSuccess': False, 'msg': '错误原因'}
        """
        if receivers:
            send_url = self.base_url.format(sckey=receivers)
        elif self.url:
            send_url = self.url
        else:
            self.return_fail['msg'] = 'sckey 不能为空！'
            return self.return_fail

        if not title or not title.strip():
            title = '无标题'

        elif len(title) >= 256:
            title = title[:256]
        payload = {'text': title, 'desp': content}
        try:
            resp = requests.get(send_url, params=payload)
            if resp.status_code == 200:
                # print(resp.text)
                content_dict = resp.json()
                if content_dict['errno'] == 0:
                    # print('发送成功')
                    return self.return_success
                else:
                    self.return_fail['msg'] = content_dict['errmsg']
                    return self.return_fail
            self.return_fail['msg'] = '网络请求失败'
            return self.return_fail
        except Exception as exception:
            self.return_fail['msg'] = str(exception)
            return self.return_fail

