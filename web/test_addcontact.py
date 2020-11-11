import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestAddcontact:

    def setup(self):
        option = Options()
        # 端口号要与复用浏览器时命令行启动的端口号一致
        option.debugger_address = "127.0.0.1:9222"
        # 直接启动新的浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass
        # self.driver.quit()

    def test_addcontact(self):
        db = shelve.open('cookies')
        cookies = db['cookie']
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys("aaa_0")
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys("hahaha")
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_phone').send_keys("15908484811")
        self.driver.find_element(By.XPATH, '//*[@class="qui_btn ww_btn js_btn_save"]').click()
        # sleep(5)
        result = self.driver.find_element(By.XPATH, '//*[@class="ww_tip success"]').text
        # self.driver.find_element(By.CSS_SELECTOR, '#memberSearchInput').send_keys("aaaa")
        # result = self.driver.find_element(By.XPATH, '//*[@class="ww_searchResult_title_peopleName"]')
        assert "保存成功" == result






