<?php
/**
 * Useage
 * weixin.class.php is the main class. It  encloses all functions that weixin  supplies.
 * You need to inherit this class (example: defaultweixin.php), and then rewrite the
 * processRequest method
 */

require 'xichao.php';
$weixin = new xichao();
$weixin->run();
exit(0);
