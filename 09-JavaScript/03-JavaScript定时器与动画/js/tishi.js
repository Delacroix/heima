/*
function fnWrap() {
    function fnTouzi() {
        alert('亲，请关注网站新的产品！');
    }
    fnTouzi();
}

fnWrap();
*/

//上面的定义方法，函数名称还可能同名，可以改写成下面封闭函数的形式：
// 在函数前面加 ;  确保之前的语句被执行完
/*
;(function() {
    function fnTouzi() {
        alert('亲，请关注网站新的产品！');
    }
    fnTouzi();
})();
*/

//封闭函数装高手的写法  !代表函数整体
/*
;!function () {
    function fnTouzi() {
        alert('亲，请关注网站新的产品！');
    }
    fnTouzi();
}();
*/

//封闭函数装高手的写法2  ~代表函数整体
;~function () {
    function fnTouzi() {
        alert('亲，请关注网站新的产品！');
    }
    fnTouzi();
}();

