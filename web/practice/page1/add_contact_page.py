from selenium.webdriver.common.by import By

from web.practice.page1.address_book_page import AddressBook
from web.practice.page1.base_page1 import Base_Page1


class AddContactPage(Base_Page1):

    def add_contact(self, name, account, phonenum):
        # 输入姓名
        self.find(By.ID, "username").send_keys(name)
        # 输入账号
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        # 输入手机号
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        # 保存
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()

        return AddressBook(self.driver)


