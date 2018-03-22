#!/usr/bin/python
# -*- coding=utf-8 -*-

import time
import sys
from appium import webdriver

def login(name,passwd):
    desired_caps = {}
    desired_caps['platformName'] = "Android"
    desired_caps['platformVersion'] = "4.4.4"
    desired_caps['deviceName'] = "MI3"
    desired_caps['appPackage'] = "com.wwkj.xueguoxue"
    desired_caps['appActivity'] = ".view.MainActivity"
    dd = webdriver.Remote("http://172.16.20.202:4723/wd/hub", desired_caps)
    time.sleep(6)
    try:
        dd.find_element_by_id('index_login').click()
        time.sleep(3)
    except:
        print "error or login over"
        dd.quit()
    finally:
        pass
    dd.find_element_by_id('login_phone_input').send_keys(name)
    dd.find_element_by_id("login_password_input").send_keys(passwd)
    dd.find_element_by_id('login_button').click()

def menu():
    dd.find_element_by_id(u'首页').click()
    dd.find_element_by_id(u'选课').click()
    dd.find_element_by_id(u'学习').click()
    dd.find_element_by_id(u'消息').click()
    dd.find_element_by_id(u'我的').click()

if __name__ == "__main__":
    n = "13141032576"
    p = "lihailong123"
    login(n,p)
