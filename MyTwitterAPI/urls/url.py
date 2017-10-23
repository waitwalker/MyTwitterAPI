# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 上午11:09
# @Author  : waitWalker
# @Email   : waitwalker@163.com
# @File    : test.py
# @Software: PyCharm

from handlers import index_handler,register_handler,about_handler,home_handler,login_handler,push_twitter_handler

handlers = [
    (r'/index/',index_handler.IndexHandler),
    (r'/register/',register_handler.RegisterHandler),
    (r'/about/',about_handler.AboutHandler),
    (r'/getHomeTwitterList/',home_handler.HomeHandler),
    (r'/login/',login_handler.LoginHandler),
    (r'/pushNewTwitter/',push_twitter_handler.PushTwitterHandler),
]
