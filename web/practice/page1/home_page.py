from time import sleep

from selenium.webdriver.common.by import By

from web.practice.page1.add_contact_page import AddContactPage
from web.practice.page1.base_page1 import Base_Page1


class HomePage(Base_Page1):

    # 给base——url初始链接
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def add_member_click(self):
        sleep(5)
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddContactPage(self.driver)