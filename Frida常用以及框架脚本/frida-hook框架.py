import frida
import sys

rdev = frida.get_remote_device()
# app名称或者app包名称
session = rdev.attach("com.shizhuang.duapp")

# 目标：指定替换是那个包中的方法名
#   - 包名称：com.shizhuang.duapp.common.utils
#   - 类名称：RequestUtils
#   - 方法名：c        m30623c-jadx工具给你创造的。
#   - 类名称.方法名.implementation = function(方法的参数列表){var res = this.方法(参数);return res}
#   - 如果是由重载的函数，那么需要携带参数类型，详情可以看frida的报错信息
#   - 这里给一个具体的例子RequestUtils.a.overload('java.lang.String', 'java.lang.String', 'java.lang.String').implementation
scr = """
Java.perform(function () {
    // 导入类
    var RequestUtils = Java.use("包名.类名");

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
