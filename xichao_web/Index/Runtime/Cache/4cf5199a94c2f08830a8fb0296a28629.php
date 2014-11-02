<?php if (!defined('THINK_PATH')) exit();?>﻿<!DOCTYPE html>
<html lang="zh-cn">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="" />
    <meta name="keywords" content="" />
    <meta name="author" content="Nee Bee Studio" />
    
    <link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/footer.css" />
    <link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/header.css" />
    <link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/home_bookstore.css" />


    <title>曦潮书店 | 曦潮书店</title>
</head>

<body>
    <div class="container">
<!--###################################header###################################-->
        <!--###################################header###################################-->
<div class="head">
    <?php if($_SESSION['nick'] == null): ?><a class="login" href="__APP__/Login/index">登录</a><a class="register" href="__APP__/Register/index">注册</a>
        <?php else: ?><a class="login" href="#"><?php echo ($_SESSION['nick']); ?></a><a class="register" href="__APP__/Logout/logout">退出</a><?php endif; ?>
    <!--
    <a class="login" href="__APP__/Login/index">登陆</a>
    <a class="register" href="__APP__/Register/index">注册</a>
    -->

    <a class="logo" href="__APP__/Index/index"><img height="75px" src="__PUBLIC__/Images/rt_logo.png"></a>
</div>   
<div class="nav_row">
    <hr class="up">
    <a id="header_item0" href="__APP__/Index/indexStatic">首页</a>
    <a id="header_item1" href="__APP__/BookStore/index">曦潮书店</a>
    <a id="header_item2" href="#">会员</a>
    <a id="header_item3" href="#">人文</a>
    <a id="header_item4" href="#">活动</a>
    <a id="header_item5" href="__APP__/Recruit/index">招募</a>
    <hr class="down">
</div>  
        <div id="home_bookstore">
            <div id="home_bookstore_header">
                <p id="home_bookstore_little_title">○ 首页 - 曦潮书店</p>
                <div style="height:10px;"></div>
                <p id="home_bookstore_title">曦潮书店</p>
                <hr id="home_bookstore_header_down">
            </div>
            <div id="home_bookstore_body">
                <a href="__APP__/Story/index">
                    <img id="home_bookstore_body_block1" src="__PUBLIC__/Images/bookstore_block1.png"  alt="曦潮故事" />
                </a>
                <a href="__APP__/Concept/index">
                    <img id="home_bookstore_body_block2" src="__PUBLIC__/Images/bookstore_block2.png"  alt="曦潮理念" />
                </a>
                <a href="__APP__/Service/index">
                    <img id="home_bookstore_body_block3" src="__PUBLIC__/Images/bookstore_block3.png"  alt="曦潮服务" />
                </a>
                <a href="__APP__/Concrete/index">
                    <img id="home_bookstore_body_block4" src="__PUBLIC__/Images/bookstore_block4.png"  alt="实体店面" />
                </a>
            </div>
        </div>
<!--###################################footer###################################--> 
        <!--###################################footer###################################-->
<hr>
<div class="footer-body">
    <a id="footer_item1" href="#">关于我们</a>
    <a id="footer_item2" href="#" >联系我们</a>
    <a id="footer_item3" href="#" >加入我们</a>
    <a id="footer_item4" href="#" >服务声明</a>
</div>   
<div id="copyright">
    <div><b>Copyright©曦潮2014，All Right Reserved|沪ICP备xxxxxx号</b>
    </div>  
</div>   
      
    </div>
</body>






</html>