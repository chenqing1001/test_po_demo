from test_homework_import_dept.page.main import Main


class TestAddDept:

    def setup(self):
        self.main = Main()

    def teardown(self):
        # self.main.quit()
        pass

    def test_add_dept(self):
       # 1、在主页点击通讯录进入通讯录页面
       # 2、在通讯录页面点击+按钮，跳转至添加部门页面
       # 3、获取当前所选择的部门名称，与输入的部门名称对比
       cur_dept = Main().goto_contact().goto_add_dept().add_dept("测试部").get_selected_dept()
       assert "测试部" == cur_dept

