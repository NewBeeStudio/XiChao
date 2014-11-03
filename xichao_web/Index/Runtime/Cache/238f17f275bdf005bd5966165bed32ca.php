<?php if (!defined('THINK_PATH')) exit();?><!DOCTYPE html>
<html lang="zh-cn">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>曦潮书店 | 登录</title>
    <meta name="description" content="" />
    <meta name="keywords" content="" />
    <meta name="author" content="Nee Bee Studio" />

    <link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/login.css" />
    <link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/footer.css" />
    <link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/header.css" />


    <script src="__PUBLIC__/Js/jquery.min.js"></script>
    
</head>



<body>
	<!--
	<a href="__APP__/Index/index">首页</a></br>
	<form action="__URL__/login" method="POST">
		<label>用户名</label>
		<input type="text"  name="username" value="<?php echo ($_COOKIE['username']); ?>"/></br>
		<label>密码</label>
		<input type="password" name="password"/></br>
		<input type="submit" value="登录" />
	</form>
	-->
	<div class="container">
		<div class="main_page">
<!--###################################header###################################-->
            <!--###################################header###################################-->
<div class="head">
    <?php if($_SESSION['nick'] == null): ?><a class="login" href="__APP__/Login/index">登录</a><a class="register" href="__APP__/Register/index">注册</a>
        <?php else: ?><a class="login" href="#"><?php echo ($_SESSION['nick']); ?></a><a class="register" href="__APP__/Logout/logout">退出</a><?php endif; ?>
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
            <div id="login_image">
            	<img src="__PUBLIC__/Images/login.jpg" id="login_image_1">
            </div>
            <div id="login_main">
            	<div id="login_my_xichao">
            		<img src="__PUBLIC__/Images/myXichao.png" style="position:absolute">
            	</div>
            	<div id="login_content">
            		<form action="__URL__/login" method="post">
            			<table>
            				<tr>
            					<td style="text-align:right;">用户名</td>
            					<td style="padding:10px" colspan="2"><input type="text" name="email" id="login_username"></td>
            				</tr>
            				<tr>
            					<td style="text-align:right;">密码</td>
            					<td style="padding:10px" colspan="2"><input type="password" name="password" id="login_password"></td>
            				</tr>
            				<tr>
            					<td> </td>
            					<td style="padding:10px;" id="login_button"><input type="submit" name="login_submit" id="login_submit" value="登录"></td>
            					<td style="font-size:10pt;line-height:20px;">
            						<a href="#">忘记登录密码？</a><br>
            						<a href="__APP__/Register/index">免费注册</a>
            					</td>
            				</tr>
            			</table>
            		</form>
            	</div>
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
</html>