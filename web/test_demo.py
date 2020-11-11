from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains

class TestTestCase():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        # self.var = {}

    def tesrdown_method(self, method):
        self.driver.quit()

    def test_testcaes(self):
        self.driver.get("https://ceshiren.com/")
        # 设置屏幕尺寸
        # self.driver.set_window_size(1128, 849)
        self.driver.find_element(By.LINK_TEXT, "所有分类").click()
        # sleep(2)
        element = self.driver.find_element(By.LINK_TEXT, "所有分类")
        result = element.get_attribute("class")
        assert 'active' == result
        # element = self.driver.find_element(By.LINK_TEXT, "所有分类")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()
        # element = self.driver.find_element(By.CSS_SELECTOR, "body")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element, 0, 0).perform()
        # self.driver.close()

    def test_wx(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(10)
        # 使用复用浏览器，避免登录动作