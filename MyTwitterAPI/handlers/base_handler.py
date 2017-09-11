from tornado.web import RequestHandler
from models import session

class BaseHandler(RequestHandler):

    def prepare(self):
        pass

    def write_error(self, status_code, **kwargs):
        pass

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