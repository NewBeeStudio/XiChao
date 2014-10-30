<?php
class TalentModel extends Model{
	//自动验证
	protected $_validate = array(
		array('verify','require','验证码必须！'),
		//array('verify','checkVerify','验证码不正确！',0,'callback'),
		array('verify','checkVerify','验证码不正确！',0,'function'),
		array('name','require','姓名必须！'),
		array('age','require','年龄必须！'),
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
		array('create_time','time',1,'function'),
		);
}