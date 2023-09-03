from blog_dispatch_system.plugins import PlatformPlugin
from blog_dispatch_system.plugins.csdn_plugin import CSDNPlatformPlugin

plugin_map = {
    "CSDN": CSDNPlatformPlugin
}


def load_plugin(platform: str, **kwargs) -> PlatformPlugin:
    if plugin_map.get(platform):
        return CSDNPlatformPlugin(**kwargs)


def load_plugins(platforms: list, **kwargs) -> list:
    return [load_plugin(platform, **kwargs) for platform in platforms]
