// hook 添加params试图定位添加newsign的地方
Java.perform(function () {
    // 导入类
    var RequestUtils = Java.use("com.shizhuang.duapp.common.helper.net.ParamsBuilder");

    // 找到类中的方法进行hook
    RequestUtils.addParams.overload('java.lang.String', 'java.lang.Object').implementation = function(str, str1){
        console.log(str, str1);
        showStacks()
        var res = this.addParams(str, str1);
        return res;
    }
})
// 定位加密点
Java.perform(function () {
    // 导入类
    var RequestUtils = Java.use("com.duapp.aesjni.AESEncrypt");

    // 找到类中的方法进行hook
    RequestUtils.encode.implementation = function (obj, str) {
    console.log('=================================================')
       console.log('obj', obj);
       console.log('str', str);
       console.log('=================================================')
        var res = this.encode(obj, str);
        console.log(res)
        console.log('=================================================')
        showStacks()
        console.log('=================================================')
        return res;
    }
})
// 显示调用栈
function showStacks() {
    Java.perform(function () {
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
    });
}