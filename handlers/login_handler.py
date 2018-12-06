# -*- coding: utf-8 -*-
# @Time    : 2017/10/23 下午3:45
# @Author  : waitWalker
# @Email   : waitwalker@163.com
# @File    : login_handler.py
# @Software: PyCharm
from handlers import base_handler
import json
from models import users



class LoginHandler(base_handler.BaseHandler):

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        email = self.get_argument('email')
        user = users.User.by_email(users.User, email)
        email = self.get_argument('email')
        if user:
            print('登录成功')
            loginSuccess = {'responseObject':
                                   {"data": "",
                                    "result": "1",
                                    "msg": '登录成功'
                                    }
                               }
            self.write(json.dumps(loginSuccess))
        else:
            print('登录失败')
            loginFailure = {'responseObject':
                                {"data": "",
                                 "result": "-1",
                                 "msg": '登录失败,用户或者密码错误'
                                 }
                            }
            self.write(json.dumps(loginFailure))