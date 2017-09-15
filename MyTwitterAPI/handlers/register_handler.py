from handlers import base_handler
from models import users
import json

class RegisterHandler(base_handler.BaseHandler):

    def post(self, *args, **kwargs):

        # phone_num = self.get_argument('phone_num')
        # user_name = self.get_argument('user_name')
        # password = self.get_argument('password')
        user = users.User.by_id(users.User,1235)
        if user:
            print('手机号已存在')
            self.write(json.dumps('号码已存在,请换另一个试试'))
        else:
            print('手机号不存在,把新增用户添加到数据库')
            # new_user = users.User()
            # new_user.phone_num = phone_num
            # new_user.user_name = user_name
            # new_user.password = password
            # self.db.add(new_user)
            # self.db.commit()
            name = self.get_argument('name')

            registerSuccess = {'responseObject':
                                   {"data":
                                        {"name":name},
                                    "result":"1",
                                    "msg":'注册成功'
                                    }
                               }

            registerSuccess = json.dumps(registerSuccess)

            self.write(registerSuccess)