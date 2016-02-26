/**
 * Created by luotim on 16/2/25.
 */


//所有的jQuery的详细注释都在

//网页头,应用跑马灯实例
function Run_going(){
    var content = document.title;
    var firstChar = content.charAt(0);
    var sub = content.substring(1,content.length);
    document.title = sub + firstChar;
    }

//定义左侧菜单栏,点击隐藏效果
function MenuChange(arg){
    //一 找到下一个标签,移除hide样式
    //$(arg).next()  下一个标签
    //removeClass('') 移除样式
    $(arg).next().removeClass('hide');
    //二 找到其他菜单,内容隐藏,添加hide
    //当前标签的父亲标签$(arg).parent()
    //所有父亲标签的兄弟标签siblings()
    $(arg).parent().siblings().find('.left_menu_content').addClass('hide');

}
//定义左侧菜单栏,子菜单栏的进/出效果
$('.left_menu_content').hover(function () {
    //滑进去的操作
    $(this).css("background-color","#84bdf6");
    $(this).addClass('left_menu_content_border');
},function () {
    //划出后的操作
    $(this).css('background-color','#ffffff');
    $(this).removeClass('left_menu_content_border')
});


//定义左侧菜单栏,子菜单栏点击,变更右侧内容效果
function ContentChange(arg){
    //var value_id = ;
    if($(arg).attr('id') == 'choose_select1'){
        $('#content_1').removeClass('hide');
        $('#content_1').parent().siblings().find('.content_master').addClass('hide');
    }

    if($(arg).attr('id') == 'choose_select2'){
        $('#content_2').removeClass('hide');
        $('#content_2').parent().siblings().find('.content_master').addClass('hide');
    }
    //var value_id = ;
    if($(arg).attr('id') == 'choose_select3'){
        $('#content_3').removeClass('hide');
        $('#content_3').parent().siblings().find('.content_master').addClass('hide');
    }

    if($(arg).attr('id') == 'choose_select4'){
        $('#content_4').removeClass('hide');
        $('#content_4').parent().siblings().find('.content_master').addClass('hide');
    }


}





//定义搜索实例效果
$('#search').focus(function () {
        $(this).val("");
        $(this).removeClass('font_color');//当获得焦点的时候添加addClass样式
    }).blur(function () {
        if($(this).val() == ''){$(this).val('请输入搜索内容');$(this).addClass('font_color')}//失去焦点的时候添加样式和value
            });


//定义多选\反选\取消实例
//全选
function CheckAll() {
    //$('#tb1').find(':checkbox').attr('checked','checked'); 这个方法也是可以的!通过属性修改,但是反选的时候有问题
    $('#tb1').find(':checkbox').prop('checked',true); //这个方法prop是专门为checkbox 而生的
}

//反选
function CheckReverse() {
    //找到/然后判断如果选中就给取消,如果没有选中就给选中
    $('#tb1').find(':checkbox').each(function () {
        //this 每一个复选框
        //$(this).prop()  如果选中为True,如果未选中为false;
        if($(this).prop('checked')){
            $(this).prop('checked',false)
        }else{
            $(this).prop('checked',true)
        }
    })
}

//取消
function CheckCancel() {
    //取消也可以用attr来做
    //$('#tb1').find(':checkbox').removeAttr('checked')
    $('#tb1').find(':checkbox').prop('checked',false)
}




//定义模态对话框
//当点击时判断用户输入的内容是否为空,如果为空提示
function SubmitForm(){
    //获取form表单中input的值
    //判断值是否为空
    var ret = true;
    //遍历所有的input,要要有控制,就讲ret设置为false
    //$('input[type="text"]') 找到所有的input标签并且类型为text的标签

    $(':text').each(function () { //找到所有的input标签并且类型为text的标签,找到的是个数组,吧数组赋值给each让他循环
        //$(this) == 要循环的每一个元素表示当前的元素or标签
        var value = $(this).val();
        if(value.trim().length == 0) { //判断取消空格"trim()",之后的字符长度为0,那么执行  注意 == 才是等于 = 是赋值!
            $(this).css('border-color','red');
            ret = false;
        }else {
            $(this).css('border-color', 'green');
        }
        });

    return ret;
}

//当点击时从form表单中的input标签中获取内容并赋值给模态对话框
function GetPrev(arg){
    var list = [];
    $.each($(arg).prevAll(),function(i) {  //循环$(arg).prevAll()这里的内容,然后把值赋值给 i 这里的function(i)
        var item = $(arg).prevAll()[i]; //获取值,如果不取获取到的是索引
        var text = $(item).text(); //取出值然后赋值给text
        list.push(text)
    });
    //反转列表
    var new_list = list.reverse();
    //把获取到的值引用到模态对话框中,赋值给value
    $('#hostname').val(new_list[0]);
    $('#ip').val(new_list[1]);
    $('#port').val(new_list[2]);

    $('#dialog').removeClass('hide');
}

//取消的操作,隐藏模态对话框
function CanCel() {
    $('#dialog').addClass('hide')
}