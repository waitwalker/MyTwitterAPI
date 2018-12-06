# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 上午11:09
# @Author  : waitWalker
# @Email   : waitwalker@163.com
# @File    : test.py
# @Software: PyCharm

from tornado.web import RequestHandler
from models import session
import json

class BaseHandler(RequestHandler):

    def prepare(self):
        pass


    def write_error(self, status_code, **kwargs):

        print('status_code',status_code)

        if status_code == 400:
            msg = '400 错误 参数不正确'
            responseObj = self.handle_msg(status_code=status_code, msg=msg)
            self.write(json.dumps(responseObj))
        elif status_code == 404:
            msg = '404 错误 页面不存在'
            responseObj = self.handle_msg(status_code=status_code,msg=msg)
            self.write(json.dumps(responseObj))
        else:
            msg = '错误类型未知'
            responseObj = self.handle_msg(status_code=status_code, msg=msg)
            self.write(json.dumps(responseObj))
            self.write(json.dumps(responseObj))

    def get(self, *args, **kwargs):
        pass

    def set_header(self, name, value):
        pass

    def post(self, *args, **kwargs):
        pass

    def initialize(self):
        self.db = session

    def on_finish(self):
        self.db.close()

    def handle_msg(self,status_code,msg):
        responseObject = {
            "data": "",
            "result": status_code,
            "msg":msg
        }
        return responseObject
