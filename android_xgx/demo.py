#!/usr/bin/python
# -*- coding=utf-8 -*-

import time
import sys
from appium import webdriver

#获得机器屏幕大小x,y
'''
def getSize():
    x = dr.get_window_size()['width']
    y = dr.get_window_size()['height']
    return (x, y)
 
#屏幕向上滑动
def swipeUp(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.75)   #起始y坐标
    y2 = int(l[1] * 0.25)   #终点y坐标
    dr.swipe(x1, y1, x1, y2,t)
#屏幕向下滑动
def swipeDown(t):
    l = getSize()
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.25)   #起始y坐标
    y2 = int(l[1] * 0.75)   #终点y坐标
    dr.swipe(x1, y1, x1, y2,t)
#屏幕向左滑动
def swipLeft(t):
    l=getSize()
    x1=int(l[0]*0.75)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.05)
    dr.swipe(x1,y1,x2,y1,t)
#屏幕向右滑动
def swipRight(t):
    l=getSize()
    x1=int(l[0]*0.05)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.75)
    dr.swipe(x1,y1,x2,y1,t)
'''

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

    def getSize(self):
        x = self.dd.get_window_size()['width']
        y = self.dd.get_window_size()['height']
        return (x, y)

    def swipeDown(self,t):
        l = self.getSize()
        print l
        y1 = int(l[0] * 0.5)  #x坐标
        x1 = int(l[1] * 0.75)   #起始y坐标
        x2 = int(l[1] * 0.25)   #终点y坐标
        self.dd.swipe(x1, y1, x2, y1,t)

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
        self.dd.find_element_by_name(u'选课').click()
        self.dd.find_element_by_name(u'学习').click()
        self.dd.find_element_by_name(u'消息').click()
        self.dd.find_element_by_name(u'我的').click()

    def logout(self):
        self.dd.find_element_by_name(u'我的').click()
        self.dd.swipe(0.5,0.75,0.5,0.25)
        print "click logout"
        self.dd.find_element_by_id('logout_button').click()
        self.dd.find_element_by_id('right_button').click()

    def __del__(self):
        try:
            self.logout()
        except:
            print "user not login"

if __name__ == "__main__":
    n = "13141032576"
    p = "lihailong123"
    test = apptest()
    #test.login(n,p)
    test.menu()
