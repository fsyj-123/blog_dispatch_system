class LoginFailedException(Exception):
    def __init__(self, platform_name, message):
        super().__init__(f"Login to platform {platform_name} failed: {message}")
        self.platform_name = platform_name
        self.message = message
