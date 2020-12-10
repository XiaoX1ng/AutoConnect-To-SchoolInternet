import requests
import time
import re
import configparser
import subprocess

class login(object):
    every = 15    # 设置检测间隔时间，单位为秒


    def __init__(self):
        self.login_url = "http://10.10.10.102:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=10.10.10.102&iTermType=1&wlanuserip=10.60.239.40&mac=3c-15-fb-a9-9f-3b&ip=10.60.239.40&enAdvert=0&queryACIP=0&loginMethod=1"
        self.headers = {
            'POST': '/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=10.10.10.102&iTermType=1&wlanuserip=10.60.239.40&mac=3c-15-fb-a9-9f-3b&ip=10.60.239.40&enAdvert=0&queryACIP=0&loginMethod=1 HTTP/1.1',
            'Host': '10.10.10.102:801',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '170',
            'Cache - Control': 'max - age = 0',
            'Origin': 'http: // 10.10.10.102',
            'Upgrade - Insecure - Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'text/html,application/xhtml+xml,application /xml;q = 0.9,image/webp,image/apng,*/*;q = 0.8,application/signed-exchange;v = b3',
            'Referer': 'http://10.10.10.102/a70.htm?wlanuserip=10.60.239.40&wlanacname=',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate',
            'Cookie': 'program=0626; vlan=202; ip=10.60.239.40; ISP_select=@liantong; md5_login2=%2C0%2C111902040126@liantong%7Cxx320582; PHPSESSID=cqoupsmm430084duatqmpf6f16'
        }     # 从F12控制台获取的header
        self.payload = {
            'DDDDD': ',0,111902040126@liantong',
            "upass": 'xx320582',
            "R1": '0',
            "R2": '0',
            'R3': '0',
            'R6': '0',
            'para': '00',
            '0MKKey': '123456',
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
