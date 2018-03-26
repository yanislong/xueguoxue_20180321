#!/usr/bin/python
# -*- coding=utf-8 -*-

import time
import sys
from appium import webdriver
import subprocess
import threading

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
        self.desired_caps['unicodeKeyboard'] = True
        self.desired_caps['resetKeyboard'] = True
        self.dd = webdriver.Remote("http://172.16.20.202:4723/wd/hub", self.desired_caps)
        return self.dd

    def getSize(self):
        x = self.dd.get_window_size()['width']
        y = self.dd.get_window_size()['height']
        return (x, y)

    def swipeDown(self,t):
        l = self.getSize()
        print l
        x1 = int(l[0] * 0.5)  #x坐标
        y1 = int(l[1] * 0.75)   #起始y坐标
        y2 = int(l[1] * 0.25)   #终点y坐标
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

    def double_click(self):
        self.dd.find_element_by_name('10').click()
        

    def search(self,text=""):
        self.dd.find_element_by_name(u'首页').click()
        self.dd.find_element_by_id('index_search_layout').click()
        tl = []
        for j in range(5):
            t = threading.Thread(target=self.double_click,args=())
            tl.append(t)
        for l in tl:
            l.start()
        sys.exit()
        self.dd.find_element_by_id('searchView').send_keys(text)
        sll = "adb shell ime set com.google.android.inputmethod.pinyin/.PinyinIME" 
        pi = subprocess.Popen(sll,shell=True,stdout=subprocess.PIPE)
        print pi.stdout.read()
        pi = subprocess.Popen("adb shell top -m 10 -n 1",shell=True,stdout=subprocess.PIPE)
        print pi.stdout.read()
        p2 = subprocess.Popen("adb shell ps|grep com.wwkj",shell=True,stdout=subprocess.PIPE)
        print p2.stdout.read()
        p2 = subprocess.Popen("adb shell su 0;procrank",shell=True,stdout=subprocess.PIPE)
        print p2.stdout.read()
        self.dd.find_element_by_id('searchView').click()
    #   self.dd.keyevent(AndroidKeyCode.ENTER)
        self.dd.keyevent(66)
        try:
            self.dd.find_element_by_name(u'首页').click()
        except:
            self.dd.find_element_by_id('search_back').click()

    def grade(self):
        g = [u"全部","幼儿蒙学","小学初段","小学中段","小学高段","初中国学","高中国学","成人国学"]
        for i in g:
            print i
            try:
                self.dd.find_element_by_name(u'首页').click()
            except:# NoSuchElementException:
                self.dd.find_element_by_id('subject_back').click()           
            self.dd.find_element_by_name(i).click()

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
    #test.menu()
    for i in range(1):
        test.search(i) # olny windows run
    #test.grade()
    print time.time()
