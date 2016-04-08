/**
 * Created by wupeiqi on 15/8/13.
 */
$(function () {
    $.InitMenu('#left_menu_user_group');
    Initialize('#table-body',1);
});


/*
刷新页面
*/
function Refresh(){
    //get current page
    var currentPage = GetCurrentPage('#pager');
    Initialize('#table-body',currentPage);
}

/*
获取当前页码（根据分页css）
 */
function GetCurrentPage(pager) {
    var page = $(pager).find("li[class='active']").text();
    return page;
}

/*
搜索提交
*/
function SearchSubmit(){
    Initialize('#table-body',1);
}

/*
*页面跳转
*/
function ChangePage(page){
    Initialize('#table-body',page);
}

/*
更新资产（退出编辑状态;获取资产中变更的字段；提交数据；显示状态）
*/
function Save(){

    if($('#edit_mode_target').hasClass('btn-warning')){
        $.TableEditMode('#edit_mode_target','#table-body');
    }

    var target_status = '#handle_status';
    //get data
    var updateData = [];
    $('#table-body').children().each(function(){
        var rows = {};
        var id = $(this).attr('auto-id');
        var num = $(this).attr('num');
        var flag = false;
        $(this).children('td[edit-enable="true"]').each(function(){
            var origin = $(this).attr('origin');
            var newer = $(this).text();
            var name = $(this).attr('name');

            if(newer && newer.trim() && origin != newer){
                rows[name] = newer;
                flag = true;
            }
        });
        if(flag){
            rows["id"] = id;
            rows["num"] = num;
            updateData.push(rows);
        }
    });
    if(updateData.length<1){
        return;
    }
    //submit data
    updateData = JSON.stringify(updateData);


    $.ajax({
        url:'/userinfo/usergroup_modify/',
        type:'POST',
        traditional:true,
        data:{'data':updateData},
        success: function (callback) {
            callback = $.parseJSON(callback);
            if(callback.status == 1){
                //success
                SuccessHandleStatus(target_status,callback.data);
            }else{
                ErrorHandleStatus(target_status,callback.data,callback.message);
            }
            Refresh();
        },
        error:function(){
            alert('请求错误.');
            Refresh();
        }

    });


}


/*
聚合搜索条件
*/
function AggregationSearchCondition(conditions){
    var ret = {};
    var $condition = $(conditions).find("input[is-condition='true']");
    var name = $condition.attr('name');
    var value = $condition.val();
    if(!$condition.is('select')){
        name = name + "__contains";
    }
    if(value) {
        var valList = $condition.val().trim().replace('，', ',').split(',');
        if (ret[name]) {
            ret[name] = ret[name].concat(valList);
        } else {
            ret[name] = valList;
        }
    }
    return ret;
}

/*
页面初始化（获取数据，绑定事件）
*/
function Initialize(tBody,page){
    $.Show('#shade,#loading');
    // 获取所有搜索条件

    var conditions = JSON.stringify(AggregationSearchCondition('#search_conditions'));
    var $body = $(tBody);
    var searchConditions = {};
    var page = page;

    $.ajax({
        url:'/userinfo/usergroup_list/',
        type:'POST',
        traditional:true,
        data:{'condition':conditions,'page':page},
        success:function(callback){

            callback = $.parseJSON(callback);
            //embed table
            EmbedIntoTable(callback.vlan, callback.start, "#table-body");


            //ResetSort()
            $.ResetTableSort('#table-head',"#table-body");

            //pager
            CreatePage(callback.pager,'#pager');

            //create global variable
            //InitGlobalDict(callback);

            //bind function and event
            $.BindTableSort('#table-head','#table-body');
            $.BindDoSingleCheck('#table-body');
            $.Hide('#shade,#loading');

        },
        error:function(){
            $.Hide('#shade,#loading');
        }
    })

}

/*
将后台ajax数据嵌套到table中
*/
function EmbedIntoTable(response,startNum,body){
    if(!response.status){
        alert(response.message);
    }else{
        //清除table中原内容
        $(body).empty();
        $.each(response.data,function(key,value){
            var tds = [];
            tds.push($.CreateTd({},{},$.CreateInput({'type':'checkbox'},{})));
            tds.push($.CreateTd({},{},startNum + key + 1));
            tds.push($.CreateTd({'edit-enable':'true','edit-type':'input','name':'name','origin':value.name},{}, value.name));
            tds.push($.CreateTd({'edit-enable':'false','edit-type':'input','name':'user_count','origin':value.user_count},{}, $.CreateA({'href':"/userinfo/usergroup/"+value.id+'/'},{},value.user_count)));
            var tr = $.CreateTr({'auto-id':value.id,'num':startNum + key + 1},{},tds);

            $(body).append(tr);

        })

    }
}


/*
创建分页信息
*/
function CreatePage(data,target){
    $(target).empty().append(data);
}


/*
更新资产错误，显示错误信息
 */
function ErrorHandleStatus(target,content,errorList){
    $(target).attr('data-toggle','popover');

    var errorStr = '';
    $.each(errorList,function(k,v){
        errorStr = errorStr + v.num + '. '+ v.message + '</br>';
    });

    $(target).attr('data-content',errorStr);
    $(target).popover();

    var msg = "<i class='fa fa-info-circle'></i>" + content;
    $(target).empty().removeClass('btn-success').addClass('btn-danger').html(msg);

}

/*
更新资产成功，显示更新信息
 */
function SuccessHandleStatus(target,content){
    $(target).popover('destroy');

    var msg = "<i class='fa fa-check'></i>" + content;
    $(target).empty().removeClass('btn-danger').addClass('btn-success').html(msg);
    setTimeout(function(){ $(target).empty().removeClass('btn-success btn-danger'); },5000);
}


/*
删除资产
*/
function DoDeleteVlan(){
    var target_status = '#handle_status';
    var table_body = '#table-body';
    var rows = [];

    $(table_body).find('input:checked').each(function(){
        var id = $(this).parent().parent().attr('auto-id');
        var num = $(this).parent().parent().attr('num');
        rows.push({'id':parseInt(id),'num':parseInt(num)});
    });

    rows = JSON.stringify(rows);
    $.ajax({
        url: '/userinfo/usergroup_del/',
        type: 'POST',
        traditional: true,
        data: {'rows': rows},
        success:function(callback){
            $.Hide('#shade,#modal_delete');
            callback = $.parseJSON(callback);
            if(callback.status == 1){
                //success
                SuccessHandleStatus(target_status,callback.data);
            }else{
                ErrorHandleStatus(target_status,callback.data,callback.message);
            }
            Refresh();
        }
    });
}

/*
添加VLAN-取消
*/
function CancelModal(container){
    $("#do_add_form").find('input').val('');
    $('#do_add_modal').modal('hide')
}

/*
添加VLAN-提交
*/
function SubmitModal(formId,statusId){
    var data_dict = {};
    $(formId).find('input[type="text"]').each(function(){
        var name = $(this).attr('name');
        var val =  $(this).val();
        data_dict[name] = val
    });
    ClearLineError(formId,statusId);
    $.ajax({
        url: '/userinfo/usergroup_add/',
        type: 'POST',
        traditional: true,
        data: data_dict,
        success:function(callback){
            callback = $.parseJSON(callback);
            if(callback.status){
                CancelModal();
                Refresh();
            }else{
                if(callback.summary){
                    SummaryError(callback.summary,statusId);
                }
                if(callback.error){
                    LineError(callback.error,formId);
                }
            }
        }
    });
}

/*
清除所有行下的错误信息
 */
function ClearLineError(formId,statusId){
    $(statusId).empty();
    $(formId).find('div[class="form-error"]').remove();
}

/*
添加行错误信息
 */
function LineError(errorDict,formId){
    //find all line，add error
    $.each(errorDict,function(key,value){
        var errorStr = '<div class="form-error">'+ value[0]['message'] +'</div>';
        $(formId).find('input[name="'+key+'"]').after(errorStr);
    });
}
/*
添加整体错误信息
 */
function SummaryError(errorStr,statusId){
    $(statusId).text(errorStr);
}

