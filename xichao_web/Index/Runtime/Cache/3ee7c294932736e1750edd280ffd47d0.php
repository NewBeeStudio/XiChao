<?php if (!defined('THINK_PATH')) exit();?><!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>注册</title>
<script>
	function show(obj){
		obj.src="__APP__/Common/verify/random/"+Math.random();
	}
</script>
</head>

<body>
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
</body>

</html>