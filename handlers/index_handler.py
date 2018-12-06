# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 上午11:09
# @Author  : waitWalker
# @Email   : waitwalker@163.com
# @File    : test.py
# @Software: PyCharm
from handlers import base_handler
from models import users

class IndexHandler(base_handler.BaseHandler):

    def get(self, *args, **kwargs):

        # user = users.User.by_id(users.User,1)
        # print(user.user_name,user.password)
        #
        # self.write('index get 请求')

        user = users.User.by_phone_num(users.User, 123456)
        if user:
            print('用户已存在')
            print(user.user_name, user.password)

            self.write('index get 请求')
        else:
            print('用户不存在')
            self.write('用户不存在')