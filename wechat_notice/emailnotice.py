# -*- coding: utf-8 -*-
"""
Project: HelloWorldPython
Creator: DoubleThunder
Create time: 2019-10-6 03:14
Introduction:
"""
from wechat_notice import WechatNotice
import yagmail


class EmailNotice(WechatNotice):
    """
    notice = EmailNotice(user="token", password='',
                                host='',to_emails=['1@163.com','2@qq.com'])
    notice.send('title','content')
    你需要安装 yagmail 才能使用
    """

    def __init__(self, user, password, host, to_emails=None):
        self.mail_conn = yagmail.SMTP(user=user, password=password, host=host)
        if to_emails:
            self.to_emails = to_emails

    def send(self, title='', content='', receivers=None):
        """
        :param title: str, 消息标题，最长为 256，必填。
        :param content: str, 消息内容，最长 64 Kb，可空，支持 MarkDown。
        :return: bool, True 发送成功；False,发送成功。
        """
        if receivers:
            to_receivers = receivers
        elif self.to_emails:
            to_receivers = self.to_emails
        else:
            self.return_fail['msg'] = '请输入要发送的邮箱'
            return self.return_fail

        try:
            self.mail_conn.send(to_receivers, title, content)
            return self.return_success
        except Exception as exception:
            # print(str(exception))
            self.return_fail['msg'] = str(exception)
            return self.return_fail


if __name__ == '__main__':
    email_user = 'sfyc23@qq.com'
    email_password = 'yxayleefbersbjeg'
    email_host = 'smtp.qq.com'
    to_emails = ['doublethunder@qq.com', 'doublethunder23@qq.com']
    notice = EmailNotice(user=email_user, password=email_password, host=email_host, to_emails=to_emails)
    yy = notice.send('title', 'content')
    print(yy)
