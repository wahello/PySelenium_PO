#-*- coding: utf-8 -*-

__author__ = 'ray'
from selenium import webdriver
import unittest
import time

class modolwindowdemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://pyselenium-d1826.coding.io/exapage.html"
        self.verificationErrors = []
        self.js = "setTimeout(function(){document.getElementsByTagName('Button')[3].click()},100);"

        
    def test_demo(self):
        driver = self.driver
        driver.get(self.base_url)
        #获取当前窗口句柄
        mainhandle = driver.current_window_handle
        print mainhandle
        #使用下面的webdriver打开模态窗口，无法进行切换
        #driver.find_element_by_xpath("//button[2]").click()

        #使用js异步进行打开模态窗口
        driver.execute_script(self.js)
        time.sleep(1)
        #获取当前所有句柄
        modalhandle = driver.window_handles

        #通过循环切换到模态窗口
        print modalhandle
        for handle in modalhandle:
            if handle != mainhandle:
                driver.switch_to_window(handle)
                print driver.current_window_handle
                driver.find_element_by_xpath("//form//tr[1]/td[2]/input").send_keys("Ray")

        time.sleep(2)
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()