<?php if (!defined('THINK_PATH')) exit();?><!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>勤工助学报名</title>
<script>
	function show(obj){
		obj.src="__APP__/Common/verify/random/"+Math.random();
	}
</script>
</head>

<body>
	<a href="__APP__/Index/index">首页</a></br>
	<!--未登陆状态，显示登陆连接，点击该链接会跳转到登陆界面，已登录状态，显示用户名-->
	<?php if($_SESSION['username'] == null): ?><a href="__APP__/Login/index">登陆</a></br><a href="__APP__/Register/index">注册</a></br>
		<?php else: ?><a href="__APP__/Logout/logout">注销</a></br><a href="__APP__/Person/index"><?php echo ($_SESSION['username']); ?></a></br><?php endif; ?>
	<p>勤工助学报名</p>
	<form action="__URL__/jobHandle" method="POST">
		<label>姓名</label>
		<input type="text"  name="name"/></br>
		<label>年龄</label>
		<input type="text" name="age"/></br>
		<label>验证码</label>
        <input type="text" name="verify"/>
        <img src="__APP__/Common/verify"/ onclick="show(this)"></br>
		<input type="submit" value="提交" />
	</form>
</body>

</html>