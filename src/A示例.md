---
layout: post
title: Git 连接 Github 与 Coding
slug: Git_set
date: 2021/2/17 11:30:00
status: hidden
author: Wainic
categories: 
  - 编程开发
  - 环境配置

tags: 
  - Git
  - Coding
---

## Github 仓库连接

打开 cmd 输入下面命令

```git
git config --global user.name "username"   # username是你的GitHub用户名，注意大小写
git config --global user.email "email"     # email是注册 GitHub的邮箱
ssh-keygen -t ed25519 -C "email"           # 生成ed25519密钥对，email同上
接下来一直回车就可以
```

默认密钥对在用户目录的 `.ssh` 目录下，在该目录你可以看到 `id_ed25519`和 `id_ed25519.pub` ，使用文本编辑器打开 `id_rsa.pub` 文件并复制

打开 GitHub，点击头像的 `settings` 选项进入设置，在 SSH and GPG keys 中粘贴 ``id_ed25519.pub`` 中的内容，并点击 `Add SSH key`

回到本地的 cmd ，输入命令连接 GitHub

```git
ssh -T git@github.com
```

出现一个 hostname 提示输入 `yes` 回车，类似下面的提示就代表没问题了

```
Hi oscar-yyc! You've successfully authenticated, but GitHub does not provide shell access.
```



## Coding 仓库连接

打开 cmd 输入下面命令

```
ssh-keygen
接下来一直回车就可以
```

默认密钥对在用户目录的 `.ssh` 目录下，在该目录你可以看到 `id_rsa` 和 `id_rsa.pub` ，使用文本编辑器打开 `id_rsa.pub` 文件并复制

打开 Coding，点击头像的 `个人账户设置` 选项进入设置，点击 `新增公钥` ，输入公钥的名称，并在 公钥内容 中粘贴 `id_rsa.pub` 中的内容，勾选`永久有效`后点击`确认`

