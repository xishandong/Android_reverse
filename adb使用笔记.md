# 此文件记录adb的使用
## 安装
此过程略，可以在网上轻易获取到
## 使用
首先我们介绍一下adb命令的基本构成
```bash
adb -s 设备 命令
```
十分简洁，我们只需要知道我们需要执行什么命令即可。

同时，如果你的设备只有一个，那么命令可以简化为
```bash
adb 命令
```

### 常用命令

我们首先需要知道启动以及结束和连接设备

``` bash
adb start-server # 启动服务
adb kill-server # 中止服务 
adb -s 设备 connect ip:host # 连接设备
```

我们使用下述命令进行查看设备

```bash
adb devices
```

这个命令可以把连接到的设备展示出来

另外例如推送文件，下载apk相关我们可以直接输入adb获取它的使用文档

下面介绍查看手机或虚拟机的cup型号的命令，会在我们使用frida时有用

```bash
adb shell getprop ro.product.cpu.abi # 查看型号
```

同时，我们可以通过下述命令进入手机的Linux终端（记得开启root哦）

```bash
adb shell
```

