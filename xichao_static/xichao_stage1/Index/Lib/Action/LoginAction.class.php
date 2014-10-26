<?php

//曦潮会员登录

class LoginAction extends Action{
	//登录界面显示
	Public function index(){
		$this->display();
	}
	//会员登录验证
	Public function login(){
		//可以设置为距离上次登录时间较长的话输入验证码，或者登陆ip发生了改变来输入验证码

		//登陆时进行自动验证
		$rules=array(
			array('username','require','用户名必须！'),
			array('password','require','密码必须！'),
		);
		$User=M('User');
		if(!$User->validate($rules)->create()){
			$this->error($User->getError());
		}else{
			$username=$_POST['username'];
			//cookie('username',$username);
			$password=md5($_POST['password']);
			if($User->where("username ='$username' AND password = '$password'")->find()){
				session('username',$username);
				U('Person/index','','',true,true);
			}
			else{
				$this->error('用户名或密码错误！');
			}
		}
	}	
}