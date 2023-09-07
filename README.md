# Blog Dispatch System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 项目简介

Blog Dispatch System 是一个用于自动发布博客到多个平台的系统。它使用Python 3.10及以上版本进行开发，采用了Poetry来进行依赖管理。

## 安装

首先，请确保你已经安装了Python 3.10或更高版本，并且安装了Poetry。如果没有安装Poetry，你可以按照官方文档进行安装：[Poetry Installation Guide](https://python-poetry.org/docs/#installation)

在项目目录中执行以下命令来安装依赖：

```bash
poetry install
```

## 使用
在使用Blog Dispatch System之前，你需要进行额外的配置。具体配置可以在plugins目录下实现一个自定义的PlatformPlugin类，以满足你的发布平台需求。确保你已经提供了正确的平台登录凭证和配置信息。

## 配置
1. 在config/目录下创建一个配置文件，以存储平台登录凭证和其他必要信息。可以使用JSON或YAML格式来定义配置文件。

2. 在plugins/目录下实现自定义的PlatformPlugin类，以处理不同平台的登录和发布逻辑。确保你的插件实现了login和publish方法。

## 运行
一旦完成配置，你可以使用Blog Dispatch System来发布博客。运行以下命令：
``` python
python main.py
```
