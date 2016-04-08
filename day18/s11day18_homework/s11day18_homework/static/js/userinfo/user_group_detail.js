/**
 * Created by wupeiqi on 15/8/13.
 */
$(function () {
    $.InitMenu('#left_menu_user_group');
    Init()

});

function Init(){
    var OthersData = [];
    var SelectedData = [];

    $('#othersAsset select').children().each(function(){
        var id = $(this).attr('value');
        var text = $(this).text();
        OthersData.push({'id':id,'text':text});

    });

    $('#currentAsset select').children().each(function(){

        var id = $(this).attr('value');
        var text = $(this).text();
        SelectedData.push({'id':id,'text':text});

    });

    $('#othersAsset').data('AssetList',OthersData);
    $('#currentAsset').data('AssetList',SelectedData);

}

/* 添加关联关系
 */
function AddReleation(){
    //异步请求，添加
    //页面移动（添加和删除）
    var oldsel = $('#othersAsset select').val();
    var sel = JSON.stringify(oldsel);
    var id = $("#caption").attr('value');
    $.Show("#shade,#loading");

    $.ajax({
        url:'/userinfo/group_relation_add/',
        type:'POST',
        dataType: "json",
        traditional:true,
        data:{id:id,data:sel},
        success:function(args){
            var status = args.status;
            var message = args.message;
            if(status){
                //全部执行成功
                $("#handlestatus").removeClass('import-failed').addClass('import-success').text(message);

                var temp = [];
                $.each($('#othersAsset').data('AssetList'),function(k,v){
                    if(oldsel.indexOf(v.id)!=-1){
                        $('#othersAsset select').find("option[value='"+v.id+"']").appendTo('#currentAsset select');
                        $('#currentAsset').data('AssetList').push({'id':v.id,'text':v.text});
                    }else{
                        temp.push(v);
                    }
                });
                $('#othersAsset').data('AssetList',temp);

            }else{
                var data = args.Data;
                $("#handlestatus").removeClass('import-success').addClass('import-failed').text(message);
            }

            var height = document.getElementById("SelectCurrentAsset").scrollHeight;
            $("#SelectCurrentAsset").scrollTop(height)

            $.Hide("#shade,#loading");
            setTimeout('RemoveStatus()',3000);
        },
        error:function(){
            $.Hide("#shade,#loading");
            alert('请求异常.');
        }
    });


}
/* 移除关联关系
 */
function RemoveReleation(){
    var oldsel = $('#currentAsset select').val();
    var sel = JSON.stringify(oldsel);

    var id = $("#caption").attr('value');
    $.Show("#shade,#loading");
    //异步请求，添加
    //页面移动（添加和删除）
    $.ajax({
        url:'/userinfo/group_relation_del/',
        type:'POST',
        dataType: "json",
        traditional:true,
        data:{id:id,data:sel},
        success:function(args){
            var status = args.status;
            var message = args.message;
            if(status){
                $("#handlestatus").removeClass('import-failed').addClass('import-success').text(message);
                var temp = [];
                $.each($('#currentAsset').data('AssetList'),function(k,v){
                    if(oldsel.indexOf(v.id)!=-1){
                        //已选中
                        $('#currentAsset select').find("option[value='"+v.id+"']").appendTo('#othersAsset select');
                        $('#othersAsset').data('AssetList').push({'id':v.id,'text':v.text});
                    }else{
                        //未选中
                        temp.push(v);
                    }
                });
                $('#currentAsset').data('AssetList',temp);

            }else{
                var data = args.Data;
                //请求异常，啥都不干
                $("#handlestatus").removeClass('import-success').addClass('import-failed').text(message);
            }

            var height = document.getElementById("SelectOthersAsset").scrollHeight;
            $("#SelectOthersAsset").scrollTop(height);
            $.Hide("#shade,#loading");
            setTimeout('RemoveStatus()',3000);
        },
        error:function(){
            $.Hide("#shade,#loading");
            alert('请求异常.');
        }
    });
}


/* 未关联数据列表搜索框
 * keyup 时触发
 */
function SearchOthersAsset(){
    var allData = $('#othersAsset').data('AssetList');
    var value = $('#SearchOthersAsset').val();
    $('#SelectOthersAsset').empty();
    if(value.trim().length<1){
        $.each(allData,function(k,v){
            var content = v.text;
            var result = content.indexOf(value);
            //展示内容
            $('#SelectOthersAsset').append("<option value='"+v.id+"'>"+content+"</option>");
        });
    }else{
        $.each(allData,function(k,v){
            var content = v.text;
            var result = content.indexOf(value);
            if(result!=-1){
                //展示内容
                $('#SelectOthersAsset').append("<option value='"+v.id+"'>"+content+"</option>");
            }
        });
    }
}

/* 已关联数据列表搜索框
 * keyup时触发
 */
function SearchCurrentAsset(){
    var allData = $('#currentAsset').data('AssetList');
    var value = $('#SearchCurrentAsset').val();
    $('#SelectCurrentAsset').empty();
    if(value.trim().length<1){
        $.each(allData,function(k,v){
            var content = v.text;
            var result = content.indexOf(value);
            //展示内容
            $('#SelectCurrentAsset').append("<option value='"+v.id+"'>"+content+"</option>");
        });
    }else{
        $.each(allData,function(k,v){
            var content = v.text;
            var result = content.indexOf(value);
            if(result!=-1){
                //展示内容
                $('#SelectCurrentAsset').append("<option value='"+v.id+"'>"+content+"</option>");
            }
        });
    }
}


function RemoveStatus(){
    $("#handlestatus").empty();
}
