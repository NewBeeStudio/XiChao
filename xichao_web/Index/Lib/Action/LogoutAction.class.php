<?php

class LogoutAction extends Action{
	Public function logout(){
		session('username',null);
		$this->success('您已成功注销！',U('Index/index'));
	}
}