# -*- coding: utf-8 -*-
# @Time    : 2017/10/23 上午11:07
# @Author  : waitWalker
# @Email   : waitwalker@163.com
# @File    : home_handler.py
# @Software: PyCharm

from handlers import base_handler
from models import users
import json

class HomeHandler(base_handler.BaseHandler):

    def get(self, *args, **kwargs):
        self.write("主页")


