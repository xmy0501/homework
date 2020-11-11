# 浏览器复用
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWX:
    def setup(self):
        option = Options()
        # 端口号要与复用浏览器时命令行启动的端口号一致
        option.debugger_address = "127.0.0.1:9222"
        # 复用浏览器
        # self.driver = webdriver.Chrome(options=option)
        # 另起页面，不复用浏览器
        self.driver = webdriver.Chrome()

    def tesrdown(self):
        self.driver.quit()

    def test_case1(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.ID, "menu_contacts").click()

    def test_cookie(self):
        cookies = self.driver.get_cookies()
        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'T5N2SJWc1V5j-R-0b-udXdUlKPkpwwc1skn0vIVE7YRR5lOY24irdt0npbsGNSrW'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a1210734'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688852020690737'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': 'yALQAuCA9w8NLx_iLLcDRwaujO8tz1t_ik-s5lHgxJoKFz4ytNnfRyM-IAV2AsVELLL4cdflui2hEJeBmrUh9E8vfM9wBvMlzIXVqG-fxXblUr7GNPI0-OyE02agGuA3TSe8etvaHqs2ScNHB51RvIIsbQeuzQ0eZyMoDeUc44VHeWaZ-YxXeWHD_XNbZVKd25Ca62zmdeNBcaOzreyCfup-mDQsbmea-wKy-I8Vw1A7lI8ZHISJAotH9PXq-ITbSNV50DFgd26Y2WPyEEnhvA'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688852020690737'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970324988186667'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636553824, 'httpOnly': False,
        #                           'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
        #                           'value': '1605017690,1605017716'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.qq.com', 'expiry': 1605194604, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.628451993.1605017691'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1605138175, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': 'fvj9ig'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '3496926173343967'},
        #     {'domain': '.qq.com', 'expiry': 1668180204, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.872410313.1605017691'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1636553688, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1607700207, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'},
        #     {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
        #      'value': '0bef1bc4720731a5b1dac5cdab77c72a6cd423f9203d0c773febe85b8fb3a23c'},
        #     {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
        #      'value': '8HxMJe5HMd'}]
        print(cookies)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.refresh()

    def test_case2(self):
        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'T5N2SJWc1V5j-R-0b-udXdUlKPkpwwc1skn0vIVE7YRR5lOY24irdt0npbsGNSrW'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a1210734'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688852020690737'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': 'yALQAuCA9w8NLx_iLLcDRwaujO8tz1t_ik-s5lHgxJoKFz4ytNnfRyM-IAV2AsVELLL4cdflui2hEJeBmrUh9E8vfM9wBvMlzIXVqG-fxXblUr7GNPI0-OyE02agGuA3TSe8etvaHqs2ScNHB51RvIIsbQeuzQ0eZyMoDeUc44VHeWaZ-YxXeWHD_XNbZVKd25Ca62zmdeNBcaOzreyCfup-mDQsbmea-wKy-I8Vw1A7lI8ZHISJAotH9PXq-ITbSNV50DFgd26Y2WPyEEnhvA'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688852020690737'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970324988186667'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636553824, 'httpOnly': False,
        #                           'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
        #                           'value': '1605017690,1605017716'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.qq.com', 'expiry': 1605194604, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.628451993.1605017691'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1605138175, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': 'fvj9ig'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '3496926173343967'},
        #     {'domain': '.qq.com', 'expiry': 1668180204, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.872410313.1605017691'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1636553688, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1607700207, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'},
        #     {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
        #      'value': '0bef1bc4720731a5b1dac5cdab77c72a6cd423f9203d0c773febe85b8fb3a23c'},
        #     {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
        #      'value': '8HxMJe5HMd'}]
        # shelve模块 python自带的对象持久化存储
        db = shelve.open('cookies')
        cookies = db['cookie']
        db.close()
        # 打开无痕新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 加入cookie
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # 刷新当前页面，获取登录状态
        self.driver.refresh()

    def test_import_contact(self):
        # shelve模块 python自带的对象持久化存储
        db = shelve.open('cookies')
        cookies = db['cookie']
        db.close()
        # 打开无痕新页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 加入cookie
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # 刷新当前页面，获取登录状态
        self.driver.refresh()
        # 点击导入联系人
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        # # 上传文件，选择文件的完整路径
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys("/Users/a10369/Desktop/data.xlsx")
        # # 判断上传文件名，与实际文件名一致
        result = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames').text
        assert "data.xlsx" == result
        # sleep(5)
