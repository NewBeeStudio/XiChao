<?php

//曦潮主页

class IndexAction extends Action {
	//曦潮主页界面显示
    public function index(){
    	$this->display();
    }

    public function indexStatic(){
    	$this->display();
    }
}