
$(function(){
    InitToggleMenu();
});

/*
初始化左侧菜单，根据cookie中的has_shrink去判断菜单默认是收缩还是展开
 */
function InitToggleMenu(){
    var $this = $('#shrink_menu');
    var shrink_status = $.cookie("has_shrink");

    if(shrink_status == 1){
        ExecuteToggleMenu($this,true);
    }else{
        ExecuteToggleMenu($this,false);
    }
}

/*
收缩或展开左侧菜单（点击触发）
 */
function ToggleMenu(ths){
    var $this = $('#shrink_menu');
    var $menu = $this.parent().parent();
    var isShrink = false;
    if($menu.hasClass('shrink')){
        //去展开
        $.cookie("has_shrink", 0,{ path: '/' });
    }else{
        var isShrink = true;
        $.cookie("has_shrink", 1,{ path: '/' });

    }
    ExecuteToggleMenu($this,isShrink);
}

/*
执行展开或者收缩左侧菜单
 */
function ExecuteToggleMenu($this,goShrink){
    var $menu = $this.parent().parent();
    var $content = $menu.next();
    if (goShrink){
        //收缩
        $this.addClass('fa-angle-double-right').removeClass('fa-angle-double-left')
        $menu.addClass('shrink')
        $content.addClass('pst-left-35');
    }else{
        //展开
        $this.removeClass('fa-angle-double-right').addClass('fa-angle-double-left');
        $menu.removeClass('shrink');
        $content.removeClass('pst-left-35');
    }
}
