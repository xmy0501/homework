from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base_Page1:

    # 定义空的url链接
    _base_url = ""

    # 定义init方法，复用当前chrome浏览器
    def __init__(self, driver: WebDriver = None):
        if driver == None:
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            # 加入隐式等待
            self.driver.implicitly_wait(5)

        else:
            self.driver = driver

        if self._base_url != "":
            self.driver.get(self._base_url)

    # 定义fine方法，避免find_element过多
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    # 定义finds方法，避免find_elements过多
    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    # 定义显示等待
    def wait_for_click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))




