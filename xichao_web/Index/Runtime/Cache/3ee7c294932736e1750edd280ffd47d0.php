<?php if (!defined('THINK_PATH')) exit();?><!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="" />
    <meta name="keywords" content="" />
    <meta name="author" content="Nee Bee Studio" />
    
    <link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/register.css" />
    <link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/header.css" />
    <link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/footer.css" />

    <script src="__PUBLIC__/Js/jquery.min.js"></script>
    <script src="__PUBLIC__/Js/register.js"></script>


    <title>曦潮书店 | 注册</title>
</head>

<body>

	<div class="container">
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

			<div id="register_header">
				<img src="__PUBLIC__/Images/myXichao.png" style="position:absolute">
				<p id="register_title">账户注册</P>
			</div>
			<div id="register_hint">
				<font id="register_hint_1">1、设置登录名</font>
				<font id="register_hint_2">2、填写账户信息</font>
				<!--<font id="register_hint_3">注册成功</font>-->
				<hr id="register_progress_bar_gray">
				<hr id="register_progress_bar_blue">
			</div>
			<div id="register_content">
				<form action="__URL__/register" method="post">
					
					<div id="register_content_1">
						<table class="register_content_position">
							<tr>
								<td style="text-align:right;">电子邮箱：</td>
								<td colspan="2"><input type="text" id="register_email" name="email"></td>
								<td></td>
							</tr>
							<tr>
								<td style="text-align:right;">验证码：</td>
								<td><input type="text" id="register_verify" name="register_verify"></td>
								<td><img src="__APP__/Common/verify" onclick="show(this)"></td>
								<td><font>看不清楚？点图更换</font></td>
							</tr>
						</table>
						<div style="height:50px"></div>
						<div id="register_next">
							<input type="button" value="下一步" id="register_next_button_1" class="register_next_button">
						</div>
					</div>
					
					<div id="register_content_2">
						<table class="register_content_position">
							<tr>
								<td style="text-align:right;">设置登录密码：</td>
								<td><input type="password" id="register_password" name="password"></td>
							</tr>

							<tr>
								<td style="text-align:right;">重复密码：</td>
								<td><input type="password" id="register_repassword" name="repassword"></td>
							</tr>
							<tr>
								<td style="text-align:right;">设置会员名：</td>
								<td><input type="text" id="register_username" name="nick"></td>
							</tr>
						</table>
						<div style="height:50px"></div>
						<div id="register_next">
							<input type="submit" value="提交" id="register_next_button_2" class="register_next_button">
						</div>
					</div>
					<!--
					<div id="register_content_3">
						<div id="register_success_1">
							<p class="register_success_words">
								注册成功!	
							</p>
						</div>
						<div style="height:10px;"></div>
						<div id="register_success_2">
							<p class="register_success_words">
								开始美妙的人文之旅吧~
							</p>
						</div>
					</div>
					-->
				</form>
			</div>
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
<script>
	function show(obj){
		obj.src="__APP__/Common/verify/random/"+Math.random();
	}
</script>
</body>

</html>