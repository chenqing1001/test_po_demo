import time

from selenium.webdriver.common.by import By

from test_homework_import_dept.page.add_dept import AddDept
from test_homework_import_dept.page.basepage import BasePage


class Contact(BasePage):

    def click_button(self):
        # 定义变量存储checkbox元素，这种定义是固定写法要传到expected_contidisons的element_to_be_clickable方法里
        ele =(By.CSS_SELECTOR,".ww_checkbox")
        self.wait_for_clickable(ele)
        self.find(By.CSS_SELECTOR,".ww_checkbox").click()

    def get_member(self):
        # 得到所有的成员信息
        list_all_name = []
        while True:
            # 获取分页信息,message获取到的是1/3格式的内容,1/3,2/3,3/3
            message:str = self.find(By.CSS_SELECTOR,".ww_pageNav_info_text").text
            # 获取当前页和总页数,message.split("/",1)返回的是("1","3")，所以需要强转为int类型
            cur_page, total_page =[int(i) for i in message.split("/",1)]
            member_list = self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)") #这个拿到的是elements
            # member_list返回的是element对象的集合，不是list，需要从element对象集合中获取每个element的title属性来进行后面的断言
            for member in member_list:
                list_all_name.append(member.get_attribute("title"))
            cur_page = [int(i) for i in message.split("/",1)][0] # 前面cur_page取过值了，这里可以不用重复取值
            #如果当前页和总页数相当，说明当前为最后一页，可以把整个列表返回了，并跳出循环
            if cur_page == total_page:
                print(list_all_name)
                return list_all_name
            # 上面的条件不满足，则翻页
            self.find(By.CSS_SELECTOR,".js_next_page").click()

    def goto_add_dept(self):
        # 跳转到添加部门页面
        # 点击部门列表上的+
          self.find(By.CSS_SELECTOR,".member_colLeft_top_addBtn").click()
        # 点击"添加部门"
          self.find(By.CSS_SELECTOR,".js_create_party").click()
        # return AddDept页面
          return AddDept(self.driver)

    def get_selected_dept(self):
        # 获取当前已被选择的部门名称
        cur_dept = self.find(By.CSS_SELECTOR,".jstree-clicked").text
        return cur_dept
