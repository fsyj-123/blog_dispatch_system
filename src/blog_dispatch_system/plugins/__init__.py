from abc import ABC, abstractmethod


class PlatformPlugin(ABC):
    platform: str

    def __init__(self):
        """
        初始化平台插件。

        """

    @abstractmethod
    def login(self):
        """
        登录到发布平台。
        实现此方法以处理平台的登录逻辑。
        """
        pass

    @abstractmethod
    def publish(self, blog_content):
        """
        发布博客原文到发布平台。

        :param blog_content: 博客原文内容
        """
        pass

    @abstractmethod
    def logout(self):
        """
        登出发布平台。
        实现此方法以处理平台的登出逻辑。
        """
        pass

    def handle_html_login(self):
        """
        处理扫码登录，可能涉及等待用户扫码、轮询检查登录状态等。
        """
        pass
