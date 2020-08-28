from selenium.webdriver.common.by import By

from test_homework_import_dept.page.add_member import AddMember
from test_homework_import_dept.page.basepage import BasePage
from test_homework_import_dept.page.contact import Contact


class Main(BasePage):

    def goto_add_member(self):
        #点击跳转页面
        #driver是从BasePage中继承而来的，继承后可以用父类的方法和属性
        self.find(By.CSS_SELECTOR,".ww_indexImg_AddMember").click()
        return AddMember(self.driver)

    def goto_contact(self):
        self.find(By.ID,"menu_contacts").click()
        return Contact(self.driver)

