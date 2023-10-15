import frida
import sys

rdev = frida.get_remote_device()
session = rdev.attach("豆瓣")


scr = """
Java.perform(function () {
    // 导入类
    var RequestUtils = Java.use("com.douban.frodo.network.ApiSignatureHelper");
    var encrypted = Java.use("com.douban.frodo.utils.crypto.HMACHash1");
    var apiKey = Java.use("com.douban.ad.utils.ApiUtils")
    
    // 找到类中的方法进行hook
    RequestUtils.a.overload('java.lang.String', 'java.lang.String', 'java.lang.String').implementation = 
    function(str, str1, str2){
        console.log(str, str1, str2);
        var res = this.a(str, str1, str2);
        console.log(res);
        return res;
    }
    encrypted.a.implementation = function(str, str1){
        console.log(str, str1)
        var res = this.a(str, str1)
        console.log(res);
        return res;
    }    
    apiKey.getApiKey.implementation = function(context){
        console.log(context)
        var res = this.getApiKey(context)
        console.log(res);
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
