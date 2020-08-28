import time
from selenium.webdriver.common.by import By

from test_homework_import_dept.page.basepage import BasePage
from test_homework_import_dept.page.contact import Contact


class AddMember(BasePage):

    def add_member(self):
        time.sleep(3)
        #添加成员，需要输入姓名
        self.find(By.ID,"username").send_keys("庄周13")
        #账号
        self.find(By.ID,"memberAdd_acctid").send_keys("zhuagnzhou13")
        #手机号
        self.find(By.ID,"memberAdd_phone").send_keys("13509999994")
        #点击保存，return到通讯录页面
        self.find(By.LINK_TEXT,"保存").click()
        return Contact(self.driver)

    def add_member_fail(self):
        # 添加成员，需要输入姓名
        self.find(By.ID, "username").send_keys("若晴")
        # 账号
        self.find(By.ID, "memberAdd_acctid").send_keys("ruoqing")
        # 手机号
        self.find(By.ID, "memberAdd_phone").send_keys("13509999999")
        # 点击保存，return到通讯录页面
        self.find(By.LINK_TEXT, "保存").click()
        return Contact(self.driver)
