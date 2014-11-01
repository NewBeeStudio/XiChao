<?php if (!defined('THINK_PATH')) exit();?><!DOCTYPE html>
<html lang="zh-cn">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>曦潮书店 | 青春校园，人文曦潮</title>
    <meta name="description" content="" />
    <meta name="keywords" content="" />
    <meta name="author" content="Nee Bee Studio" />

    <link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/index.css" />
    <link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/footer.css" />
    <link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/header.css" />


    <script src="__PUBLIC__/Js/jquery.min.js"></script>
    <script src="__PUBLIC__/Js/index.js"></script>
</head>

<body>
    <div id="pt-main" class="pt-perspective">
<!--###################################animate###################################-->
        <div class="pt-page1">
            <img id="bgimg1" src="__PUBLIC__/Images/bgimg1.jpg">
            <img id="bgimg2" src="__PUBLIC__/Images/bgimg2.png">
            <img id="page1_up" src="__PUBLIC__/Images/white.png">
            <img id="page1_down" src="__PUBLIC__/Images/white.png">
            <img id="logo_tran" src="__PUBLIC__/Images/logo_tran.png">
            <img id="logo_blue" src="__PUBLIC__/Images/logo_blue.png">
        </div>
<!--###################################index###################################-->
        <div class="pt-page2">
            <div class="container">
                <div class="main_page">
<!--###################################header###################################-->
                    <!--###################################header###################################-->
<div class="head">
    <?php if($_SESSION['nick'] == null): ?><a class="login" href="__APP__/Login/index">登录</a><a class="register" href="__APP__/Register/index">注册</a>
        <?php else: ?><a class="login" href="#"><?php echo ($_SESSION['nick']); ?></a><a class="register" href="__APP__/Logout/logout">注销</a><?php endif; ?>
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
<!--###################################content###################################-->
                    <div class="main_page_content">
                        <div class="main_page_content_1">
                            <img id="bgimg2_1" src="__PUBLIC__/Images/bgimg2.png">
                            <img id="logo_blue_1" src="__PUBLIC__/Images/logo_blue.png">
                        </div>
                        <div class="main_page_content_2">
                            <img id="require" src="__PUBLIC__/Images/require.png">
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
        </div>
    </div>
</div>
</body>

</html>