# -*- coding: utf-8 -*-
# @Time    : 2017/9/29 上午11:09
# @Author  : waitWalker
# @Email   : waitwalker@163.com
# @File    : test.py
# @Software: PyCharm

from handlers import base_handler
from models import abouts
import json

class AboutHandler(base_handler.BaseHandler):

    def get(self, *args, **kwargs):

        aboutList = abouts.AboutTwitter.all(abouts.AboutTwitter)
        print("aboutList:",aboutList)

        if len(aboutList) == 0:

            print("来到这里了")
            data = [
                {
                    "title":u"版本",
                    "urlString":"http://www.baidu.com",
                    "type":"0",
                    "subType":"0"
                },
                {
                    "title":u"发送崩溃报告",
                    "urlString":"http://www.baidu.com",
                    "type":"1",
                    "subType":"0"
                },
                {
                    "title":u"帮助中心",
                    "urlString":"http://www.baidu.com",
                    "type":"1",
                    "subType":"1"
                },
                {
                    "title":u"服务条款",
                    "urlString":"http://www.baidu.com",
                    "type":"2",
                    "subType":"0"
                },
                {
                    "title":u"隐私政策",
                    "urlString":"http://www.baidu.com",
                    "type":"2",
                    "subType":"1"
                },
                {
                    "title":u"Cookie 使用政策",
                    "urlString":"http://www.baidu.com",
                    "type":"2",
                    "subType":"2"
                },
                {
                    "title":u"法律声明",
                    "urlString":"http://www.baidu.com",
                    "type":"2",
                    "subType":"3"
                }
            ]
            for item in data:
                newAbout = abouts.AboutTwitter()


                newAbout.title = item["title"]

                newAbout.urlString = item["urlString"]
                newAbout.type = str(item["type"])
                newAbout.subType = str(item["subType"])
                self.db.add(newAbout)
                self.db.commit()

            responseObject = {
                "result":"200",
                "msg":"成功",
                "data":data
            }

            self.write(json.dumps(responseObject))
        else:
            data = []
            for about in aboutList:
                dic = {
                    "title": about.title,
                    "urlString": about.urlString,
                    "type": about.type,
                    "subType": about.subType
                }

                data.append(dic)
                print(data)

            responseObject = {
                "result": "200",
                "msg": "成功",
                "data": data
            }
            self.write(json.dumps(responseObject))