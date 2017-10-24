# -*- coding: utf-8 -*-
# @Time    : 2017/10/23 上午11:07
# @Author  : waitWalker
# @Email   : waitwalker@163.com
# @File    : home_handler.py
# @Software: PyCharm

from handlers import base_handler
from models import users
import json


class HomeHandler(base_handler.BaseHandler):

    def get(self, *args, **kwargs):

        homeList = users.HomeTwitterList.all(users.HomeTwitterList)
        print(homeList)
        if len(homeList) == 0:
            responseObject = {
                "result": "200",
                "msg": "请求成功,主页目前没有数据",
                "data": ""
            }
            self.write(json.dumps(responseObject))
        else:
            data = []
            for home in homeList:
                dic = {
                    "retwitterType": home.retwitterType,
                    "retwitterAccount": home.retwitterAccount,
                    "avatarImage": home.avatarImage,
                    "account": home.account,
                    "nickName": home.nickName,
                    "time": home.time,
                    "content": home.content,
                    "contentImages": home.contentImages,
                    "contentVideo": home.contentVideo,
                    "commentCount": home.commentCount,
                    "retwitterCount": home.retwitterCount,
                    "likeCount": home.likeCount,
                    "privateMessageCount": home.privateMessageCount,
                }

                data.insert(0,dic)
            print(data)

            responseObject = {
                "result":"200",
                "msg":"请求成功",
                "data":data
            }
            self.write(json.dumps(responseObject))
