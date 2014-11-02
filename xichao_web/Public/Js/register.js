$(document).ready(function(){
	var hint_1_width=$("#register_hint_1").css("width");
	var hint_1_margin_left=$("#register_hint_1").css("margin-left");
	var hint_2_width=$("#register_hint_2").css("width");
	var hint_2_margin_left=$("#register_hint_2").css("margin-left");

	var blue_width=hint_1_width;
	$("#register_progress_bar_blue").animate({width:blue_width},500,function(){
		$("#register_hint_1").click(function(){
			var blue_width=hint_1_width;
			var blue_margin_left=hint_1_margin_left;

			$("#register_progress_bar_blue").animate({width:blue_width,marginLeft:blue_margin_left},500);
			$("#register_hint_1").css("color","black");
			$("#register_hint_2").css("color","gray");
			//$("#register_hint_3").css("color","gray");
			$("#register_content_1").show();
			$("#register_content_1").animate({marginLeft:"137px"},500);
			$("#register_content_2").animate({marginLeft:"1034px"},500);
			//$("#register_content_3").animate({marginLeft:"1867px"},500);


		})
		$("#register_hint_2,#register_next_button_1").click(function(){
			//$("#register_progress_bar_blue").animate({width:400},500);

			var blue_width=hint_2_width;
			var blue_margin_left=hint_2_margin_left;

			$("#register_progress_bar_blue").animate({width:blue_width,marginLeft:blue_margin_left},500);
			$("#register_hint_1").css("color","gray");
			$("#register_hint_2").css("color","black");
			//$("#register_hint_3").css("color","gray");
			$("#register_content_1").animate({marginLeft:"-650px"},500);
			$("#register_content_2").animate({marginLeft:"247px"},500);
			//$("#register_content_3").animate({marginLeft:"1080px"},500);

		})
		/*
		$("#register_hint_3,#register_next_button_2").click(function(){
			$("#register_progress_bar_blue").animate({width:620},500);
			$("#register_hint_1").css("color","gray");
			$("#register_hint_2").css("color","gray");
			//$("#register_hint_3").css("color","black");
			$("#register_content_1").animate({marginLeft:"-1217px"},500);
			$("#register_content_2").animate({marginLeft:"-540px"},500);
			//$("#register_content_3").animate({marginLeft:"293px"},500);			
		})	
*/
	});
	
})