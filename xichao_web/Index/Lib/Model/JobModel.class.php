<?php
class JobModel extends Model{
	//自动验证
	protected $_validate = array(
		/*
		array('verify','require','验证码必须！'),
		//array('verify','checkVerify','验证码不正确！',0,'callback'),
		array('verify','checkVerify','验证码不正确！',0,'function'),
		*/
		array('appl-name','require','姓名必须！'),
		array('appl-gender','require','性别必须'),
		array('appl-grade','require','年级必须'),
		array('appl-major','require','专业必须'),
		array('appl-addr','require','地址必须'),
		array('appl-email','require','邮箱必须'),
		array('appl-email','email','邮箱地址不正确'),
		array('appl-phone','require','联系电话必须'),
		array('appl-intro0','require','自我介绍必须'),
		array('appl-intro1','require','优势阐述必须'),
		array('appl-intro2','require','加入理由必须'),
		array('free-time-1','require','第一个空闲时间必须'),
		array('free-time-2','require','第二个空闲时间必须'),
		array('appl-worktime','require','每周可工作的时间段必须'),
		//array('age','require','年龄必须！'),
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