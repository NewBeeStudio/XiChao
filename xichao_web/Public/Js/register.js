$(document).ready(function(){
	var hint_1_width=$("#register_hint_1").css("width");
	
	var blue_width_1=hint_1_width;
	$("#register_progress_bar_blue").animate({width:blue_width_1},500,function(){
		$("#register_hint_1").click(function(){
			$("#register_progress_bar_blue").animate({width:blue_width_1},500);
		})
		$("#register_hint_2").click(function(){
			$("#register_progress_bar_blue").animate({width:400},500);
		})
		$("#register_hint_3").click(function(){
			$("#register_progress_bar_blue").animate({width:620},500);
		})		
	});
	
})