class PublishException(Exception):
    def __init__(self, platform_name, message):
        super().__init__(f"{platform_name} 发布出错，异常信息：{message}")
        self.platform_name = platform_name
        self.message = message
