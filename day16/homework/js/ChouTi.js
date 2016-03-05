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

//点赞操作

$('.change_style1').hover(function () {
    //滑进去的操作
    $(this).children('div').css("background-position","0px -18px");
},function () {
    //划出后的操作
    $(this).children('div').css("background-position","0px -38px");
});

//信息操作
$('.change_style2').hover(function () {
    //滑进去的操作
    $(this).children('div').css("background-position","0px -78px");
},function () {
    //划出后的操作
    $(this).children('div').css("background-position","0px -58px");
});

//收藏操作
$('.change_style3').hover(function () {
    //滑进去的操作
    $(this).children('div').css("background-position","0px -138px");
},function () {
    //划出后的操作
    $(this).children('div').css("background-position","0px -158px");
});



$(function(){
        //当滚动条的位置处于距顶部100像素以下时，跳转链接出现，否则消失
        $(function () {
            $(window).scroll(function(){
                if ($(window).scrollTop()>100){
                    $("#back-to-top").fadeIn(1500);
                }
                else
                {
                    $("#back-to-top").fadeOut(1500);
                }
            });

            //当点击跳转链接后，回到页面顶部位置

            $("#back-to-top").click(function(){
                $('body,html').animate({scrollTop:0},1000);
                return false;
            });
        });
    });
