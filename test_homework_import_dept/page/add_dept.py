import time

from selenium.webdriver.common.by import By

from test_homework_import_dept.page.basepage import BasePage



class AddDept(BasePage):

    def add_dept(self,dept_name):
        # 填写部门名称
        self.find(By.NAME,"name").send_keys(dept_name)
        # 选择所属部门
        self.find(By.CSS_SELECTOR,".js_toggle_party_list").click()
        # 点击根节点的部门
        self.find(By.XPATH,"//div[@id='__dialog__MNDialog__']//a[@id='1688854035661665_anchor']").click()
        # 点击确定按钮
        self.find(By.CSS_SELECTOR,".ww_dialog_foot .ww_btn_Blue").click()
        # 等待新建部门成功的提示出现后再进行断言
        ele = (By.XPATH, "//div[text()='新建部门成功']")
        self.wait_for_visible(ele)

        from test_homework_import_dept.page.contact import Contact
        # 返回对应部门的联系人页面
        return Contact(self.driver)
