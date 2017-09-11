from handlers import base_handler
from models import users

class IndexHandler(base_handler.BaseHandler):

    def get(self, *args, **kwargs):

        user = users.User()
        user.user_name = 'aixuepai'
        user.password = 'a11111'
        self.db.add(user)
        self.db.commit()

        self.write('index get 请求')
