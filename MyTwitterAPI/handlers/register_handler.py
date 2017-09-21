from handlers import base_handler
from models import users
import json

class RegisterHandler(base_handler.BaseHandler):

    def post(self, *args, **kwargs):
        user_name = self.get_argument('user_name')
        password = self.get_argument('password')
        email = self.get_argument('email')
        phone = self.get_argument('phone')
        user = users.User.by_email(users.User,email)
        if user:
            print('用户已存在')

            new_user = users.User()
            new_user.user_name = user_name
            new_user.password = password
            new_user.email = email
            # self.db.add(new_user)
            # self.db.commit()
            data = {
                "user_name": user_name,
                "email": email
            }

            registerSuccess = {'responseObject':
                                   {"data": data,
                                    "result": "1",
                                    "msg": '注册成功'
                                    }
                               }

            registerSuccess = json.dumps(registerSuccess)

            self.write(json.dumps(registerSuccess))
        else:
            print('用户不存在,把新增用户添加到数据库')
            new_user = users.User()
            new_user.user_name = user_name
            new_user.password = password
            new_user.email = email
            # self.db.add(new_user)
            # self.db.commit()
            data = {
                "user_name":user_name,
                "email":email
            }

            registerSuccess = {'responseObject':
                                   {"data":data,
                                    "result":"1",
                                    "msg":'注册成功'
                                    }
                               }

            registerSuccess = json.dumps(registerSuccess)

            self.write(registerSuccess)


    def getResponseObejct(self,result,msg,*args):

        responseObject = {
            'responseObject':{
                'result':result,
                'msg':msg,
                'data': args,
            }
        }
        return responseObject
