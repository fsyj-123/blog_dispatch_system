""" CSDN 平台博客发布插件 """
import logging
import os
import time

from blog_dispatch_system.exception.page_update_except import PageUpdateExcept
from blog_dispatch_system.exception.publish_except import PublishException
from blog_dispatch_system.plugins import PlatformPlugin
from selenium import webdriver
from selenium.webdriver.common.by import By

from blog_dispatch_system.utils.find_utils import find_tag_prefix
from blog_dispatch_system.utils.scirpts.csdn_scripts import *

os.environ['webdriver.chrome.driver'] = "E:\\Explore-driver\\Chrome\\chromedriver.exe"


class CSDNPlatformPlugin(PlatformPlugin):
    platform = "CSDN"

    def __init__(self, **kwargs):
        super().__init__()
        # 设置无头浏览器选项
        self.login_status = False
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')  # 启用无头模式
        options.add_argument('--no-sandbox')  # 避免部分安全限制
        self.driver = webdriver.Chrome(options=options)
        self.tags = kwargs['tags']

    def handle_html_login(self) -> bool:
        # 获取微信登录二维码
        images = find_tag_prefix('img', ['data-v'], self.driver)
        # 这里第一个就是登录二维码
        time.sleep(20)
        return True

    def login(self):
        if self.login_status:
            return True
        self.driver.get('https://passport.csdn.net/login')
        # 点击密码登录
        wx_login = self.driver.find_element(By.XPATH, "//span[contains(text(), '微信登录')]")
        if wx_login:
            wx_login.click()
            if self.handle_html_login():
                self.login_status = True
        else:
            raise PageUpdateExcept(self.platform, '登录页面更新，请联系开发人员')

    def publish(self, blog_content):
        logging.debug("start to publish with csdn")
        if self.login_status:
            publish_btn = self.driver.find_element(By.CSS_SELECTOR,
                                                   'div.toolbar-container-right > :first-child > :nth-child(6) > :first-child')
            if publish_btn:
                publish_btn.click()
                # 预处理，清空 编辑区
                # 调用函数移除子节点直到遇到空白字符
                try:
                    self.driver.execute_script(delete_js)
                    self.driver.execute_script(past_js, blog_content)
                    time.sleep(10)
                    self.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-publish').click()
                    time.sleep(3)
                    self.do_publish()
                except Exception as e:
                    raise PublishException(self.platform, "发布出错，异常信息：" + str(e))
            else:
                raise PageUpdateExcept(self.platform, "发布按钮未找到")

    def logout(self):
        self.driver.quit()

    def do_publish(self):
        # 点击标签展开
        self.driver.execute_script(open_tag_js)
        time.sleep(2)
        # 输入tag
        for tag in self.tags:
            time.sleep(2)
            self.driver.execute_script(input_tag_js, tag)
            time.sleep(3)
            self.driver.execute_script(select_tag_js, tag)
        self.driver.find_element(By.CSS_SELECTOR, "div.modal__button-bar").click()
        time.sleep(5)
