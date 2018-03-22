#!/usr/bin/python
# -*- coding=utf-8 -*-

import time
import sys
from appium import webdriver

class apptest():
    def __init__(self):
        self.dd = self.MO()

    def MO(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = "Android"
        self.desired_caps['platformVersion'] = "4.4.4"
        self.desired_caps['deviceName'] = "MI3"
        self.desired_caps['appPackage'] = "com.wwkj.xueguoxue"
        self.desired_caps['appActivity'] = ".view.MainActivity"
        self.dd = webdriver.Remote("http://172.16.20.202:4723/wd/hub", self.desired_caps)
        return self.dd

    def login(self,name,passwd):
        try:
            self.dd.find_element_by_id('index_login').click()
            time.sleep(3)
        except:
            print "error or login over"
            print "progarm is exit"
            self.dd.quit()
            sys.exit()
        finally:
            pass
        self.dd.find_element_by_id('login_phone_input').send_keys(name)
        self.dd.find_element_by_id("login_password_input").send_keys(passwd)
        self.dd.find_element_by_id('login_button').click()
        time.sleep(3)

    def menu(self):
        self.dd.find_element_by_name(u'首页').click()
        time.sleep(2)
        self.dd.find_element_by_name(u'选课').click()
        self.dd.find_element_by_name(u'学习').click()
        self.dd.find_element_by_name(u'消息').click()
        self.dd.find_element_by_name(u'我的').click()
        self.dd.find_element_by_id('logout_button').click()

    def logout(self):
        self.dd.find_element_by_name(u'我的').click()
        print "click logout"
        #self.dd.find_element_by_name('').click()
        #self.dd.find_element_by_id('logout_button').click()

    def __del__(self):
        self.logout()

if __name__ == "__main__":
    n = "13141032576"
    p = "lihailong123"
    test = apptest()
    #test.login(n,p)
    test.menu()
