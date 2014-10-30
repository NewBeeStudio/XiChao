<?php

class PersonAction extends Action{
	//个人主页显示
	Public function index(){
		if(session('?username')){
			$this->assign('username',session('username'));

			$User=M('User');
			/*
			继续读取数据库信息
			*/
			$this->display();
		}
	}
}