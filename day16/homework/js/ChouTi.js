/**
 * Created by luo_t on 3/4/2016.
 */


//定义跑马灯实例
function Run_going(){
    var content = document.title;
    var firstChar = content.charAt(0);
    var sub = content.substring(1,content.length);
    document.title = sub + firstChar;
    }
