from handlers import base_handler
from models import users

class IndexHandler(base_handler.BaseHandler):

    def get(self, *args, **kwargs):

        user = users.User.by_id(users.User,1)
        print(user.user_name,user.password)

        self.write('index get 请求')
