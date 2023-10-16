import frida

rdev = frida.get_remote_device()
session = rdev.attach("名称")


# 整体思路和hook差不多，但是需要在rpc里面进行导出
src = """
rpc.exports = {
    CustomizationFunctionName: function(参数列表) {
        var res;
        Java.perform(function(){
           var CustomizationObjectName = Java.use("包名.类名");
           res = CustomizationObjectName.函数名(参数列表); 
        });
        return res;
    }
}

"""

script = session.create_script(src)
script.load()

wanna_args = script.exports_sync.CustomizationFunctionName("参数列表")
print(wanna_args)

