<?php
class UserModel extends Model{
	//自动验证
	protected $_validate = array(
		array('register_verify','require','验证码必须！'),
		array('register_verify','checkVerify','验证码不正确！',0,'function'),

		array('email','require','电子邮箱必须！'),
		array('email','email','电子邮箱格式不正确！'),
		array('email','require','该邮箱已注册，请重新输入!',0,'unique'),

		//array('username','require','用户名必须！'),
		//array('username','require','用户名已存在，请重新输入!',0,'unique'),
		array('password','require','密码必须！'),
		array('repassword','require','确认密码必须！'),
		array('repassword','password','确认密码不正确！',0,'confirm'),
		array('nick','require','会员名必须！'),
		array('nick','require','会员名已存在，请重新输入!',0,'unique'),
		);
	/*
	function checkVerify($data){
		if(session('verify') != md5($data)){
			return false;
		}
		return true;
	}
	*/
	//自动完成
	protected $_auto=array(
		array('password','md5',3,'function'),
		array('create_time','time',1,'function'),
		array('update_time','time',1,'function'),
		);
}