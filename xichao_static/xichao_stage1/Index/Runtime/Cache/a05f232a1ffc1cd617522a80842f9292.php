<?php if (!defined('THINK_PATH')) exit();?>
<!DOCTYPE html>
<html lang="zh-cn">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="" />
    <meta name="keywords" content="" />
    <meta name="author" content="Nee Bee Studio" />
    <link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/header.css" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>曦潮书店 | 曦潮记</title>
    
    <link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/inputstyle.css">
    <link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/button.css">
    <link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/xichaoji.css">
    <link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/jquery-ui.css">
        <link rel="stylesheet" type="text/css" href="__PUBLIC__/Css/footer.css" />

    <script src="__PUBLIC__/Js/jquery.min.js"></script>
    <script src="__PUBLIC__/Js/jquery-ui.min.js"></script>
    <script src="__PUBLIC__/Js/formslide.js"></script>
</head>

<body>
    <div class="container">
        <div class="main_page">
            
<!--  ################################### header ###################################    -->
            
            <div class="head">
                <a class="login" href="__APP__/Login/index">登陆</a>
                <a class="register" href="__APP__/Register/index">注册</a>
                <a class="logo" href="__APP__/Index/index"><img height="75px" src="__PUBLIC__/Images/rt_logo.png"></a>
            </div>   
             
            <div class="nav_row">
                <hr class="up">
                <a id="header_item1" href="#">曦潮书店</a>
                <a id="header_item2" href="#">会员</a>
                <a id="header_item3" href="#">人文</a>
                <a id="header_item4" href="#">活动</a>
                <a id="header_item5" href="__APP__/Recruit/index">招募</a>
                <hr class="down">
            </div>  
            
            
           <div id = "xichaoji">

<!--  ################################### main ###################################    -->
<h1 id="header">曦潮记</h1>

<div id="brief-intro">
招募文化创意产品项目，从人文的视角出发，还原并挖掘演化产品本身的功能与材质，实现曦潮“本然如初”的文化理念内核，达成质朴创新的视觉呈现与产品概念。<br>
欢迎产品设计类和项目协调类人才加入。

</div>



<div>
<button type="button" id="appl-start" class="button appl-start">我要报名</button>
<br><br>
</div>

<div id = "appl-sheet">
<!--  ################################### form ###################################    -->

<form action="__APP__/Form/formHandle" method="post" id = "appl-form">
<div class = "form-element" id = "appl-title" align="center">
<strong>曦潮招募报名表</strong>
<br><br>
</div>
<div class = "form-element">
    <label id="name-label">
        姓名:
        <input type="text" name="appl-name" id="appl-name" class="appl-input">
    </label>
    <label id="gender-label">
        性别:
        <input type="text" name="appl-gender" id="appl-gender" class="appl-input">
    </label>
    <label id="grade-label">
        年级:
        <input type="text" name="appl-grade" id="appl-grade" class="appl-input">
    </label>
    <label id="studentid-label">
        学号:
        <input type="text" name="appl-studentid" id="appl-studentid" class="appl-input">
    </label>
</div>

<div class = "form-element">
    <label id="major-label">
        学院/专业:
        <input type="text" name="appl-major" id="appl-major" class="appl-input">
    </label>
    <label id="addr-label">
        校内地址:
        <input type="text" name="appl-addr" id="appl-addr" class="appl-input">
    </label>
</div>

<div class = "form-element">
    <label id="major-label">
        邮箱:
        <input type="text" name="appl-email" id="appl-email" class="appl-input">
    </label>
    <label id="addr-label">
        联系电话:
        <input type="text" name="appl-phone" id="appl-phone" class="appl-input">
    </label>
</div>

<div class = "form-element">
    您是否愿意加入？(请保留您选择的项目)
</div>


<div class = "form-element">
    <label>
        -曦潮内质网
        <input type="radio" id="radio-1-1" class = "regular-radio big-radio" name="if-jiguangpianyu" value="1">
        <label for="radio-1-1"></label>
        是
        <input type="radio" id="radio-1-2" class = "regular-radio big-radio" name="if-jiguangpianyu" value="0" checked>
        <label for="radio-1-2"></label>
        否
    </label>
</div>

<div class = "form-element">
    <label>
        -曦潮线粒体
        <input type="radio" id="radio-2-1" class = "regular-radio big-radio" name="if-mitochondria" value="1">
        <label for="radio-2-1"></label>
        是
        <input type="radio" id="radio-2-2" class = "regular-radio big-radio" name="if-mitochondria" value="0" checked>
        <label for="radio-2-2"></label>
        否
    </label>
    <label style="margin-left: 70px">(以下岗位最多填报三项)</label>
</div>

<div class = "form-element">
<ul>
    <li class="choice-line">
        曦潮一组(“当下即是”书香生态系统)：
        <br>
        <input type="checkbox" id="checkbox-1-1" class = "regular-checkbox" name="appl-web" value="1">
        <label for="checkbox-1-1"></label>
        网站开发
        <input type="checkbox" id="checkbox-1-2" class = "regular-checkbox" name="appl-app" value="1">
        <label for="checkbox-1-2"></label>
        移动终端开发
        <input type="checkbox" id="checkbox-1-3" class = "regular-checkbox" name="appl-interactive-design" value="1">
        <label for="checkbox-1-3"></label>
        交互性设计
        <input type="checkbox" id="checkbox-1-4" class = "regular-checkbox" name="appl-operation-maintenance" value="1">
        <label for="checkbox-1-4"></label>
        运营维护
        <input type="checkbox" id="checkbox-1-5" class = "regular-checkbox" name="appl-homepage" value="1">
        <label for="checkbox-1-5"></label>
        主页菌
    </li>
    <li class="choice-line">
        曦潮二组(带状活动，外联及文化合作)：
        <br>
        <input type="checkbox" id="checkbox-2-1" class = "regular-checkbox" name="appl-lecture" value="1">
        <label for="checkbox-2-1"></label>
        讲座策划统筹
        <input type="checkbox" id="checkbox-2-2" class = "regular-checkbox" name="appl-movie" value="1">
        <label for="checkbox-2-2"></label>
        电影播放策划统筹
        <input type="checkbox" id="checkbox-2-3" class = "regular-checkbox" name="appl-image" value="1">
        <label for="checkbox-2-3"></label>
        影像记录剪辑
        <input type="checkbox" id="checkbox-2-4" class = "regular-checkbox" name="appl-report" value="1">
        <label for="checkbox-2-4"></label>
        文艺报道        
    </li>
    <li class="choice-line">
        曦潮三组(曦潮运行)：
        <br>
        <input type="checkbox" id="checkbox-3-1" class = "regular-checkbox" name="appl-office" value="1">
        <label for="checkbox-3-1"></label>
        日常办公
        <input type="checkbox" id="checkbox-3-2" class = "regular-checkbox" name="appl-window" value="1">
        <label for="checkbox-3-2"></label>
        窗口服务
        <input type="checkbox" id="checkbox-3-3" class = "regular-checkbox" name="appl-mitochondrion-service" value="1">
        <label for="checkbox-3-3"></label>
        线粒体服务岗
    </li>
    <li class="choice-line">
        曦潮四组(曦潮设计组)：
        <br>
        <input type="checkbox" id="checkbox-4-1" class = "regular-checkbox" name="appl-plane-design" value="1">
        <label for="checkbox-4-1"></label>
        校园文化平面设计
        <input type="checkbox" id="checkbox-4-2" class = "regular-checkbox" name="appl-product-design" value="1">
        <label for="checkbox-4-2"></label>
        产品设计
    </li>

</ul>
</div>

<div class = "form-element">
    <label>
        自我介绍(包括但不限于: 性格特点、个人经历、兴趣和特长等)
        <br>
        <textarea type="text" name="appl-intro0" id="appl-intro0" class="appl-input"></textarea>
    </label>
</div>

<div class = "form-element">
    <label>
        您认为加入曦潮，您的优势在于:<br>
        (曾经参与过的活动、项目、实习经历具体说明，或任何能展现您个人风格、魅力的事例)
        <br>
        <textarea type="text" name="appl-intro1" id="appl-intro1" class="appl-input"></textarea>
    </label>
</div>

<div class = "form-element">
    <label>
        您认为加入曦潮的原因
        <br>
        <textarea type="text" name="appl-intro2" id="appl-intro2" class="appl-input"></textarea>
    </label>
</div>

<div class = "form-element">
    <label>请选择您可以面试的时间(请选择两个时间)</label><br>
    第一个时间:
    <input type="text" id="appl-freedate1" class="appl-input" readonly="readonly" name="free-time-1"/>
    第二个时间:
    <input type="text" id="appl-freedate2" class="appl-input" readonly="readonly" name="free-time-2"/>    
</div>

<div class = "form-element">
    <label>
        请说明您可以每周工作的时间段:
        <br>
        <textarea type="text" name="appl-worktime" id="appl-worktime" class="appl-input"></textarea>
    </label>
</div>

<div class = "form-element">
    <label>
        <u>特别说明: 曦潮线粒体为长期招募，持续接受简历。</u><br>
        <u>在第二轮面试之后，第三轮面试启动时间未定</u>
    </label>
</div>

<div>
<input type="submit" id="appl-submit" class="button appl-submit" value="提交" />

</div>

</form>

</div>


            
           </div>
<!--  ################################### footer ###################################    -->

           <div class="main_page">
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
</body>






</html>