import time

from blog_dispatch_system.plugins import PlatformPlugin
import logging


def _login_with_retry(plugin, max_retries=3):
    """
    尝试登录到平台，最多重试max_retries次。

    :param plugin: 平台插件
    :param max_retries: 最大重试次数
    :return: 登录是否成功
    """
    for retry_times in range(max_retries):
        if plugin.login():
            return True
        time.sleep(5)  # 等待5秒后重试
        logging.info(f'retry login {plugin.platform} with times:{retry_times}')
    # 如果没有登录成功，则清除数据
    plugin.logout()
    return False


def _publish_blog(plugin, blog_content):
    """
    发布博客到平台。

    :param plugin: 平台插件
    :param blog_content: 博客原文内容
    """
    plugin.publish(blog_content)


class BlogScheduler:

    @classmethod
    def schedule_publish(cls, plugins: list, blog_content):
        """
        调度发布博客原文到不同的平台。

        :param blog_content: 博客原文内容
        :param plugins: 插件
        """
        for plugin in plugins:
            if isinstance(plugin, PlatformPlugin):
                try:
                    if _login_with_retry(plugin):
                        _publish_blog(plugin, blog_content)
                except Exception as e:
                    logging.error(f"{plugin.platform}发布错误：", e)
                finally:
                    # 退出，防止占用资源
                    plugin.logout()
