# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python


# 导入之前，安装appium-python-client 客户端安装包
from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "emulator-5554"
caps["appPackage"] = "com.tencent.wework"
caps["appActivity"] = ".launch.LaunchSplashActivity"
caps["noReset"] = "True"

# 建立客户端与服务端的连接
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
el2.click()
el3 = driver.find_element_by_id("com.tencent.wework:id/i6n")
el3.click()
el5 = driver.find_element_by_id("com.tencent.wework:id/gpg")
el5.send_keys("hogwarts1")

driver.quit()