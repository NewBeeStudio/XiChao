<?php

//曦潮会员注册

class RegisterAction extends Action{
	//会员注册页面显示
	Public function index(){
		$this->display();
	}
	//会员注册验证
	Public function register(){
		if(!IS_POST) _404('页面不存在',U('index'));//debug开启时显示页面不存在，debug关闭时，自动跳转到index操作
		$User=D('User');
		if($User->create()){//create方法会自动验证和自动完成post提交的数据
			session('username',$_POST['username']);
			$result=$User->add();
			if($result){
				$this->success('注册成功',U('Index/index'));
			}else{
				$this->error('写入错误');
			}
		}else{
			$this->error($User->getError());
		}
	}
}