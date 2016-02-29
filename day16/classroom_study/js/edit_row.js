/**
 * Created by luotim on 16/2/28.
 */

//编辑模式

function EditMode(ths,tb){
    //ths = this;
    var isEditing = $(ths).hasClass('editing');
    if(isEditing){
        $(ths).text('进入编辑模式');
        //如果有有editing这个样式,移除
        $(ths).removeClass('editing');
        //退出编辑模式
        $(tb).children().each(function () {
            var tr = $(this);
            if(tr.find(':checkbox').prop('checked')){
                //当前行,退出编辑状态
                tr.children().each(function () {
                    var td = $(this);
                    if(td.attr('edit') == 'true'){
                        var inp = td.children(':first');
                        var input_value = inp.val();
                        td.text(input_value)
                    }
                })
            }
        })


    }else{
        $(ths).text('退出编辑模式');
        //如果没有这个editing这个样式,添加
        $(ths).addClass('editing');
        $(tb).children().each(function () {
            //$(this)表示循环过程中,每一个tr,每一行数据
            var tr = $(this);
            var isChecked = $(this).find(':checkbox').prop('checked');
            if(isChecked == true){
                //当前行进入编辑状态
                tr.children().each(function () {
                    var td = $(this);
                    if(td.attr('edit') == 'true'){
                        var text = td.text();
                        var temp = "<input type='text' value='" + text + "'/>"
                        td.html(temp)
                    }
                })
            }
        })
    }
}


//全选

function CheckAll(mode,tb) {
    //如果选中checkbox
    //如果已经进入编辑模式,让选中行进入编辑模式
    //tb = #tb1
    //$(tb) = $(#tb1)

    $(tb).children().each(function () {
        //$(this) 表示循环过程中,每一个tr,每一行数据
        var tr = $(this);
        //找到到tr下面的td,选中的
        var isChecked = $(this).find(':checkbox').prop('checked');
        //判断是否被选中
        if(isChecked==true){
            //如果被选中,什么都不做
        }else{
            //如果没有被选中
            $(this).find(':checkbox').prop('checked',true);
            //判断是否进入编辑模式,如果进入编辑模式,让选中行进入编辑模式
            var isEditMode = $(mode).hasClass('editing');
            if(isEditMode){
                //行进行进入编辑状态
                tr.children().each(function() {
                    var td = $(this);
                    if(td.attr('edit')=='true'){
                        var text = td.text();
                        console.log(text);
                        var temp = "<input type='text' value='" + text + "' />";
                        //var temp = "<input value='"+text+"'/>";
                        td.html(temp);
                    }
                })
            }
        }
    })
}



//取消

function CheckCancel(mode,tb){
    //取消消肿checkbox
    //如果已经进入编辑模式,行退出编辑状态
    $(tb).children().each(function () {
        var tr = $(this);
        if(tr.find(':checkbox').prop('checked')){
            //移除选中
            tr.find(':checkbox').prop('checked',false);
            //获取判断是否进入编辑模式
            var isEditing = $(mode).hasClass('editing');
            if(isEditing == true){
                //当前行,退出编辑状态
                tr.children().each(function () {
                    var td = $(this);
                    if(td.attr('edit')=='true'){
                        var inp = td.children(':first');
                        var input_value = inp.val();//获取当前input的标签
                        td.text(input_value);//替换input为text值
                    }
                })
            }
        }
    })
}

//反选
function CheckReverse(mode,tb){
    //判断是否进入编辑模式
    if($(mode).hasClass('editing')){
        $(tb).children().each(function () {
            //遍历所有tr
            var tr = $(this);
            var check_box = tr.children().find(':checkbox');
            //判断是否被选中
            if(check_box.prop('checked')){
                //选中执行
                check_box.prop('checked',false);
                tr.children().each(function () {
                    var td = $(this);
                    //如果他在编辑状态并且他为可编辑的那么,那么他肯定是input的标签,所以改为text
                    if(td.attr('edit')  == 'true'){
                        var inp = td.children(':first');
                        var input_value = inp.val();
                        td.text(input_value);
                    }


                });
            }else{
                check_box.prop('checked',true);
                tr.children().each(function () {
                    var td = $(this);
                    if(td.attr('edit') == 'true'){
                        var text = td.text();
                        var temp = "<input type='text' value='" + text + "' />";
                        td.html(temp);
                    }
                })
            }
        });
    }else{
        //如果没有进入编辑模式就正常的对checked进行操作即可
        $(tb).children().each(function () {
            var tr = $(this);
            var check_box = tr.children().first().find(':checkbox');
            if(check_box.prop('checked')){
                check_box.prop('checked',false);
            }else{
                check_box.prop('checked',true);
            }
        });
    }
}

































































