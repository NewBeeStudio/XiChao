<?php

require 'weixin.class.php';

$ret=wxcommon::getToken();
$ACCESS_TOKEN=$ret['access_token'];
$menuPostData='{
  				 "button":[
					 {	
						  "type":"view",
						  "name":"曦潮",
						  "url":"http://www.baidu.com/"
					  },
					  {
						   "type":"view",
						   "name":"新蜂",
						   "url":"http://www.soso.com/"
					  },
					  {
						   "name":"菜单",
						   "sub_button":[
							{
							   "type":"click",
							   "name":"test1",
							   "key":"V1001_CLICK1"
							},
							{
							   "type":"click",
							   "name":"test2",
							   "key":"V1001_CLICK2"
							}]
					   }]
				 }';
         
// create new menu
$wxmenu=new wxmenu($ACCESS_TOKEN);	 
$create=$wxmenu->createMenu($menuPostData);

//get current menu
$get=$wxmenu->getMenu();
var_dump($get);

//delete current menu
//$del=$wxmenu->deleteMenu();
//var_dump($del);
