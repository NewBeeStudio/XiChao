<?php

require 'weixin.class.php';

class xichao extends wxmessage {


    public function processRequest($data) {
        // $input is the content that user inputs
        $input = $data->Content;       
        // deal with text msg from user
        if ($this->isTextMsg()) {
            switch ($input) {
                
                case 'news':
                	$this->text("news");
                 	break;

                default:
              		$this->text("HELLO WORLD");
                	break;
                   
            }         
        }
        // deal with geographical location
        elseif ($this->isLocationMsg()) {
           
        } 
        elseif ($this->isImageMsg()) {
            
        } 
        elseif ($this->isLinkMsg()) {
           
        } 
        elseif ($this->isEventMsg()) {
        	
        	if($data->Event=='subscribe'){
        		$this->text('曦潮书店test');
        	}

            if($data->Event=='CLICK'){
               
               switch($data->EventKey){
                   case 'V1001_CLICK1': 
                        $this->text('hello world');
                        break;
                   case 'V1001_CLICK2': 
                        $this->text("HELLO WORLD");
                        break;
                    
                }
            }
            
        } 
        else {
            
        }
    }

   
    /**
     * return news
     */
    private function news($title,$description,$picurl,$url) {
        
        $posts = array(
            array(
                'title' => $title,
                'discription' => $description,
                'picurl' => $picurl,
                'url' => $url,
            )
        );
        $xml = $this->outputNews($posts);
        header('Content-Type: application/xml');
        echo $xml;
    }

    /**
     * return text
     */
    private function text($text) {
        $xml = $this->outputText($text);
        header('Content-Type: application/xml');
        echo $xml;
    }

        
	/**
     * return music
     */
    private function music($title,$discription,$musicurl,$hdmusicurl) {
        $music = array(
            'title' => $title,
            'discription' => $discription,
            'musicurl' => $musicurl,
            'hdmusicurl' => $hdmusicurl
        );
        $xml = $this->outputMusic($music);
        //sae_log($xml);
        header('Content-Type: application/xml');
        echo $xml;
    }

   

    /**
     * Pre processing，common usage:save the request into your database.
	 * Because weixin save your msgs only 5 days.
     * @return boolean
     */
    protected function beforeProcess($postData) {

        return true;
    }

    protected function afterProcess() {
    }

    public function errorHandler($errno, $error, $file = '', $line = 0) {
        $msg = sprintf('%s - %s - %s - %s', $errno, $error, $file, $line);
    }

    public function errorException(Exception $e) {
        $msg = sprintf('%s - %s - %s - %s', $e->getCode(), $e->getMessage(), $e->getFile(), $e->getLine());
    }

    private function saveRequest($request) {
        
    }

}
