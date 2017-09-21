from tornado.web import RequestHandler
from models import session
import json

class BaseHandler(RequestHandler):

    def prepare(self):
        pass


    def write_error(self, status_code, **kwargs):

        print('status_code',status_code)

        if status_code == 400:
            self.write(json.dumps("400 错误 参数不正确"))
        elif status_code == 404:
            self.write(json.dumps("页面找不到"))
        else:
            self.write(json.dumps('错误类型未知'))

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