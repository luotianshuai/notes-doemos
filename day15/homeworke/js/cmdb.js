/**
 * Created by luotim on 16/2/25.
 */

//网页头,应用跑马灯实例
function Run_going(){
    var content = document.title;
    var firstChar = content.charAt(0);
    var sub = content.substring(1,content.length);
    document.title = sub + firstChar;
    }