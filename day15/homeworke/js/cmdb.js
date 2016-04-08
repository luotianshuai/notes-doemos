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
function CheckAll_1() {
    //$('#tb1').find(':checkbox').attr('checked','checked'); 这个方法也是可以的!通过属性修改,但是反选的时候有问题
    $('#tb1').find(':checkbox').prop('checked',true); //这个方法prop是专门为checkbox 而生的
}

//反选
function CheckReverse_1() {
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
function CheckCancel_1() {
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


//作业js
//作业全选
function CheckAll() {
    //$('#tb1').find(':checkbox').attr('checked','checked'); 这个方法也是可以的!通过属性修改,但是反选的时候有问题
    $('#table_list').find(':checkbox').prop('checked',true); //这个方法prop是专门为checkbox 而生的
    //找到所有选中的td并循环
    if($('#select').attr('status') == 'on'){ //判断编辑模式是否选中，如果选中执行
        //找到ID为cmdb_form，下面所有选中了的标签下的td标签,但是刨除序列号$('#cmdb_form').find(':checkbox').parent().nextAll().not('.cselect')

        $('#table_list').find(':checkbox').parent().nextAll().not('.cselect').each(function () {
            //循环取出的每一个td标签，并获取里面的值
            // 并且判断td标签内的孩子是否为input，如果是什么都不做，如果不是执行修改字符串为input标签
            if($(this).children().is('input')){console.log('The children type is input so do not running coding')}else{
            var old = $(this).text();
            //对取出来的值进行拼接
            var temp ="<input value='"+old+"'>";
            //然后赋值
            $(this).html(temp);}
        })

        }
}

//作业反选
function CheckReverse() {
    //找到input标签为checkbox 然后判断如果选中就给取消,如果没有选中就给选中
    $('#table_list').find(':checkbox').each(function () {

        //首先判断是否为编辑状态
        if($('#select').attr('status') == 'on'){
        //如果为编辑状态
        if($(this).prop('checked')){
            //如果选中了，首先把他的选中状态取消并且，把他的input标签改为字符串类型
            // 状态给为取消
            $(this).prop('checked',false);
            //把父级别下面的所有input标签改为字符串
            $(this).parent().nextAll().not('.cselect').each(function () {
                //取出input标签内的内容
                var input_info = $(this).children().val();
                //并赋值给td标签
                $(this).html(input_info);
            });}else{
            //如果没有选中，首先把他的状态改为选中，并且把他的字符串赋值给input标签
            //改为选中
            $(this).prop('checked',true);
            //并把兄父级别下面的字符串赋值给input标签
            $(this).parent().nextAll().not('.cselect').each(function () {
                //取出他的值来
                var old = $(this).text();
                //对取出来的值进行拼接
                var temp ="<input value='"+old+"'>";
                //然后赋值
                $(this).html(temp);})
            }}else{
            //如果不是编辑状态
            if($(this).prop('checked')){
                //如果不是编辑状态把选中的给取消
                $(this).prop('checked',false);
            }else{
                //如果不是编辑状态把未选中的给选中
                $(this).prop('checked',true);
            }}
        })
}

//作业取消
function CheckCancel() {
    //取消也可以用attr来做
    //$('#tb1').find(':checkbox').removeAttr('checked')
    $('#table_list').find(':checkbox').prop('checked',false);
    //不管是选中，只要点击取消我就去找到所有的td转为input的标签全部转回td标签
    $('#cmdb_form').find(':checkbox').parent().nextAll().not('.cselect').find(':input').each(function () {
        var input_info = $(this).val();
        $(this).parent().html(input_info);
    })
}

//编辑按钮功能
$('#select').toggle(
        //进入编辑模式执行的function
        function () {
            $(this).addClass('select_color');
            $(this).attr('status','on');
            console.log($(this).attr('status'))
        },
        function () {
            //退出编辑模式执行的function
            $(this).removeClass('select_color');//移除按钮上的样式
            $(this).removeAttr('status');//删除自定义属性
            //不管是选中，只要你退出编辑模式我就去找到所有的td转为input的标签全部转回td标签
            //并判断值是否为空
            $('#cmdb_form').find(':checkbox').parent().nextAll().not('.cselect').find(':input').each(function () {
                if($(this).val().length == '0'){alert('Sorry the value can not be null')}else{
                    var input_info = $(this).val();
                    $(this).parent().html(input_info);
                    $('.cmdbchose').prop('checked',false)
                }

            })}
);

//定义单选功能
$('.cmdbchose').click(function () {
    //判断是否为编辑模式
    if($('#select').attr('status') == 'on'){
        if($(this).prop('checked')){
            //如果被选中了，取消选中并把input标签内的value取出并改为字符串
            //alert('is chose')
            //找到当前父标签的兄弟标签并刨除.cselect类的标签
            $(this).parent().siblings().not('.cselect').each(function () {
                var old = $(this).text();
                //对取出来的值进行拼接
                var temp ="<input value='"+old+"'>";
                //然后赋值
                $(this).html(temp);
            })
        }else{
            //如果没有被选中，选中并把字符串取出来赋值给input标签
            //alert('not be chose')
            //如果没有被选中，找到父亲标签的兄弟标签，并取出里面的input的value并改为字符串
            $(this).parent().siblings().not('.cselect').each(function () {
                console.log($(this));
                var input_info = $(this).children().val();
                $(this).html(input_info);
            })
    }}
});

//定义作业保存按钮功能

function save_woker(){
    //找到input标签为checkbox 然后判断如果选中就给取消,如果没有选中就给选中
    $('#table_list').find(':checkbox').each(function () {
        //判断是否为编辑状态
        if($('#select').attr('status') == 'on'){
            //判断这个标签是否为选中状态
            if($(this).prop('checked')){
                //判断值是否空，
                            //如果为空，报警
                            //如果不为空然后把input标签的内容写入text，然后取消选中状态
                //把父级别下面的所有input标签刨除..cselect标签的所有标签
                $(this).parent().nextAll().not('.cselect').each(function () {
                    //判断，任意一个值为空都不行
                    if($(this).children().val().length == '0'){(alert('Sorry the value can not be null'))}else{
                        //如果值不为空，那么保存
                        //取出input标签内的内容
                        var input_info = $(this).children().val();
                        //并赋值给td标签
                        $(this).html(input_info);
                        console.log($(this))
                    }

                });
                //保存完成之后，取消所有选中项目
                $('#table_list').find(':checkbox').prop('checked',false)
            }
        }
    });
    }