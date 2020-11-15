from selenium.webdriver.common.by import By

from web.practice.page1.base_page1 import Base_Page1


class AddressBook(Base_Page1):
    # 搜索框内输入要验证的成员名称
    def get_member(self, value):
        self.find(By.ID, 'memberSearchInput').send_keys(value)
        elements = self.finds(By.CSS_SELECTOR, '.ww_searchResult_title_peopleName')
        print(elements)
        if value in elements:
            print("添加成功")

        else:
            print("添加失败")

