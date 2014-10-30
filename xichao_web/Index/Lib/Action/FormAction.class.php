<?php

//曦潮报名表处理


class FormAction extends Action{

	//报名表处理
	Public function formHandle(){
		if(!IS_POST) _404('页面不存在',U('index'));//debug开启时显示页面不存在，debug关闭时，自动跳转到index操作
		$Job=D('Job');
		if($Job->create()){//create方法会自动验证和自动完成post提交的数据
			$result=$Job->add();
			if($result){
				$this->success('申请成功');//,U('Index/index'));
			}else{
				$this->error('写入错误');
			}
		}else{
			$this->error($Job->getError());
		}
	}
/*
	//曦潮人才库报名表处理
	Public function talentHandle(){
		if(!IS_POST) _404('页面不存在',U('index'));//debug开启时显示页面不存在，debug关闭时，自动跳转到index操作
		$Talent=D('Talent');
		if($Talent->create()){//create方法会自动验证和自动完成post提交的数据
			$result=$Talent->add();
			if($result){
				$this->success('申请成功',U('Index/index'));
			}else{
				$this->error('写入错误');
			}
		}else{
			$this->error($Talent->getError());
		}
	}
	*/
}