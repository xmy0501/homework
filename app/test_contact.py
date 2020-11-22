from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWX:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "True"

        # 建立客户端与服务端的连接
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_contact(self):
        sleep(10)
        name = "倩倩"
        gender = "女"
        phonenum = "18300000000"
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # 点击添加成员
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        # 点击手动添加输入
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        # 定位姓名输入框，输入姓名
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(name)
        # 定位性别项，判断选择输入性别
        self.driver.find_element(MobileBy.XPATH, '//*[@text="性别"]/..//*[@text="男"]').click()
        if gender == "男":
            self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        else:
            self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
        # 定位手机号输入框输入手机号
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手机号"]').send_keys(phonenum)
        # 点击保存，保存联系人
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()

        # 添加断言，判断是否添加成功
        toast = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        assert "添加成功" == toast