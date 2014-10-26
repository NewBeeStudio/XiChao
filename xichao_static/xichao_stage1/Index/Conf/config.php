<?php
return array(
	//'配置项'=>'配置值'
	//数据库配置参数
	'DB_HOST'=>'localhost',
	'DB_USER'=>'root',
	'DB_PWD'=>'',
	'DB_NAME'=>'xichao',
	'DB_PREFIX'=>'think_',

	//模板文件的后缀名
	'TMPL_TEMPLATE_SUFFIX' => '.html',

	//U函数生成的URL的伪静态后缀名
	'URL_HTML_SUFFIX' => '',//html，htm都可以

	//pathinfo模式http://localhost/wish/Index.php/Index/show
	//还是普通模式http://localhost/wish/Index.php?m=Index&a=show
	//方便U函数来生成各种模式的URL
	'URL_MODEL' => 1,//0或者2
	//设置默认过滤函数
	'DEFAULT_FILTER' => 'htmlspecialchars'
);
?>