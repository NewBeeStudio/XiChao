var appl_start = false;

$(document).ready(function(){
  $('#appl-freedate1').datepicker();
  $('#appl-freedate2').datepicker();
  $("#appl-start").click(function(){
    if (!appl_start){
        appl_start = true;
        $('html, body').animate({scrollTop: $(document).height()-200},1000);
        $("#appl-sheet").slideDown(1000);
        $("#appl-start").show().html("收起表格");
    }else{
        appl_start = false;
        $('html, body').animate({scrollTop: 0},1000);
        $("#appl-sheet").slideUp(1000);
        $("#appl-start").show().html("我要报名");
    }
  });
  //$("#appl-intro0").keypress(form_check);
});


function form_check(){
    var count=0;
    if (document.getElementById('checkbox-1-1').checked) {count = count + 1;}
    if (document.getElementById('checkbox-1-2').checked) {count = count + 1;}
    if (document.getElementById('checkbox-1-3').checked) {count = count + 1;}
    if (document.getElementById('checkbox-1-4').checked) {count = count + 1;}
    if (document.getElementById('checkbox-1-5').checked) {count = count + 1;}

    if (document.getElementById('checkbox-2-1').checked) {count = count + 1;}
    if (document.getElementById('checkbox-2-2').checked) {count = count + 1;}
    if (document.getElementById('checkbox-2-3').checked) {count = count + 1;}
    if (document.getElementById('checkbox-2-4').checked) {count = count + 1;}

    if (document.getElementById('checkbox-3-1').checked) {count = count + 1;}
    if (document.getElementById('checkbox-3-2').checked) {count = count + 1;}
    if (document.getElementById('checkbox-3-3').checked) {count = count + 1;}

    if (document.getElementById('checkbox-4-1').checked) {count = count + 1;}
    if (document.getElementById('checkbox-4-2').checked) {count = count + 1;}
    
    if (count > 3){
        alert("请最多选三个岗位");
        return false;
    }
    return true;
}