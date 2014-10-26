<?php
	function checkUsername($username){
		$User=M('User');
		$data=$User->find($username);
		if($data){
			return true;
		}
		return false;
	}
	function checkVerify($data){
		if(session('verify') != md5($data)){
			return false;
		}
		return true;
	}
?>