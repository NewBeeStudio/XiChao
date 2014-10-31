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

    <script src="__PUBLIC__/Js/jquery.min.js"></script>
    <script src="__PUBLIC__/Js/register.js"></script>


    <title>曦潮书店 | 注册</title>
</head>

<body>
	<!--
	<a href="__APP__/Index/index">首页</a></br>
	<p>注册</p>
	<a href="__APP__/Login/index">登陆</a>
	<form action="__URL__/register" method="POST">
		<label>用户名</label>
		<input type="text"  name="username"/></br>
		<label>密码</label>
		<input type="password" name="password"/></br>
		<label>重复密码</label>
		<input type="password" name="repassword"/></br>
		<label>验证码</label>
        <input type="text" name="verify"/>
        <img src="__APP__/Common/verify"/ onclick="show(this)">
		<input type="submit" value="注册" />
	</form>
-->

	<div class="container">
		<div class="main_page_new">
			<div id="register_header">
				<img src="__PUBLIC__/Images/myXichao.png" style="position:absolute">
				<p id="register_title">账户注册</P>
			</div>
			<div id="register_hint">
				<font id="register_hint_1">1、设置登录名</font>
				<font id="register_hint_2">2、填写账户信息</font>
				<font id="register_hint_3">注册成功</font>
				<hr id="register_progress_bar_gray">
				<hr id="register_progress_bar_blue">
			</div>
			<div id="register_content">
				<form action="#" method="post">
					<div id="register_content_1">
						<table class="register_content_position">
							<tr>
								<td>电子邮箱：</td>
								<td colspan="2"><input type="text" id="register_email" name="register_email"></td>
								<td></td>
							</tr>
							<tr>
								<td>验证码：</td>
								<td><input type="text" id="register_verify" name="register_verify"></td>
								<td><img src="__APP__/Common/verify" onclick="show(this)"></td>
								<td><font>看不清楚？换图一张</font></td>
							</tr>   
							<tr>
								<td colspan="4"><input type="button" value="下一步"></td>
							</tr>
						</table>
						
					</div>
					<div id="register_content_2">
					</div>
					<div id="register_content_3">
					</div>
				</form>
			</div>
		</div>
	</div>

<script>
	function show(obj){
		obj.src="__APP__/Common/verify/random/"+Math.random();
	}
</script>
</body>

</html>