import requests
import time
import re
import configparser
import subprocess

class login(object):
    every = 15    # 设置检测间隔时间，单位为秒


    def __init__(self):
        self.login_url = "输入在这" # 验证页面网址，F12控制台可找到，以及以下所有内容都在F12控制台中
        self.headers = {
            'POST': '输入在这',
            'Host': '输入在这',
            'Accept-Language': '输入在这',
            'Connection': '输入在这',
            'Content-Length': '输入在这',
            'Cache - Control': '输入在这',
            'Origin': '输入在这',
            'Upgrade - Insecure - Requests': '输入在这',
            'Content-Type': '输入在这',
            'Accept': '输入在这',
            'Referer': '输入在这',
            'User-Agent': '输入在这',
            'Accept-Encoding': '输入在这',
            'Cookie': '输入在这'
        }     # 从F12控制台获取的header
        self.payload = {
            'DDDDD': '输入在这',
            "upass": '输入在这',
            "R1": '0',
            "R2": '0',
            'R3': '0',
            'R6': '0',
            'para': '00',
            '0MKKey': '输入在这',
            'buttonClicked':'',
            'redirect_url':'',
            'err_flag':'',
            'username':'',
            'password':'',
            'user':'',
            'cmd':'',
            'Login':''
        }    # 从F12控制台获取的playload
        self.every = login.every  # 检测间隔时间，单位为秒

    def login(self):
        try:
            requests.post(self.login_url, headers=self.headers, data=self.payload)
            if self.canConnect() is False:
                print("连接失败，请检查网络环境或账号密码")
            else:
                print(self.getCurrentTime(),u"网络连接成功")
        except Exception as e:
            print("some errors")
            print(str(e))

    def canConnect(self):
        try:
            q = requests.get("http://www.baidu.com", timeout=5)
            m = re.search(r'STATUS OK', q.text)
            if m:
                return True
            else:
                return False
        except Exception as conE:
            return False

    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

    def main(self):
        print(self.getCurrentTime(), u"Hi，欢迎使用自动登陆系统")
        while True:
            self.login()
            while True:
                can_connect = self.canConnect()
                if not can_connect:
                    print(self.getCurrentTime(), u"断网了...")
                    self.login()
                else:
                    print(self.getCurrentTime(), u"一切正常...")
                time.sleep(self.every)
            time.sleep(self.every)

if __name__ == '__main__':
    logins = login()
    logins.main()
