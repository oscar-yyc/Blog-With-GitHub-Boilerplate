---
layout: post
title: MySQL 8.0.18安装教程(windows 64位)
slug: MySQL_install
date: 2020/2/10 16:30:00
status: publish
author: Wainic
categories: 
  - 编程开发
  - 软件安装

tags: 
  - MySQL
---

## 下载MySQL安装文件

MySQL下载网址：https://dev.mysql.com/downloads/mysql/

已经下载好的压缩包：
[百度云提取码：dcwb](https://pan.baidu.com/s/1afSZBMSsIn9JOLCLvYfO_w)

[微云](https://share.weiyun.com/7imJMKW7)

页面呈现的是MySQL的最新版本，下载8.0.18版本还需要点击`Archives`

![ ](https://gallery.dachunwang.top/img/14a2fx.png)

版本选择`8.08.8`，系统选择`Windows`，下载`Windows (x86, 64-bit), ZIP Archive`

![ ](https://gallery.dachunwang.top/img/14wkad.png)

 下载完成以后，首先到C盘根目录创建一个MySQL文件夹

![ ](https://gallery.dachunwang.top/img/14O4vq.png)

将下载好的压缩包解压到刚刚创建的目录，解压好以后是这样

![ ](https://gallery.dachunwang.top/img/14XCVO.png)

## 创建配置文件

创建一个文本文件my.ini（新建文本文件，将文件类型改为的.ini）

![ ](https://gallery.dachunwang.top/img/14Xts0.png)

双击打开这个文件，将下面的文本复制进去并保存

```CODE
[mysqld]
# 设置3306端口
port=3306
# 设置mysql的安装目录
basedir=C:\\MySQL\\mysql-8.0.18-winx64 
# 设置mysql数据库的数据的存放目录
datadir=C:\\MySQL\\mysql-8.0.18-winx64\\data
# 允许最大连接数
max_connections=200
# 允许连接失败的次数。这是为了防止有人从该主机试图攻击数据库系统
max_connect_errors=10
# 服务端使用的字符集默认为utf8mb4
character-set-server=utf8mb4
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
# 默认使用“mysql_native_password”插件认证
default_authentication_plugin=mysql_native_password
[mysql]
# 设置mysql客户端默认字符集
default-character-set=utf8mb4
[client]
# 设置mysql客户端连接服务端时默认使用的端口
port=3306
default-character-set=utf8mb4
```

![ ](https://gallery.dachunwang.top/img/14XLef.png)

## 配置环境变量

也可以右击`我的电脑`，选择`属性`点击`高级系统设置`——选择`环境变量`——单击`系统变量`上的`Path`接着点击`编辑`点击`编辑文本`，点击`确定`

![ ](https://gallery.dachunwang.top/img/1jM9Yj.png)

在`变量值`最后面输入

```CODE
;C:\MySQL\mysql-8.0.18-winx64\bin
```

> ;后面的是你MySQl的bin路径

然后点击**确定**即可。

![ ](https://gallery.dachunwang.top/img/1jMFlq.png)

## 初始化MySQL

> 在安装时，避免出错我们尽量全部使用管理员身份运行cmd，否则在安装时会报错，会导致安装> > 失败的情况。一定要使用管理员身份运行cmd，否则会出错!!!

在搜索栏输入`cmd`选择`以管理员身份运行`即可

![ ](https://gallery.dachunwang.top/img/Snipaste_2020-07-04_21-55-33.png)

也可以在`C:\Windows\System32`中，右击`以管理员身份打开`。

![ ](https://gallery.dachunwang.top/img/14vZHf.png)

在安装前应该查看端口3306是否被占用。

在cmd端输入：

```CODE
netstat -ano
```

![ ](https://gallery.dachunwang.top/img/14vGD0.png)

接下来输入：

```CODE
cd C:\MySQL\mysql-8.0.18-winx64\bin
```

> cd 后面是bin文件存放位置,也就是打开后进入mysql的bin目录

![ ](https://gallery.dachunwang.top/img/14xBFS.png)

继续输入

```CODE
mysqld --initialize --console
```

![ ](https://gallery.dachunwang.top/img/14zlmq.png)

> 注意！root @ localhost：后面的**?vo!se;t<2=Y**就是初始密码（不含首位空格）。在没有更改密码前，需要记住这个密码，后续登录需要用到。复制密码先保存起来!!!

## 安装MySQL服务 + 启动MySQL 服务

安装mysql服务执行下面的命令：

```CODE
mysqld --install [服务名]
```

> （服务名可以不加，不加默认为mysql）

> 出现Service successfully installed.代表成功了
> ![ ](https://gallery.dachunwang.top/img/15SjRe.png)

> 如果出现了
> The service already exists!
> The current server installed: C:\MySQL\mysql-8.0.18-winx64\bin\mysqld MySQL
> ![ ](https://gallery.dachunwang.top/img/15pGz4.png)

这是由于之前已经安装过mysql并且没有删除干净

输入下面命令删除该mysql即可

```CODE
sc delete mysql
```

![ ](https://gallery.dachunwang.top/img/159PX9.png)

删除以后再执行上面的安装命令

![ ](https://gallery.dachunwang.top/img/15SjRe.png)

服务安装成功之后通过下面命令启动MySQL的服务

```CODE
net start mysql
```

![ ](https://gallery.dachunwang.top/img/159sA0.png)

## 连接MySQL + 修改密码

首先访问网址：https://www.navicat.com.cn/download/navicat-premium

下载安装一个Navicat Premium

![ ](https://gallery.dachunwang.top/img/15iN9K.png)

安装完成后打开软件，点击`文件`——`新建连接`——`MySQL`

![ ](https://gallery.dachunwang.top/img/15FzQS.png)

将刚刚复制保存下来的root @ localhost：后面的初始密码复制粘贴到密码

点击`测试连接`

![ ](https://gallery.dachunwang.top/img/15kX79.png)
![ ](https://gallery.dachunwang.top/img/15kO0J.png)

## 修改密码

使用cmd下输入下面命令进行数据库连接

```MySQL
mysql -u root -p
```

接着在`Enter password`后面输入你的初始密码

> （注意是输入进去，无法粘贴）

![ ](https://gallery.dachunwang.top/img/15EjRx.png)

出现 `mysql>` 这个的时候  你就可以输入下面命令进行修改密码了

```MySQL
ALTER USER 'root'@'localhost' IDENTIFIED BY '新密码';
```

![ ](https://gallery.dachunwang.top/img/15VJS0.png)

修改完密码以后输入下面命令就可以退出mysql了

```MySQL
exit;
```

![ ](https://gallery.dachunwang.top/img/15Vrf1.png)