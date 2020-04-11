window.onload = function(){
    var oBtn = document.getElementById('btn');
    var iNum01 = 12;

    oBtn.onclick = function(){
        var iNum02 = 24;
        var iRs = fnAdd(iNum01,iNum02);
        alert(iRs);
    }
    function fnAdd(iVal01,iVal02){
        var iRs02 = iVal01 + iVal02;
        return iRs02;
    }
}