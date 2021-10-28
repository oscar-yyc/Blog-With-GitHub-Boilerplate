---
layout: post
title: Rss订阅设置
slug:Rss_setl
date: 2021/5/16 11:30:00
status: publish
author: xiaowangwang
categories: 
  - 编程开发
  - 软件安装

tags: Rss
---

## bilibili

Tiny Tiny RSS 用户请注意

Tiny Tiny RSS 会给所有 iframe 元素添加 `sandbox="allow-scripts"` 属性，导致无法加载 bilibili 内嵌视频，如果需要使用内嵌视频请为 Tiny Tiny RSS 安装 [remove_iframe_sandbox (opens new window)](https://github.com/DIYgod/ttrss-plugin-remove-iframe-sandbox)插件

关于视频清晰度

内嵌视频的默认清晰度为 480P，如需解锁更高清晰度，请[点此 (opens new window)](https://www.bilibili.com/blackboard/html5player.html?cid=253377437&aid=885203421&page=&as_wide=1)在下方登录以设置 Cookie，仅对当前浏览器生效

### [#](https://docs.rsshub.app/social-media.html#bilibili-fan-ju)番剧



作者: [@DIYgod](https://github.com/DIYgod)

举例: https://rsshub.app/bilibili/bangumi/media/9192 ![img](https://gallery.dachunwang.top/img/20211028214445.svg+xml;charset=utf-8)

路由: `/bilibili/bangumi/media/:mediaid`

参数:

- mediaid, 必选 -

   

  番剧媒体 id, 番剧主页 URL 中获取



### [#](https://docs.rsshub.app/social-media.html#bilibili-yong-hu-zhui-fan-lie-biao)用户追番列表

[反爬严格](https://docs.rsshub.app/faq.html) [支持浏览器扩展](https://github.com/DIYgod/RSSHub-Radar) [支持 RSSBud](https://github.com/Cay-Zhang/RSSBud)

作者: [@wdssmq](https://github.com/wdssmq)

举例: https://rsshub.app/bilibili/user/bangumi/208259 ![img](https://gallery.dachunwang.top/img/20211028214445.svg+xml;charset=utf-8)

路由: `/bilibili/user/bangumi/:uid/:type?`

参数:

- uid, 必选 -

   

  用户 id

- type, 可选 -

   

  1为番，2为剧，留空为1



### [#](https://docs.rsshub.app/social-media.html#bilibili-up-zhu-tou-gao)UP 主投稿

[反爬严格](https://docs.rsshub.app/faq.html) [支持浏览器扩展](https://github.com/DIYgod/RSSHub-Radar) [支持 RSSBud](https://github.com/Cay-Zhang/RSSBud)

作者: [@DIYgod](https://github.com/DIYgod)

举例: https://rsshub.app/bilibili/user/video/2267573 ![img](https://gallery.dachunwang.top/img/20211028214445.svg+xml;charset=utf-8)

路由: `/bilibili/user/video/:uid/:disableEmbed?`

参数:

- uid, 必选 -

   

  用户 id, 可在 UP 主主页中找到

- disableEmbed, 可选 -

   

  默认为开启内嵌视频, 任意值为关闭



### [#](https://docs.rsshub.app/social-media.html#bilibili-up-zhu-zhuan-lan)UP 主专栏

[反爬严格](https://docs.rsshub.app/faq.html) [支持浏览器扩展](https://github.com/DIYgod/RSSHub-Radar) [支持 RSSBud](https://github.com/Cay-Zhang/RSSBud)

作者: [@lengthmin](https://github.com/lengthmin)

举例: https://rsshub.app/bilibili/user/article/334958638 ![img](https://gallery.dachunwang.top/img/20211028214445.svg+xml;charset=utf-8)

路由: `/bilibili/user/article/:uid`

参数:

- uid, 必选 -

   

  用户 id, 可在 UP 主主页中找到



### [#](https://docs.rsshub.app/social-media.html#bilibili-up-zhu-dong-tai)UP 主动态

[支持浏览器扩展](https://github.com/DIYgod/RSSHub-Radar) [支持 RSSBud](https://github.com/Cay-Zhang/RSSBud)

作者: [@DIYgod ](https://github.com/DIYgod)[@zytomorrow](https://github.com/zytomorrow)

举例: https://rsshub.app/bilibili/user/dynamic/2267573 ![img](https://gallery.dachunwang.top/img/20211028214445.svg+xml;charset=utf-8)

路由: `/bilibili/user/dynamic/:uid/:disableEmbed?`

参数:

- uid, 必选 -

   

  用户 id, 可在 UP 主主页中找到

- disableEmbed, 可选 -

   

  默认为开启内嵌视频, 任意值为关闭



### [#](https://docs.rsshub.app/social-media.html#bilibili-up-zhu-pin-dao)UP 主频道

[反爬严格](https://docs.rsshub.app/faq.html)

作者: [@HenryQW](https://github.com/HenryQW)

举例: https://rsshub.app/bilibili/user/channel/142821407/49017 ![img](https://gallery.dachunwang.top/img/20211028214445.svg+xml;charset=utf-8)

路由: `/bilibili/user/channel/:uid/:cid/:disableEmbed?`

参数:

- uid, 必选 -

   

  用户 id, 可在 UP 主主页中找到

- cid, 必选 -

   

  频道 id, 可在频道的 URL 中找到

- disableEmbed, 可选 -

   

  默认为开启内嵌视频, 任意值为关闭



### [#](https://docs.rsshub.app/social-media.html#bilibili-up-zhu-mo-ren-shou-cang-jia)UP 主默认收藏夹

[支持浏览器扩展](https://github.com/DIYgod/RSSHub-Radar) [支持 RSSBud](https://github.com/Cay-Zhang/RSSBud)

作者: [@DIYgod](https://github.com/DIYgod)

举例: https://rsshub.app/bilibili/user/fav/2267573 ![img](https://img.shields.io/website?label=status&style=flat-square&url=https%3A%2F%2Frsshub.app%2Fbilibili%2Fuser%2Ffav%2F2267573)

路由: `/bilibili/user/fav/:uid/:disableEmbed?`

参数:

- uid, 必选 -

   

  用户 id, 可在 UP 主主页中找到

- disableEmbed, 可选 -

   

  默认为开启内嵌视频, 任意值为关闭



### [#](https://docs.rsshub.app/social-media.html#bilibili-up-zhu-fei-mo-ren-shou-cang-jia)UP 主非默认收藏夹



作者: [@Qixingchen](https://github.com/Qixingchen)

举例: https://rsshub.app/bilibili/fav/756508/50948568 ![img](https://img.shields.io/website?label=status&style=flat-square&url=https%3A%2F%2Frsshub.app%2Fbilibili%2Ffav%2F756508%2F50948568)

路由: `/bilibili/fav/:uid/:fid/:disableEmbed?`

参数:

- uid, 必选 -

   

  用户 id, 可在 UP 主主页中找到

- fid, 必选 -

   

  收藏夹 ID, 可在收藏夹的 URL 中找到, 默认收藏夹建议使用 UP 主默认收藏夹功能

- disableEmbed, 可选 -

   

  默认为开启内嵌视频, 任意值为关闭



### [#](https://docs.rsshub.app/social-media.html#bilibili-up-zhu-tou-bi-shi-pin)UP 主投币视频

[反爬严格](https://docs.rsshub.app/faq.html) [支持浏览器扩展](https://github.com/DIYgod/RSSHub-Radar) [支持 RSSBud](https://github.com/Cay-Zhang/RSSBud)

作者: [@DIYgod](https://github.com/DIYgod)

举例: https://rsshub.app/bilibili/user/coin/208259 ![img](https://img.shields.io/website?label=status&style=flat-square&url=https%3A%2F%2Frsshub.app%2Fbilibili%2Fuser%2Fcoin%2F208259)

路由: `/bilibili/user/coin/:uid/:disableEmbed?`

参数:

- uid, 必选 -

   

  用户 id, 可在 UP 主主页中找到

- disableEmbed, 可选 -

   

  默认为开启内嵌视频, 任意值为关闭



### [#](https://docs.rsshub.app/social-media.html#bilibili-up-zhu-fen-si)UP 主粉丝

[支持浏览器扩展](https://github.com/DIYgod/RSSHub-Radar) [支持 RSSBud](https://github.com/Cay-Zhang/RSSBud)

作者: [@Qixingchen](https://github.com/Qixingchen)

举例: https://rsshub.app/bilibili/user/followers/2267573 ![img](https://img.shields.io/website?label=status&style=flat-square&url=https%3A%2F%2Frsshub.app%2Fbilibili%2Fuser%2Ffollowers%2F2267573)

路由: `/bilibili/user/followers/:uid`

参数:

- uid, 必选 -

   

  用户 id, 可在 UP 主主页中找到



### [#](https://docs.rsshub.app/social-media.html#bilibili-up-zhu-guan-zhu-yong-hu)UP 主关注用户

[支持浏览器扩展](https://github.com/DIYgod/RSSHub-Radar) [支持 RSSBud](https://github.com/Cay-Zhang/RSSBud)

作者: [@Qixingchen](https://github.com/Qixingchen)

举例: https://rsshub.app/bilibili/user/followings/2267573 ![img](https://img.shields.io/website?label=status&style=flat-square&url=https%3A%2F%2Frsshub.app%2Fbilibili%2Fuser%2Ffollowings%2F2267573)

路由: `/bilibili/user/followings/:uid`

参数:

- uid, 必选 -

   

  用户 id, 可在 UP 主主页中找到



### [#](https://docs.rsshub.app/social-media.html#bilibili-fen-qu-shi-pin)分区视频

[支持浏览器扩展](https://github.com/DIYgod/RSSHub-Radar) [支持 RSSBud](https://github.com/Cay-Zhang/RSSBud)

作者: [@DIYgod](https://github.com/DIYgod)

举例: https://rsshub.app/bilibili/partion/33 ![img](https://img.shields.io/website?label=status&style=flat-square&url=https%3A%2F%2Frsshub.app%2Fbilibili%2Fpartion%2F33)

路由: `/bilibili/partion/:tid/:disableEmbed?`

参数:

- tid, 必选 -

   

  分区 id

- disableEmbed, 可选 -

   

  默认为开启内嵌视频, 任意值为关闭



动画

| MAD·AMV | MMD·3D | 短片・手书・配音 | 特摄 | 综合 |
| ------- | ------ | ---------------- | ---- | ---- |
| 24      | 25     | 47               | 86   | 27   |

番剧

| 连载动画 | 完结动画 | 资讯 | 官方延伸 |
| -------- | -------- | ---- | -------- |
| 33       | 32       | 51   | 152      |

国创

| 国产动画 | 国产原创相关 | 布袋戏 | 动态漫・广播剧 | 资讯 |
| -------- | ------------ | ------ | -------------- | ---- |
| 153      | 168          | 169    | 195            | 170  |

音乐

| 原创音乐 | 翻唱 | VOCALOID·UTAU | 电音 | 演奏 | MV   | 音乐现场 | 音乐综合 | OP/ED/OST |
| -------- | ---- | ------------- | ---- | ---- | ---- | -------- | -------- | --------- |
| 28       | 31   | 30            | 194  | 59   | 193  | 29       | 130      | 54        |

舞蹈

| 宅舞 | 街舞 | 明星舞蹈 | 中国舞 | 舞蹈综合 | 舞蹈教程 |
| ---- | ---- | -------- | ------ | -------- | -------- |
| 20   | 198  | 199      | 200    | 154      | 156      |

游戏

| 单机游戏 | 电子竞技 | 手机游戏 | 网络游戏 | 桌游棋牌 | GMV  | 音游 | Mugen |
| -------- | -------- | -------- | -------- | -------- | ---- | ---- | ----- |
| 17       | 171      | 172      | 65       | 173      | 121  | 136  | 19    |

知识

| 科学科普 | 社科人文 | 财经 | 校园学习 | 职业职场 | 野生技术协会 |
| -------- | -------- | ---- | -------- | -------- | ------------ |
| 201      | 124      | 207  | 208      | 209      | 122          |

科技

| 演讲・公开课 | 星海 | 机械 | 汽车 |
| ------------ | ---- | ---- | ---- |
| 39           | 96   | 98   | 176  |

数码

| 手机平板 | 电脑装机 | 摄影摄像 | 影音智能 |
| -------- | -------- | -------- | -------- |
| 95       | 189      | 190      | 191      |

生活

| 搞笑 | 日常 | 美食圈 | 动物圈 | 手工 | 绘画 | 运动 | 汽车 | 其他 | ASMR |
| ---- | ---- | ------ | ------ | ---- | ---- | ---- | ---- | ---- | ---- |
| 138  | 21   | 76     | 75     | 161  | 162  | 163  | 176  | 174  | 175  |

鬼畜

| 鬼畜调教 | 音 MAD | 人力 VOCALOID | 教程演示 |
| -------- | ------ | ------------- | -------- |
| 22       | 26     | 126           | 127      |

时尚

| 美妆 | 服饰 | 健身 | T 台 | 风向标 |
| ---- | ---- | ---- | ---- | ------ |
| 157  | 158  | 164  | 159  | 192    |

广告

| 广告 |
| ---- |
| 166  |

资讯

| 热点 | 环球 | 社会 | 综合 |
| ---- | ---- | ---- | ---- |
| 203  | 204  | 205  | 206  |

娱乐

| 综艺 | 明星 | Korea 相关 |
| ---- | ---- | ---------- |
| 71   | 137  | 131        |

影视

| 影视杂谈 | 影视剪辑 | 短片 | 预告・资讯 |
| -------- | -------- | ---- | ---------- |
| 182      | 183      | 85   | 184        |

纪录片

| 全部 | 人文・历史 | 科学・探索・自然 | 军事 | 社会・美食・旅行 |
| ---- | ---------- | ---------------- | ---- | ---------------- |
| 177  | 37         | 178              | 179  | 180              |

电影

| 全部 | 华语电影 | 欧美电影 | 日本电影 | 其他国家 |
| ---- | -------- | -------- | -------- | -------- |
| 23   | 147      | 145      | 146      | 83       |

电视剧

| 全部 | 国产剧 | 海外剧 |
| ---- | ------ | ------ |
| 11   | 185    | 187    |

### [#](https://docs.rsshub.app/social-media.html#bilibili-fen-qu-shi-pin-pai-xing-bang)分区视频排行榜



作者: [@lengthmin](https://github.com/lengthmin)

举例: https://rsshub.app/bilibili/partion/ranking/171/3 ![img](https://img.shields.io/website?label=status&style=flat-square&url=https%3A%2F%2Frsshub.app%2Fbilibili%2Fpartion%2Franking%2F171%2F3)

路由: `/bilibili/partion/ranking/:tid/:days?/:disableEmbed?`

参数:

- tid, 必选 -

   

  分区 id, 见上方表格

- days, 可选 -

   

  缺省为 7, 指最近多少天内的热度排序

- disableEmbed, 可选 -

   

  默认为开启内嵌视频, 任意值为关闭