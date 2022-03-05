from selenium import webdriver
from datetime import date
from time import sleep
import tkinter
# 导入消息对话框子模块
import tkinter.messagebox
class Student(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def submit_form(self):
        driver = webdriver.Chrome('E:/hope/打卡/chromedriver.exe')
        #打卡网站
        driver.get('http://ids.hhu.edu.cn/amserver/UI/Login?goto=http://form.hhu.edu.cn/pdc/form/list')

        # 登录
        sleep(1)
        driver.find_element_by_id('IDToken1').send_keys(self.username)
        driver.find_element_by_id('IDToken2').send_keys(self.password)
        sleep(1)
        driver.find_element_by_xpath('//*[@onclick="defaultSubmit()"]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@class="datav-flex-box"]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="saveBtn"]').click()
        sleep(1)
        driver.quit()

        ##您的(账号   ， 密码)
Student("********", "***********").submit_form()
Student("*********", "*********").submit_form()
sleep(3)
tkinter.messagebox.showinfo('提示','健康打卡成功')