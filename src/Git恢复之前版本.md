---
layout: post
title: Git恢复之前版本
slug: Git_reset
date: 2021/2/20 11:30:00
status: publish
author: Wainic
categories: 
  - 日常技巧

tags: 
  - Git
---

## 查看版本号

   可以使用下面命令查看

   ```git
git log
   ```

   ![](https://gallery.dachunwang.top/img/202112292050132.png)

   也可以在 github 网站上查看：

![](https://gallery.dachunwang.top/img/202112292056645.png)

## 使用下面命令将版本退回

   ```git
git reset --hard 目标版本号
   ```

## 使用下面命令提交更改

   ```git
git push -f
   ```

回退成功！
