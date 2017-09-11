from handlers import base_handler
from models import users

class RegisterHandler(base_handler.BaseHandler):

    def post(self, *args, **kwargs):

        phone_num = self.get_argument('phone_num')
        user_name = self.get_argument('user_name')
        password = self.get_argument('password')
        user = users.User.by_id(users.User,phone_num)
