from handlers import base_handler
from models import users

class RegisterHandler(base_handler.BaseHandler):

    def post(self, *args, **kwargs):

        # phone_num = self.get_argument('phone_num')
        # user_name = self.get_argument('user_name')
        # password = self.get_argument('password')
        user = users.User.by_id(users.User,1235)
        if user:
            print('手机号已存在')
            self.write('号码已存在,请换另一个试试')
        else:
            print('手机号不存在,把新增用户添加到数据库')
            # new_user = users.User()
            # new_user.phone_num = phone_num
            # new_user.user_name = user_name
            # new_user.password = password
            # self.db.add(new_user)
            # self.db.commit()
            self.write('注册成功')