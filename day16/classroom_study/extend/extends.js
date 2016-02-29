/**
 * Created by luotim on 16/2/28.
 */

//扩展用自执行函数来写,逼格比较高点
(function (arg) {
    arg.extend({
        'luotianshuai':function (){
            return 123;
        },
        'login':function(){}  //他的代码是以字典形式存储的扩展jQuery
    })
})(jQuery);//jQuery为传进去的函数他的方程式:(function (arg) {})();第一个括号为函数,第二个括号内存储参数