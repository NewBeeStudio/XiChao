var page1_touch = false,
page2_touch = false,
left = false,
right = false,
no_listen = true,
$main = $( '#pt-main' ),
$pages = $main.children( 'div.pt-page' ),
pagesCount = $pages.length,
current = 0,
isAnimating = false,
endCurrPage = false,
endNextPage = false,
animEndEventNames = {
	'WebkitAnimation' : 'webkitAnimationEnd',
	'OAnimation' : 'oAnimationEnd',
	'msAnimation' : 'MSAnimationEnd',
	'animation' : 'animationend'
},
// animation end event name
animEndEventName = animEndEventNames[ Modernizr.prefixed( 'animation' ) ],
// support css animations
support = Modernizr.cssanimations,
screen_width = document.body.clientWidth,
screen_height = document.body.clientHeight,
mouseX = screen_width / 2,
mouseY = 0;

window.addEventListener('mousemove', changePage, false);

$(document).ready(function(){
	$pages.each( function() {
		var $page = $( this );
		$page.data( 'originalClassList', $page.attr( 'class' ) );
	} );
	$pages.eq( current ).addClass( 'pt-page-current' );

	$("#logo_blue").mouseenter(function(){
		if(!page1_touch){
			page1_touch = true;
			$("#page1_up").animate({height:"0"},700,function(){
				setTimeout(function(){
					$("#up_edge").animate({height:"3%"},300,function(){
						setTimeout(function(){
							$("#up_edge").animate({height:"0"},600);
						},100);
					});
				},0);
			});
			$("#page1_down").animate({height:"0"},700,function(){
				setTimeout(function(){
					$("#down_edge").animate({height:"3%"},300,function(){
						setTimeout(function(){
							$("#down_edge").animate({height:"0"},600);
						},100);
					});
				},0);
			});
			$("#logo_blue").fadeOut(700,function(){
				setTimeout(function(){
					$("#logo_tran").fadeIn(1500);
				},0);
			});
			setTimeout(function(){
				$("#previous1").show();
				$("#next1").show();
				$("#previous1").fadeTo(800,0.4);
				$("#next1").fadeTo(800,0.4,function(){
					no_listen = false;
				});
			},1500);
		}
	});

	$("#string31").mouseenter(function(){
		$("#line31").slideDown(250,function(){
			$("#photo31").fadeIn(250);
		});
	});
	$("#string31").mouseleave(function(){
		setTimeout(function(){
			$("#line31").slideUp(250,function(){
				$("#photo31").fadeOut(250);
			});
		},100);
	});
	$("#string32").mouseenter(function(){
		$("#line32").slideDown(250,function(){
			$("#photo32").fadeIn(250);
		});
	});
	$("#string32").mouseleave(function(){
		setTimeout(function(){
			$("#line32").slideUp(250,function(){
				$("#photo32").fadeOut(250);
			});
		},100);
	});
	$("#string33").mouseenter(function(){
		$("#line33").slideDown(250,function(){
			$("#photo33").fadeIn(250);
		});
	});
	$("#string33").mouseleave(function(){
		setTimeout(function(){
			$("#line33").slideUp(250,function(){
				$("#photo33").fadeOut(250);
			});
		},100);
	});
	$("#string34").mouseenter(function(){
		$("#line34").slideDown(250,function(){
			$("#photo34").fadeIn(250);
		});
	});
	$("#string34").mouseleave(function(){
		setTimeout(function(){
			$("#line34").slideUp(250,function(){
				$("#photo34").fadeOut(250);
			});
		},100);
	});
	$("#string35").mouseenter(function(){
		$("#line35").slideDown(250,function(){
			$("#photo35").fadeIn(250);
		});
	});
	$("#string35").mouseleave(function(){
		setTimeout(function(){
			$("#line35").slideUp(250,function(){
				$("#photo35").fadeOut(250);
			});
		},100);
	});
	$("#string41").mouseenter(function(){
		$("#line41").slideDown(250,function(){
			$("#photo41").fadeIn(250);
		});
	});
	$("#string41").mouseleave(function(){
		setTimeout(function(){
			$("#line41").slideUp(250,function(){
				$("#photo41").fadeOut(250);
			});
		},100);
	});
	$("#string42").mouseenter(function(){
		$("#line42").slideDown(250,function(){
			$("#photo42").fadeIn(250);
		});
	});
	$("#string42").mouseleave(function(){
		setTimeout(function(){
			$("#line42").slideUp(250,function(){
				$("#photo42").fadeOut(250);
			});
		},100);
	});
	$("#string51").mouseenter(function(){
		$("#line51").slideDown(250,function(){
			$("#photo51").fadeIn(250);
		});
	});
	$("#string51").mouseleave(function(){
		setTimeout(function(){
			$("#line51").slideUp(250,function(){
				$("#photo51").fadeOut(250);
			});
		},100);
	});
	$("#string52").mouseenter(function(){
		$("#line52").slideDown(250,function(){
			$("#photo52").fadeIn(250);
		});
	});
	$("#string52").mouseleave(function(){
		setTimeout(function(){
			$("#line52").slideUp(250,function(){
				$("#photo52").fadeOut(250);
			});
		},100);
	});
	$("#string53").mouseenter(function(){
		$("#line53").slideDown(250,function(){
			$("#photo53").fadeIn(250,function(){
				$("#download").fadeIn(250);
			});
		});
	});
	$("#string53").mouseleave(function(){
		setTimeout(function(){
			$("#line53").slideUp(250,function(){
				$("#photo53").fadeOut(250);
			});
		},100);
	});
	$("#string54").mouseenter(function(){
		$("#line54").slideDown(250,function(){
			$("#photo54").fadeIn(250);
		});
	});
	$("#string54").mouseleave(function(){
		setTimeout(function(){
			$("#line54").slideUp(250,function(){
				$("#photo54").fadeOut(250);
			});
		},100);
	});
	$("#string55").mouseenter(function(){
		$("#line55").slideDown(250,function(){
			$("#photo55").fadeIn(250);
		});
	});
	$("#string55").mouseleave(function(){
		setTimeout(function(){
			$("#line55").slideUp(250,function(){
				$("#photo55").fadeOut(250);
			});
		},100);
	});
	$("#download").click(function(){
		$(this).fadeOut(250);
	});
	

	$(".strings31").mouseenter(function(){
		$(this).animate({fontSize:'14px'},300);
	});
	$(".strings31").mouseleave(function(){
		$(this).animate({fontSize:'11px'},300);
	});
	$(".strings41").mouseenter(function(){
		$(this).animate({fontSize:'20px'},300);
	});
	$(".strings41").mouseleave(function(){
		$(this).animate({fontSize:'15px'},300);
	});
	$(".strings51").mouseenter(function(){
		$(this).animate({fontSize:'18px'},300);
	});
	$(".strings51").mouseleave(function(){
		$(this).animate({fontSize:'15px'},300);
	});


	$(".pt-page").click(function(){
		if(left&&page2_touch){
			if( isAnimating ) {
				return false;
			}
			nextPage(false);
		}
		else if(right){
			if( isAnimating ) {
				return false;
			}
			nextPage(true);
		}
	});
});
function nextPage( direction ) {

	if( isAnimating ) {
		return false;
	}

	isAnimating = true;

	var $currPage = $pages.eq( current );

	if(direction){
		if( current < pagesCount - 1 ) {
			++current;
		}
		else {
			current = 0;
		}

		var $nextPage = $pages.eq( current ).addClass( 'pt-page-current' ),
		outClass = 'pt-page-moveToLeftFade', inClass = 'pt-page-moveFromRightFade';

		$currPage.addClass( outClass ).on( animEndEventName, function() {
			$currPage.off( animEndEventName );
			endCurrPage = true;
			if( endNextPage ) {
				onEndAnimation( $currPage, $nextPage );
			}
		} );

		$nextPage.addClass( inClass ).on( animEndEventName, function() {
			$nextPage.off( animEndEventName );
			endNextPage = true;
			if( endCurrPage ) {
				onEndAnimation( $currPage, $nextPage );
			}
		} );

		if( !support ) {
			onEndAnimation( $currPage, $nextPage );
		}
	}
	else{
		if( current > 0 ) {
			--current;
		}
		else {
			current = pagesCount - 1;
		}

		var $nextPage = $pages.eq( current ).addClass( 'pt-page-current' ),
		outClass = 'pt-page-moveToRightFade', inClass = 'pt-page-moveFromLeftFade';

		$currPage.addClass( outClass ).on( animEndEventName, function() {
			$currPage.off( animEndEventName );
			endCurrPage = true;
			if( endNextPage ) {
				onEndAnimation( $currPage, $nextPage );
			}
		} );

		$nextPage.addClass( inClass ).on( animEndEventName, function() {
			$nextPage.off( animEndEventName );
			endNextPage = true;
			if( endCurrPage ) {
				onEndAnimation( $currPage, $nextPage );
			}
		} );

		if( !support ) {
			onEndAnimation( $currPage, $nextPage );
		}
	}

	if(current == 1&&!page2_touch){
		page2_touch = true;
		setTimeout(function(){
			$(".string2").fadeIn(1000);
		},800);
	}
}

function onEndAnimation( $outpage, $inpage ) {
	endCurrPage = false;
	endNextPage = false;
	resetPage( $outpage, $inpage );
	isAnimating = false;
}

function resetPage( $outpage, $inpage ) {
	$outpage.attr( 'class', $outpage.data( 'originalClassList' ) );
	$inpage.attr( 'class', $inpage.data( 'originalClassList' ) + ' pt-page-current' );
}

function changePage (argument) {
	if(!no_listen){
		mouseX = event.clientX;
		mouseY = event.clientY;
		//if(screen_height * 0.4 < mouseY && mouseY < screen_height * 0.7 && mouseX < screen_width * 0.2){
		if(mouseX < screen_width * 0.48){
			left = true;
			$(".previous").css("opacity","0.8");
		}
		//else if (screen_height * 0.4 < mouseY && mouseY < screen_height * 0.7 && mouseX > screen_width * 0.8) {
		else if (mouseX > screen_width * 0.52) {
			right = true;
			$(".next").css("opacity","0.8");
		}
		else{
			left = false;
			right = false;
			$(".previous").css("opacity","0.4");
			$(".next").css("opacity","0.4");	 
		}
	}
}