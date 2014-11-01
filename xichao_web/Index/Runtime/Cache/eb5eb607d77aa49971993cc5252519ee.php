<?php if (!defined('THINK_PATH')) exit();?><!DOCTYPE html>
<html>
<!-- ###类说明### recruit 是单张模块 ## recruit_total 是两张并排模块 ##recruit_bg 是背景## -->
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="" />
<meta name="keywords" content="" />
<meta name="author" content="Nee Bee Studio" />
<link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/footer.css" />
<link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/header.css" />
<link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/recruit.css" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<script src="__PUBLIC__/Js/jquery.min.js"></script>

</head>
	<body>
		<div class="container" >
			<div class="main_page">
<!--###################################header###################################-->
	            <!--###################################header###################################-->
<div class="head">
    <?php if($_SESSION['nick'] == null): ?><a class="login" href="__APP__/Login/index">登录</a><a class="register" href="__APP__/Register/index">注册</a>
        <?php else: ?><a class="login" href="#"><?php echo ($_SESSION['nick']); ?></a><a class="register" href="__APP__/Logout/logout">注销</a><?php endif; ?>
    <!--
    <a class="login" href="__APP__/Login/index">登陆</a>
    <a class="register" href="__APP__/Register/index">注册</a>
    -->

    <a class="logo" href="__APP__/Index/index"><img height="75px" src="__PUBLIC__/Images/rt_logo.png"></a>
</div>   
<div class="nav_row">
    <hr class="up">
    <a id="header_item0" href="__APP__/Index/indexStatic">首页</a>
    <a id="header_item1" href="__APP__/BookStore/index">曦潮书店</a>
    <a id="header_item2" href="#">会员</a>
    <a id="header_item3" href="#">人文</a>
    <a id="header_item4" href="#">活动</a>
    <a id="header_item5" href="__APP__/Recruit/index">招募</a>
    <hr class="down">
</div>          
				<div class="vs"></div>
<!--####################################main####################################-->
<!--####################################first###################################-->
				<div class="recruit_total">
					<div id="recruit_01" class="recruit">
						<div class="recruit_bg">
							<a href="#">
								<img src="__PUBLIC__/Images/recruit_recruit.png" />
								<img  class="gray" src="__PUBLIC__/Images/recruit_gray.png"/>
								<img  class="words_style_1" id="words_01" src="__PUBLIC__/Images/recruit_word_recruit_b.png"/>
								<img  class="words_style_2" id="words_02" src="__PUBLIC__/Images/recruit_word_recruit_d.png"/>
							</a>
						</div>
					</div>
				</div>
				<div class="vs"></div>
<!-- ####################################second#################################-->
				<div  class="recruit_total" style="height:480px;width:790px;">
					<div class="recruit" id="recruit_02">
						<div class="recruit_bg">
							<a href="__APP__/Mitochondrion/index">
								<img  src="__PUBLIC__/Images/recruit_mitochondrion.png" />
								<img  class="gray" src="__PUBLIC__/Images/recruit_gray.png"/>
								<img class="words_style_1" id="words_03" src="__PUBLIC__/Images/recruit_word_mitochondrion_b.png"/>
								<img class="words_style_2" id="words_04" src="__PUBLIC__/Images/recruit_word_mitochondrion_d.png"/>
							</a>
						</div>
					</div>
					<div class="recruit" id="recruit_03">
						<div class="recruit_bg">
							<a href="__APP__/Special/index">
								<img src="__PUBLIC__/Images/recruit_special.png" />
								<img  class="gray" src="__PUBLIC__/Images/recruit_gray.png" />
								<img class="words_style_1" id="words_05" src="__PUBLIC__/Images/recruit_word_special_b.png" />
								<img class="words_style_2" id="words_06" src="__PUBLIC__/Images/recruit_word_special_d.png" style="margin-top:-88px"/>
							</a>
						</div>
					</div>

				</div>
				<div class="vs"></div>
<!--###################################third###################################-->
				<div  class="recruit_total" style="height:412px;width:790px;">
					<div class="recruit" id="recruit_04" >
						<div class="recruit_bg">
							<a href="__APP__/Inklings/index">
								<img src="__PUBLIC__/Images/recruit_inklings.png" />
								<img class="gray" src="__PUBLIC__/Images/recruit_gray.png" />
								<img class="words_style_1" id="words_07" src="__PUBLIC__/Images/recruit_word_inklings_b.png" />
								<img class="words_style_2" id="words_08" src="__PUBLIC__/Images/recruit_word_inklings_d.png" style="margin-top:55px"/>
							</a>
						</div>
					</div>
					<div class="recruit" id="recruit_05" >
						<div class="recruit_bg">
							<a href="__APP__/Strategy/index">
								<img src="__PUBLIC__/Images/recruit_strategy.png" />
								<img class="gray" src="__PUBLIC__/Images/recruit_gray.png"/>
								<img class="words_style_1" id="words_09" src="__PUBLIC__/Images/recruit_word_strategy_b.png" />
								<img class="words_style_2" id="words_10" src="__PUBLIC__/Images/recruit_word_strategy_d.png" />
							</a>
						</div>
					</div>
				</div>
				
				<div class="vs"></div>
<!--###################################fourth###################################-->
				<div  class="recruit_total" style="height:175px;width:790px;">
					<div class="recruit" id="recruit_06" >
						<div class="recruit_bg">
							<a href="__APP__/Talents/index">
								<img src="__PUBLIC__/Images/recruit_endoplasmic.png" />
								<img class="gray" src="__PUBLIC__/Images/recruit_gray.png"/>
								<img class="words_style_1" id="words_11" src="__PUBLIC__/Images/recruit_word_endoplasmic_b.png" />
								<img class="words_style_2" id="words_12" src="__PUBLIC__/Images/recruit_word_endoplasmic_d.png" />
							</a>
						</div>
					</div>
					<div class="recruit" id="recruit_07" >
						<div class="recruit_bg">
							<a href="__APP__/Leaf/index">
								<img src="__PUBLIC__/Images/recruit_leaf.png" />
								<img class="gray" src="__PUBLIC__/Images/recruit_gray.png"/>
								<img class="words_style_1" id="words_13" src="__PUBLIC__/Images/recruit_word_leaf_b.png" />
								<img class="words_style_2" id="words_14" src="__PUBLIC__/Images/recruit_word_leaf_d.png" />
							</a>
						</div>
					</div>
				</div>

<script>
	$(document).ready(function(){
		$(".recruit_bg").mouseover(function(){
			$("img.gray",$(this)).show();
			$("img.words_style_1",$(this)).hide();
			$("img.words_style_2",$(this)).show();

		})
		$(".recruit_bg").mouseout(function(){
			$("img.gray",$(this)).hide();
			$("img.words_style_1",$(this)).show();
			$("img.words_style_2",$(this)).hide();
		})
	})
</script>
<!--###################################footer###################################--> 
	            <!--###################################footer###################################-->
<hr>
<div class="footer-body">
    <a id="footer_item1" href="#">关于我们</a>
    <a id="footer_item2" href="#" >联系我们</a>
    <a id="footer_item3" href="#" >加入我们</a>
    <a id="footer_item4" href="#" >服务声明</a>
</div>   
<div id="copyright">
    <div><b>Copyright©曦潮2014，All Right Reserved|沪ICP备xxxxxx号</b>
    </div>  
</div>   

			</div>
		</div>
	</body>
</html>