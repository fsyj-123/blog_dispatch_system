class PageUpdateExcept(Exception):
    def __init__(self, platform_name, message):
        super().__init__(f"{platform_name}页面被官方更新，详情；{message}")
        self.platform_name = platform_name
        self.message = message
