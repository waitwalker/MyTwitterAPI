# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 上午11:09
# @Author  : waitWalker
# @Email   : waitwalker@163.com
# @File    : test.py
# @Software: PyCharm

import tornado.web
import tornado.options
import tornado.ioloop
import tornado.httpserver
from tornado.web import RequestHandler,url
from tornado.options import define,options
from urls import url
from models import users
from models import create_tables


define('port',type=int,default=8000,help='server port')
define('tables',type=bool,default=False,group='application',help='create tables')

class Application(tornado.web.Application):
    def __init__(self,*args,**kwargs):
        super(Application,self).__init__(*args,**kwargs)

def main():
    tornado.options.parse_command_line()
    if options.tables == False:
        create_tables.run()

    app = Application(
        url.handlers,

    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()