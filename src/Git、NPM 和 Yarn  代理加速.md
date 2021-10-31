---
layout: post
title: Git、NPM 和 Yarn  代理加速
slug: Git_proxy
date: 2021/2/16 11:30:00
status: publish
author: 向日葵旺
categories: 
  - 编程开发
  - 环境配置

tags: 
  - Git
  - NPM
  - Yarn
  - proxy
---

## 配置Git代理

Git 同时支持 `http` 代理和 `socks5` 代理，二选一即可

```
# http代理
$ git config --global http.proxy http://server:port
$ git config --global https.proxy http://server:port
# socks5代理
$ git config --global http.proxy socks5://127.0.0.1:10808
$ git config --global https.proxy socks5://127.0.0.1:10808
```

以 CFW 代理工具为例：

```
# http代理
$ git config --global http.proxy http://127.0.0.1:10809
$ git config --global https.proxy http://127.0.0.1:10809
# socks5代理
$ git config --global http.proxy socks5://127.0.0.1:10808
$ git config --global https.proxy socks5://127.0.0.1:10808
```

取消 Git 代理：

```
$ git config --global --unset http.proxy
$ git config --global --unset https.proxy
```

## 配置NPM代理

NPM 原生支持 `http` 代理类型，但是不支持 `socks5` 代理类型，如果还想要使用 `socks5` 代理，可能还需要使用一个工具使用 `http` 监听 `socks5` 代理 （禁止套娃），此处不做讨论

```
# http代理
$ npm config set proxy http://server:port
$ npm config set https-proxy http://server:port
```

以 CFW 代理工具为例：

```
$ npm config set proxy http://127.0.0.1:10809
$ npm config set https-proxy http://127.0.0.1:10809
```

取消 NPM 代理：

```
$ npm config delete proxy
$ npm config delete https-proxy
```

## 配置Yarn代理

Yarn 原生就拥有比 NPM 更快的速度，类似 NPM，使用 `http` 代理（必要的话），打开 Terminal/Bash：

```
# http代理
$ yarn config set proxy http://server:port
$ yarn confit set https-proxy http://server:port
```

以 CFW 代理工具为例：

```
$ yarn config set proxy http://127.0.0.1:10809
$ yarn confit set https-proxy http://127.0.0.1:10809
```

取消 Yarn 代理：

```
$ yarn config delete proxy
$ yarn config delete https-proxy
```

