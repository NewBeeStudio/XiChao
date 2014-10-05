$("#logo_blue").mouseenter(function(){
	$("#page_up").animate({height:"37%"},1000);
	$("#page_down").animate({height:"37%"},1000);
	$("#logo_blue").fadeOut(1000,function(){
		setTimeout(function(){
			$("#logo_tran").fadeIn(900);
		},0)
	});

});