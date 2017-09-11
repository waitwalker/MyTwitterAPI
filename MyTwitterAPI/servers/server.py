import tornado.web
import tornado.options
import tornado.ioloop
import tornado.httpserver
from tornado.web import RequestHandler,url
from tornado.options import define,options
from urls import url
from models import users


define('port',type=int,default=8000,help='server port')

class IndexHandler(RequestHandler):

    def get(self, *args, **kwargs):


        self.write('get 请求')

    def post(self, *args, **kwargs):

        self.write('post 请求')


if __name__ == '__main__':
    tornado.options.parse_command_line()

    app = tornado.web.Application(
        url.handlers
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()