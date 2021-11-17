# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Kepler",
    "type": "git",
    "url": "https://github.com/AlanDecode/Maverick-Theme-Kepler.git",
    "branch": "latest"
}

enable_jsdelivr = {
    "enabled": False,
    "repo": ""
}

# 站点设置
site_name = "Wainic's wiki"
site_logo = "${static_prefix}android-chrome-512x512.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "Wainic"
email = "iloveyichen@aliyun.com"
author_homepage = "https://wainic.com"
description = "Coding Changes the World"
key_words = ['Maverick', 'wiki', 'Kepler', 'blog']
language = 'zh-CN'
#external_links = [
#    {
#        "name": "Blog",
#        "url": "https://yixi.world",
#        "brief": "My blog."
#    },
#    {
#        "name": "Navigation",
#        "url": "https://nav.yixi.world",
#        "brief": "My navigation network."
#    }
#]
nav = [
    {
        "name": "Home",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "Archives",
        "url": "${site_prefix}archives/",
        "target": "_self"
    }
]

#social_links = [
#    {
#        "name": "Twitter",
#        "url": "https://twitter.com/AlanDecode",
#        "icon": "gi gi-twitter"
#    },
#    {
#        "name": "GitHub",
#        "url": "https://github.com/AlanDecode",
#        "icon": "gi gi-github"
#    },
#    {
#        "name": "Weibo",
#        "url": "https://weibo.com/5245109677/",
#        "icon": "gi gi-weibo"
#    }
#]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="icon" type="image/x-icon" href="https://gallery.dachunwang.top/img/20211117104259.vnd.microsoft.icon"/>
'''

footer_addon = ''

body_addon = ''
