---
layout: post
title: 转载 - 使用 scoop 管理 Windows 下的软件和开发环境
slug: Scoop_install
date: 2021/8/16 11:30:00
status: publish
author: Wainic
categories: 
  - 编程开发
  - 环境配置

tags: 
  - Scoop
  - Git
---

## 前言

假如你的计算机使用 Windows 系统，如果你需要安装 Git，正常的步骤是：

打开浏览器——>在搜索引擎中输入关键词「Git」——>找到 Git 官网——>下载 Git 安装包——>运行 Git 安装程序——>安装完成

如果你使用的是「Baidu」等**搜索引擎，中间的过程可能会更加繁琐曲折

在 Windows 下大部分软件安装、配置使用各种不规范的目录，弄脏你系统的注册表，将计算机系统内部弄得脏乱不堪，这是让人难以忍受的

由于工作、学习环境对 Windows 生态系统的依赖亦或是迁移 Linux、macOS 生态的过程会增加学习和金钱成本，是时候摆脱这个困境了，请允许我介绍 Windows 下最好用的 「包管理器」——[Scoop](https://scoop.sh/)！

Windows 下目前主要有三种包管理器：

- [Scoop](https://scoop.sh/)
- [Chocolatey](https://chocolatey.org/)
- [Winget](https://github.com/microsoft/winget-cli)

本文不做三者的比较，仅讨论 Scoop；严格来说，Scoop 不算是「包管理器」，官方解释为「Scoop 是 Windows 的命令行安装程序」，但它基本实现了 Windows 上管理软件包的流程

**包管理器：**或叫 `包管理系统` 是在计算机中自动安装、配置、卸载和升级软件包的工具的集合，在 `系统软件` 和 `应用软件` 的软件管理中都有大量应用，常见的一些系统/应用软件包管理器：

| 软件          | 包管理器 | 实例                      |
| ------------- | -------- | ------------------------- |
| Debian/Ubuntu | apt      | apt install git           |
| ArchLinux     | pacman   | pacman -S git             |
| macOS         | Homebrew | brew install git          |
| openSUSE      | zypper   | zypper install git        |
| Python        | Pypi     | pip install opencv-python |

## 简介

### Scoop 是什么？

Scoop 是 Windows 的命令行安装程序（command-line installer）

Scoop 致力于解决：

- 权限弹出窗口（Windows UAC）
- GUI 引导式安装程序
- 安装大量程序后造成的文件路径污染
- 安装和卸载程序的污染和残留
- 查找和安装依赖程序
- 需要执行额外的配置以使程序工作

### 环境要求

- 系统版本：Windows 7 SP1 及 Windows Server 2008 之后的版本
- PowerShell 5（或更高版本，包括 PowerShell Core）
- Net Framework 4.5 及更高版本
- 由于中国大陆特殊的网络情况，大概率还需要科学上网

**建议环境：**

- [CFW 优雅地使用 TUN 模式接管系统流量](https://www.dejavu.moe/posts/cfw-tun/)
- [Windows Terminal & PowerShell 7 打造 Windows 下最好用的终端](https://www.dejavu.moe/posts/windows-terminal/)

## 安装

### 执行策略

首先，以管理员身份打开 Windows Terminal/PowerShell，允许执行本地脚本

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 安装路径

Scoop 是自由的，无论是 Scoop 本身的安装路径还是以后使用 Scoop 安装的软件路径，都是可控的：

- Scoop 本身和安装软件的路径为：`C:\Users\[username]\scoop`
- Scoop 全局安装软件的路径为：`C:\ProgramData\scoop`

在开始安装 Scoop 前，我们应当提前设置环境变量决定其安装路径

对于 Scoop 本身和安装软件的路径，打开 Windows Terminal/PowerShell

```
$env:SCOOP='C:\Scoop'
[Environment]::SetEnvironmentVariable('SCOOP', $env:SCOOP, 'User')
```

对于 Scoop 全局安装软件的路径，以 `管理员身份` 打开 Windows Terminal/PowerShell

```
$env:SCOOP_GLOBAL='C:\Scoop\Global'
[Environment]::SetEnvironmentVariable('SCOOP_GLOBAL', $env:SCOOP_GLOBAL, 'Machine')
```

### 安装 scoop

现在可以开始安装 Scoop 了，打开 Windows Terminal/PowerShell

```
Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
# 或者短命令
iwr -useb get.scoop.sh | iex
```

![img](https://gallery.dachunwang.top/img/20211122103403.webp)

### 安装 Git

对于 Scoop 来说，Git 是必需的组件，现在安装很简单

```
scoop install git
```

PS: 安装 Git 会附带安装 7zip，它也是 Scoop 必需的组件

### 安装 Aria2

Scoop 使用 [Aria2](https://github.com/aria2/aria2) 进行多线程下载，之后它会应用于 Scoop 安装软件过程所有的下载

```
scoop install aria2
```

配置一下 Aria2 的参数 `scoop config [参数]`

参数：

- aria2-enabled (是否启用 Aria2，默认: true)
- [aria2-retry-wait](https://aria2.github.io/manual/en/html/aria2c.html#cmdoption-retry-wait) (重试等待时间，默认: 2)
- [aria2-split](https://aria2.github.io/manual/en/html/aria2c.html#cmdoption-s) (单任务最大连接数，默认: 5)
- [aria2-max-connection-per-server](https://aria2.github.io/manual/en/html/aria2c.html#cmdoption-x) (单服务器最大连接数，默认: 5，最大: 16)
- [aria2-min-split-size](https://aria2.github.io/manual/en/html/aria2c.html#cmdoption-k) (文件最小切片大小: 5M)

比如：

```
# 重试等待时间 5s
scoop config aria2-retry-wait 5
# 单任务最大连接数 32
scoop config aria2-split 32
# 单服务器最大连接数 16
scoop config aria2-max-connection-per-server 16
# 文件最小切片 1M
scoop config aria2-min-split-size 1M
```

### 安装 sudo

当 Scoop 全局安装软件的时候，需要管理员权限，在日常的使用过程中，我们可以在 scoop 命令前加 sudo 来提权以简化步骤，安装 sudo

```
scoop install sudo
```

**可能需要的步骤：**

在使用 `scoop checkup` 后看到如下提示

```
WARN  Windows Defender may slow down or disrupt installs with realtime scanning.
  Consider running:
    sudo Add-MpPreference -ExclusionPath 'C:\Scoop'
  (Requires 'sudo' command. Run 'scoop install sudo' if you don't have it.)
WARN  Windows Defender may slow down or disrupt installs with realtime scanning.
  Consider running:
    sudo Add-MpPreference -ExclusionPath 'C:\Scoop\Global'
  (Requires 'sudo' command. Run 'scoop install sudo' if you don't have it.)
WARN  LongPaths support is not enabled.
You can enable it with running:
    Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem' -Name 'LongPathsEnabled' -Value 1
WARN  Found 3 potential problems.
```

其中有三个「潜在」问题，可以按照自己实际情况选择执行

```
# Windows Defender可能会因实时扫描而减慢或破坏安装（注意对应实际 Scoop 路径）
sudo Add-MpPreference -ExclusionPath 'C:\Scoop'
sudo Add-MpPreference -ExclusionPath 'C:\Scoop\Global'
# 长路径支持（建议开启）
sudo Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem' -Name 'LongPathsEnabled' -Value 1
```

## 使用

使用命令 `scoop help` 可以查看 scoop 命令帮助

```
Usage: scoop <command> [<args>]

Some useful commands are:

alias       Manage scoop aliases
bucket      Manage Scoop buckets
cache       Show or clear the download cache
checkup     Check for potential problems
cleanup     Cleanup apps by removing old versions
config      Get or set configuration values
create      Create a custom app manifest
depends     List dependencies for an app
export      Exports (an importable) list of installed apps
help        Show help for a command
hold        Hold an app to disable updates
home        Opens the app homepage
info        Display information about an app
install     Install apps
list        List installed apps
prefix      Returns the path to the specified app
reset       Reset an app to resolve conflicts
search      Search available apps
status      Show status and check for new app versions
unhold      Unhold an app to enable updates
uninstall   Uninstall an app
update      Update apps, or Scoop itself
virustotal  Look for app's hash on virustotal.com
which       Locate a shim/executable (similar to 'which' on Linux)

Type 'scoop help <command>' to get help for a specific command.
```

使用 `scoop help <command>`，查看具体命令的帮助，比如，使用 `scoop help config` 查看 `config` 命令的帮助

```
Usage: scoop config [rm] name [value]

The scoop configuration file is saved at ~/.config/scoop/config.json.

To get a configuration setting:

    scoop config <name>

To set a configuration setting:

    scoop config <name> <value>

To remove a configuration setting:

    scoop config rm <name>

Settings
--------

proxy: [username:password@]host:port

By default, Scoop will use the proxy settings from Internet Options, but with anonymous authentication.

* To use the credentials for the current logged-in user, use 'currentuser' in place of username:password
* To use the system proxy settings configured in Internet Options, use 'default' in place of host:port
* An empty or unset value for proxy is equivalent to 'default' (with no username or password)
* To bypass the system proxy and connect directly, use 'none' (with no username or password)
```

### 安装

```
# 安装 <AppName>
scoop install <AppName>
# 安装 <AppName> 且禁止缓存安装包
scoop install -k <AppName>
# 安装 <AppName> 的指定版本 <Version>
scoop install <AppName>@<Version>
# 安装 <AppName> 的指定版本 <Version> 且禁止缓存安装包
scoop install -k <AppName>@<Version>
# 全局安装 <AppName>
sudo scoop install <AppName> -g
# 全局安装 <AppName> 且禁止缓存安装包
sudo scoop install -gk <AppName>
```

### 卸载

```
# 卸载 <AppName>
scoop uninstall <AppName>
# 卸载全局安装的 <AppName>
sudo scoop uninstall -g <AppName>
# 卸载 <AppName> 且删除配置文件
scoop uninstall -p <AppName>
# 卸载全局安装的 <AppName> 且删除配置文件
sudo scoop uninstall -gp <AppName>
```

### 更新

```
# 查看更新
scoop status
# 更新所有非全局安装的应用
scoop update *
# 更新所有全局安装的应用
sudo scoop update * -g
# 更新 scoop 和 bucket
scoop update
# 禁止更新名为 <AppName> 的应用
scoop hold <AppName>
# 允许更新名为 <AppName> 的应用
scoop unhold <AppName>
```

### Bucket

Scoop 的软件存储库使用「Bucket」的概念，它是应用程序的集合，或者更具体地说，Bucket 是一个 Git 存储库，其中包含描述如何安装应用程序的JSON [应用程序清单](https://github.com/ScoopInstaller/Main/tree/master/bucket) 主要的 Bucket [按照  Star 数](https://raw.githubusercontent.com/rasa/scoop-directory/master/by-score.md) 排序：

| Bucket                                                       | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Main](https://github.com/lukesampson/scoop)                 | Windows 的命令行安装程序                                     |
| [extras](https://github.com/lukesampson/scoop-extras)        | 包含不太符合主存储桶标准的应用                               |
| [main](https://github.com/ScoopInstaller/Main)               | 下一代的 Scoop 默认 Bucket                                   |
| [chawyehsu/dorado](https://github.com/chawyehsu/dorado)      | 又是一个可爱的 Scoop 的 Bucket                               |
| [Ash258/Scoop-Ash258](https://github.com/Ash258/Scoop-Ash258) | 个人 Bucket，包含各种应用                                    |
| [nerd-fonts](https://github.com/matthewjberger/scoop-nerd-fonts) | 一个用于安装 Nerd Fonts 字体的 Bucket                        |
| [java](https://github.com/ScoopInstaller/Java)               | 用于 Oracle Java, OpenJDK, Zulu, ojdkbuild, AdoptOpenJDK, Amazon Corretto, BellSoft Liberica, SapMachine和Microsoft JDK 的 Bucket |
| [borger/scoop-galaxy-integrations](https://github.com/borger/scoop-galaxy-integrations) | 提供安装、附加和更新 GOG Galaxy 2 号集成的简单方法           |
| [TheRandomLabs/Scoop-Spotify](https://github.com/TheRandomLabs/Scoop-Spotify) | 一个用于 Spotify、Spicetify 和相关软件包的 Bucket            |
| [nonportable](https://github.com/TheRandomLabs/scoop-nonportable) | 一个用于非可移植应用程序的 Bucket                            |
| [games](https://github.com/Calinou/scoop-games)              | 开源/免费游戏和游戏相关工具的 Bucket                         |
| [TheCjw/scoop-retools](https://github.com/TheCjw/scoop-retools) | 逆向工程工具的 Bucket                                        |
| [jetbrains](https://github.com/Ash258/Scoop-JetBrains)       | 包含 Jetbrians IDE 的 Bucket                                 |
| [integzz/scoopet](https://github.com/integzz/scoopet)        | 包含学术研究应用的 Bucket                                    |
| [Versions](https://github.com/ScoopInstaller/Versions)       | 包含一些知名软件包的旧版本的 Bucket                          |
| [Ash258/GenericBucket](https://github.com/Ash258/GenericBucket) | 通用的 Bucket 模板                                           |
| [kidonng/sushi](https://github.com/kidonng/sushi)            | 一个美味的、包容的 Bucket                                    |
| [rasa/scoops](https://github.com/rasa/scoops)                | 一个美味的的 Bucket                                          |
| [littleli/scoop-clojure](https://github.com/littleli/scoop-clojure) | 安装 Clojure 的 Bucket                                       |
| [MCOfficer/scoop-nirsoft](https://github.com/MCOfficer/scoop-nirsoft) | 个人收藏的 nirsoft.net-bucket，总共包含了250多个程序         |
| [kkzzhizhou/coop-apps](https://github.com/kkzzhizhou/scoop-apps) | 合并多个Scoop仓库，使用Github Action自动更新                 |
| [KNOXDEV/wsl](https://github.com/KNOXDEV/wsl)                | 一个用于 WSL 的 Bucket，不需要 Windows UWP 应用商店          |
| [Ash258/Scoop-Sysinternals](https://github.com/Ash258/Scoop-Sysinternals) | 所有分开的 Sysinternals 工具的 Bucket                        |
| [TheRandomLabs/Scoop-Bucket](https://github.com/TheRandomLabs/Scoop-Bucket) | 个人收藏的 Bucket                                            |
| [cderv/r-bucket](https://github.com/cderv/r-bucket)          | R 语言用户和软件工程师使用的个人 Bucket                      |
| [kkzzhizhou/scoop-zapps](https://github.com/kkzzhizhou/scoop-zapps) | 自用Scoop仓库，使用 Github Actions 自动更新                  |
| [tetradice/scoop-iyokan-jp](https://github.com/tetradice/scoop-iyokan-jp) | 日本語環境に最適化されたscoop bucket                         |
| [rkbk60/scoop-for-jp](https://github.com/rkbk60/scoop-for-jp) | 适合小日子过得不错的日本人的 Bucket                          |
| [ZvonimirSun/scoop-iszy](https://github.com/ZvonimirSun/scoop-iszy) | ZvonimirSun 个人收藏的 Bucket                                |
| [php](https://github.com/ScoopInstaller/PHP)                 | PHP 的 Bucket                                                |

举个例子，假如我们使用 Scoop 安装 Snipaste，使用 `scoop search [软件包名]` 查找

```
scoop search snipaste
```

可以看到下面的输出

```
Results from other known buckets...
(add them using 'scoop bucket add <name>')

'extras' bucket:
    bucket/snipaste

'versions' bucket:
    bucket/snipaste-beta
```

可以看到名为 extras 的 Bucket 含有 Snipaste，而名为 versions 的 Bucket 中含有 snipaste 的 beta 版，根据自己选择 Bucket 添加 Bucket

```
scoop bucket add versions
# 或者
scoop bucket add extras
```

强烈建议添加 `versions` 和 `extras` 两个 Bucket

然后安装对应的 Snipaste，比如

```
scoop install snipaste
# 或者 beta 版
scoop install snipaste-beta
```

对于不在官方认证的已知 Bucket，可以按照其项目文档说明来添加，比如：

```
scoop bucket add dorado https://github.com/h404bi/dorado
```

### 代理

如果你所在的网络深受中国大陆局域网的荼毒，scoop 支持 HTTP 代理

```
scoop config proxy [username:password@]host:port
# 比如无认证的本地代理
scoop config proxy 127.0.0.1:7890
# 比如有认证的服务器代理
scoop config proxy admin:password@43.54.76.98:6542
# 取消代理设置
scoop config rm proxy
```

### 缓存

默认情况下，Scoop 安装软件会缓存应用的安装包，管理 Scoop 的缓存

```
# 查看所有软件包缓存
scoop cache show
# 清除所有软件包缓存
scoop cache rm *
# 清除 <AppName> 的缓存
scoop cache rm <AppName>
# 清除所有全局安装软件的缓存和旧版本
sudo scoop cleanup -gk *
# 清除所有非全局安装软件的缓存和旧版本
scoop cleanup -k *
# 删除 <AppName> 的旧版本
scoop cleanup <AppName>
# 删除全局安装的 <AppName> 的旧版本
sudo scoop cleanup <AppName> -g
# 删除所有非全局安装应用的旧版本
scoop cleanup *
# 删除所有全局安装应用的旧版本
sudo scoop cleanup * -g
# 删除下载 <AppName> 的过期缓存
scoop cleanup <AppName> -k
# 上面的太麻烦？直接用下面一条命令一把梭
scoop cache rm * && sudo scoop cleanup -gk * && scoop cleanup * && sudo scoop cleanup * -g
```

### 其他

```
# 查看已安装应用
scoop list
# 查看 <AppName> 的信息
scoop info <AppName>
# 打开 <AppName> 的官网
scoop home <AppName>
# 查看官方认证可添加的 Bucket
bucket known
# 检查 scoop 状态
scoop checkup
# 启用调试信息
scoop config debug true
```

## 常用软件

应用清单/Bucket 列表可以 [在这](https://scoop-docs.vercel.app/apps/) 查看

```
# 流量/硬件监控
scoop install trafficmonitor
# Draw.io 绘图工具
scoop install draw.io
# 一个 RSS 阅读器
scoop install fluent-reader
# 轻量的图片查看器
scoop install imageglass
# 强大的串流、录屏工具
scoop install obs-studio
# PowerShell 7
scoop install powershell-preview
# 苏门答腊 PDF
scoop install sumatrapdf
# Telegram
scoop install telegram
# 终端增强
scoop install starship
# ISO 写录工具
scoop install rufus
# Windows Terminal
scoop install windows-terminal
# DeepL 翻译工具
scoop install deepl
# 傲梅分区软件
scoop install AoMeiPartition
# Android Studio
scoop install android-studio
# 百度云盘（快逃！）
scoop install baidunetdisk
# 安装 cpu-z gpu-z aida64
scoop install cpu-z gpu-z Aida64
# Linux 常用工具
scoop install curl wget grep touch vim gcc cmake sed less
# 钉钉
scoop install dingtalk
# DiskGenius  分区精灵
scoop install DiskGenius 
# Everything 文件索引软件
scoop install everything 
# Geek Unistaller 卸载软件
scoop install geekuninstaller 
# Chrome 浏览器
scoop install googlechrome 
scoop install gradle 
# IDM 下载工具
scoop install IDM 
scoop install innounp 
scoop install lessmsi 
# 管理 WSL 的全功能实用程序
scoop install lxrunoffline 
# JAVA maven
scoop install maven 
# Motrix 下载工具
scoop install motrix 
# Node.js
scoop install nodejs -g
# 安装 yarn
scoop install yarn
# Notepad++ 文本编辑器
scoop install notepadplusplus 
# OpenSSL
scoop install openssl
# Pandoc
scoop install pandoc 
# Postman
scoop install postman 
scoop install privoxy 
scoop install process-explorer 
# Redis 管理器
scoop install redis-desktop-manager 
# ScreenToGif 录制 Gif 工具
scoop install screentogif
# 图形化查看磁盘空间占用
scoop install SpaceSniffer 
# 切换 hosts 工具
scoop install switchhosts 
# Markdown 码字工具
scoop install typora 
# 强大的小工具集合
scoop install utools 
# VScode
scoop install vscode-portable 
# WireShark 流量分析工具
scoop install wireshark 
# Wox 一款 Windows 上快速启动器
scoop install wox 
# Windows 上空格键快速预览文件小工具
scoop install quicklook
```

差不多这些指南已经够用了，更多的自行探索吧，Enjoy it 

**参考信息：**

- [Scoop Docs](https://scoop-docs.vercel.app/)
- [~/Scoop](https://scoop.netlify.app/)



> 版权属于：**DEJAVU**
  原文链接：https://www.dejavu.moe/posts/windows-scoop
  转载时须注明出处及本声明

