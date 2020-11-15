from selenium.webdriver.common.by import By

from web.practice.page1.home_page import HomePage
class TestCase:
    def setup(self):
        self.main = HomePage()

    def teardown(self):
        pass

    def test_get_member(self):
        name = "xmy_03"
        account = "xmy_03_hogwarts"
        phonenum = "15221345679"
        gender = "女"
        value = "zz"
        # 点击添加成员自定义为addmember
        self.main.add_member_click().add_contact(name, account, gender, phonenum).get_member(value)
        # addmember.add_contact(name, account, phonenum)
        # addmember.get_member()
