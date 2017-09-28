from handlers import base_handler
from models import abouts
import json

class AboutHandler(base_handler.BaseHandler):

    def get(self, *args, **kwargs):

        aboutList = abouts.AboutTwitter.all(abouts.AboutTwitter)
        print("aboutList:",aboutList)

        if aboutList == None:

            print("来到这里了")
            data = [
                {
                    "title":"版本",
                    "urlString":"http://www.baidu.com",
                    "type":"0",
                    "subType":"0"
                },
                {
                    "title":"发送崩溃报告",
                    "urlString":"http://www.baidu.com",
                    "type":"1",
                    "subType":"0"
                },
                {
                    "title":"帮助中心",
                    "urlString":"http://www.baidu.com",
                    "type":"1",
                    "subType":"1"
                },
                {
                    "title":"服务条款",
                    "urlString":"http://www.baidu.com",
                    "type":"2",
                    "subType":"0"
                },
                {
                    "title":"隐私政策",
                    "urlString":"http://www.baidu.com",
                    "type":"2",
                    "subType":"1"
                },
                {
                    "title":"Cookie 使用政策",
                    "urlString":"http://www.baidu.com",
                    "type":"2",
                    "subType":"2"
                },
                {
                    "title":"法律声明",
                    "urlString":"http://www.baidu.com",
                    "type":"2",
                    "subType":"3"
                }
            ]
            for item in data:
                print("item:",str(item["type"]))
                newAbout = abouts.AboutTwitter()
                newAbout.title = item["title"].encode('utf-8')
                print(newAbout.title)
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

            self.write("插入成功")
        else:
            
            self.write("有数据了")