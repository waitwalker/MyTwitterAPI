# -*- coding: utf-8 -*-
# @Time    : 17/10/23 下午9:16
# @Author  : waitWalker
# @Email   : waitwalker@163.com
# @File    : push_twitter_handler.py
# @Software: PyCharm


from handlers import base_handler
from models import users
import json

class PushTwitterHandler(base_handler.BaseHandler):

    def get(self, *args, **kwargs):
        self.write("发推成功")

    def post(self, *args, **kwargs):
        retwitterType = self.get_argument("retwitterType")
        retwitterAccount = self.get_argument("retwitterAccount")
        avatarImage = self.get_argument("avatarImage")
        account = self.get_argument("account")
        nickName = self.get_argument("nickName")
        time = self.get_argument("time")
        content = self.get_argument("content")
        contentImages = self.get_argument("contentImages")
        contentVideo = self.get_argument("contentVideo")
        commentCount = self.get_argument("commentCount")
        retwitterCount = self.get_argument("retwitterCount")
        likeCount = self.get_argument("likeCount")
        privateMessageCount = self.get_argument("privateMessageCount")

        new_twitter = users.HomeTwitterList()
        new_twitter.retwitterType = retwitterType
        new_twitter.retwitterAccount = retwitterAccount
        new_twitter.avatarImage = avatarImage
        new_twitter.account = account
        new_twitter.nickName = nickName
        new_twitter.time = time
        new_twitter.content = content
        new_twitter.contentImages = contentImages
        new_twitter.contentVideo = contentVideo
        new_twitter.commentCount = commentCount
        new_twitter.retwitterCount = retwitterCount
        new_twitter.likeCount = likeCount
        new_twitter.privateMessageCount = privateMessageCount

        self.db.add(new_twitter)
        self.db.commit()
        reponseObj ={
            "result":"200",
            "msg":"发推成",
            "data":""
        }
        self.write(json.dumps(reponseObj))
