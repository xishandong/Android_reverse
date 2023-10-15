# 此文件记录frida的使用

## 电脑安装frida
```bash
pip install frida
pip install frida-tools
```
十分简单
## 手机安装frida
首先我们需要确定手机的cpu类型

模拟器通常是: x86_64

真机通常是: arm

我们根据不同的型号去frida的github下载对应的frida-sever

下面附录frida的github链接: https://github.com/frida/frida

我们下载好之后需要解压然后推送到手机中
```bash
adb -s 设备 push  xx/xxx/xxx/frida-server  /sdcard # 首先推送到一个用户目录然后在安卓的Linux推送到系统中
adb shell       # 进入手机
su -            # 获得root权限
mv /sdcard/frida-server  /data/local/tmp # 移动到系统文件
cd /data/local/tmp # 进入目录
chmod 777 frida-server # 赋予最高权限
./frida-server # 开启服务
```
在安卓开启frida服务之前，我们记得在电脑上开启tcp转发
```bash
adb forward tcp:27042 tcp:27042
adb forward tcp:27043 tcp:27043
```

## 下面介绍一些固定的格式
### 获取连接设别的信息，确认包名
```python
import frida

rdev = frida.get_remote_device()
print(rdev)

processes = rdev.enumerate_processes()
for process in processes:
    print(process)

front_app = rdev.get_frontmost_application()
print(front_app)

```
### hook类中的方法
这个是hook的类的方法没有重载的情况
```python
import frida
import sys

rdev = frida.get_remote_device()
# app名称或者app包名称
session = rdev.attach("com.shizhuang.duapp")

# 目标：指定替换是那个包中的方法名
#   - 包名称：com.shizhuang.duapp.common.utils
#   - 类名称：RequestUtils
#   - 方法名：c        m30623c-jadx工具给你创造的。
#       - 参数1：map<string,string>
#       - 参数2：long
scr = """
Java.perform(function () {
    // 导入类, 看文件最顶部的package
    var RequestUtils = Java.use("com.shizhuang.duapp.common.utils.RequestUtils");

    // 找到类中的方法进行hook
    RequestUtils.c.implementation = function(map,j){
        console.log("666");
        var res = this.c(map,j);
        console.log("999");
        return res;
    }    

});
"""
script = session.create_script(scr)


def on_message(message, data):
    print(message, data)


script.on("message", on_message)

script.load()
sys.stdin.read()
```
下面是类中的函数具有重载的情况
```python

scr = """
Java.perform(function () {
    // 导入类
    var RequestUtils = Java.use("com.douban.frodo.network.ApiSignatureHelper");
    
    // 找到类中的方法进行hook,然后加上overload参数类型即可
    RequestUtils.a.overload('java.lang.String', 'java.lang.String', 'java.lang.String').implementation = 
    function(str, str1, str2){
        console.log(str, str1, str2);
        var res = this.a(str, str1, str2);
        console.log(res);
        return res;
    }

});
"""
script = session.create_script(scr)
```
### 下面是hook so层代码的情况
> so层代码的hook需要在真机下才可以，因为默认只有arm芯片，不支持x86_64
>
```python
scr = """
Java.perform(function () {    
    var addr_func = Module.findExportByName("libJNIEncrypt.so", "AES_128_ECB_PKCS5Padding_Encrypt");
    Interceptor.attach(addr_func, {
        onEnter: function(args){
        	// 进入并执行函数：AES_128_ECB_PKCS5Padding_Encrypt，args就是参数
            console.log("-------------参数 1-------------");
            console.log(args[0].readUtf8String())
            
            console.log("-------------参数 2-------------");
            console.log(args[1].readUtf8String());
        },
        onLeave: function(retValue){
            console.log("-------------返回-------------");
            console.log(retValue.readUtf8String());
        }
    })
});
"""
script = session.create_script(scr)
```
> 小总结：
> 
> frida hook参数函数的时候，前面的基本都不变，只是hook脚本会发送改变