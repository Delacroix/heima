$(function() {
    var error_name = true;
    var $name = $('#user_name');
    
    $name.blur(function() {
        fn_check_username();
    }).click(function () {
        $(this).next().hide();
    })
})

function fn_check_username() {
    var sVal = $name.val();

    //判断是否为空
    if(sVal==''){
        error_name = true;
        $name.next().html('用户名不能为空').show();
        return;
    }

    if(reUser.test(sVal)){
        error_name = false;
        $name.next().hide();
    }
    else{
        error_name = true;
        $name.next().html('用户名是6到20位的数字、字母、下划线')
    }
}