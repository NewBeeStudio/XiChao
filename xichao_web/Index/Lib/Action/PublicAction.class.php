<?php

//公用控制器

class PublicAction extends Action{
	//验证码生成
	Public function verify(){
		import('ORG.Util.Image');
		Image::buildImageVerify();
	}
}