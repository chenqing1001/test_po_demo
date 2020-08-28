from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# BasePage负责所有公共的方法
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self,driver1=None):
        #如果dirvier是null则进行初始化
        if driver1 ==None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options = option)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        #否则self.driver等于传入的已经初始化的driver
        else:
            self.driver:webdriver = driver1
        self.driver.implicitly_wait(5) #隐式等待

    #以下为封装公用方法
    def find(self,by,value):
        return self.driver.find_element(by,value)

    def finds(self,by,value):
        return self.driver.find_elements(by,value)

    #显示等待，等待元素可点击
    def wait_for_clickable(self,ele,time=10):
        return WebDriverWait(self.driver,time).until(expected_conditions.element_to_be_clickable(ele))

    # 显示等待，等待元素显示
    def wait_for_visible(self, ele, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(ele))

    def quit(self):
        return self.driver.quit()



