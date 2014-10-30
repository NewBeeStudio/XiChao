
$(document).ready(function(){
	$(".pt-perspective").mouseenter(function(){
		$("#page1_up").animate({height:"0"},1000);
		$("#page1_down").animate({height:"0"},1000,function(){
			$("#logo_blue").fadeOut(500);
			$("#logo_tran").fadeIn(500);			
			$("#page1_up").animate({height:"70"},500);
			$("#page1_down").animate({height:"70"},500,function(){
				$("#page1_up").animate({height:"0"},1000,function(){
					$("#page1_up").hide();
				});
				$("#page1_down").animate({height:"0"},1000,function(){
					$("#page1_down").hide();
				});

				$("#logo_blue").fadeIn(1000);
				$("#logo_tran").fadeOut(1000,function(){
					$("#logo_tran").hide();
				});
				$("#bgimg1").fadeOut(1000);
				$("#bgimg2").fadeIn(1000,function(){
					$(".pt-page2").show();
					var x=$(".main_page_content_1").offset().left;
					var y=$(".main_page_content_1").offset().top;
					$("#bgimg2").animate({height:"510",width:"420",left:x,top:y},700,function(){
						$("#bgimg2").hide();
						$("#bgimg2_1").show();
					});
					$("#logo_blue").animate({left:x+76,top:y+130},700,function(){
						$("#logo_blue").hide();
						$("#logo_blue_1").show();
						$(".pt-page1").hide();
					});
				});
			});
		});
	})
})
