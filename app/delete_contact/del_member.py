"""
appium自动化第一次直播课课后作业：
删除企业微信通讯录联系人
"""

from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class TestBasePage:

    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = True
        # 建立客户端与服务端的连接
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def test_goto_contact(self):
        sleep(10)
        name = "zz"
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/i6n').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="搜索"]').send_keys(name)
        sleep(2)
        list1 = self.driver.find_elements(MobileBy.ID, 'com.tencent.wework:id/e6d')
        # list = self.driver.find_elements(MobileBy.XPATH,"zz")
        print(type(list1), len(list1))
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/i63').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("zz").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, f'//*[@text="zz"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/i6d').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("删除成员").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="确定"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/i6n').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="搜索"]').send_keys(name)
        sleep(2)
        list2 = self.driver.find_elements(MobileBy.ID, 'com.tencent.wework:id/e6d')
        print(type(list2), len(list2))
    #     list2 = self.driver.find_elements(MobileBy.XPATH, '//*[@text="搜索"]').send_keys(name)
        if len(list2) < len(list1):
            print("删除成功")
        else:
            print("删除失败")