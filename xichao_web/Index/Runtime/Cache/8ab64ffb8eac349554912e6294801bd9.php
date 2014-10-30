<?php if (!defined('THINK_PATH')) exit();?><!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>login</title>

</head>



<body>
	<form action="__URL__/login" method="POST">
		<label>用户名</label>
		<input type="text"  name="username"/></br>
		<label>密码</label>
		<input type="password" name="password"/></br>
		<input type="submit" value="登录" />
	</form>
</body>
</html>