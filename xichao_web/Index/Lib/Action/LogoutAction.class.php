<?php

class LogoutAction extends Action{
	Public function logout(){
		session('nick',null);
		$this->success('您已成功注销！');
	}
}