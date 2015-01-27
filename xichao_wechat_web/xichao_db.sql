DROP TABLE IF EXISTS `article_category`;
    
CREATE TABLE `article_category` (
  `id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  `name` VARCHAR(128) NULL DEFAULT NULL,
  `description` VARCHAR(512) NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
);

DROP TABLE IF EXISTS `xichao_article`;
 	
CREATE TABLE `xichao_article` (
  `id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  `title` MEDIUMTEXT NULL DEFAULT NULL,
  `image_path` VARCHAR(256) NULL DEFAULT NULL,
  `article` MEDIUMTEXT NULL DEFAULT NULL,
  `category` INTEGER NULL DEFAULT NULL,
  `posttime` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `top` INTEGER NULL DEFAULT 0,
  foreign key (category) references article_category(id) ON DELETE CASCADE ON UPDATE CASCADE,
  PRIMARY KEY (`id`)
);


-- DROP TABLE IF EXISTS `xichao_comments`;
  
-- CREATE TABLE `xichao_comments` (
--   `comment_id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
--   `comment` MEDIUMTEXT NULL DEFAULT NULL,
--   `comment_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
--   `poster_id` VARCHAR(256) NULL DEFAULT NULL,
--   `articleID` INTEGER NULL DEFAULT NULL,
--   PRIMARY KEY (`comment_id`)
-- );





-- ---
-- Test Data
-- ---
--  INSERT INTO `article_category` (`id`,`name`) VALUES('1','0.48南洋荐书');
--  INSERT INTO `article_category` (`id`,`name`) VALUES('2','树枝态度');

--  INSERT INTO `article_category` (`id`,`name`) VALUES('3','嗜书瘾君子');

--  INSERT INTO `article_category` (`id`,`name`) VALUES('4','一只球球');

--  INSERT INTO `article_category` (`id`,`name`) VALUES('5','曦潮温度');


-- -- ---
-- Table Properties
-- ---

ALTER TABLE `article_category` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE `xichao_article` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE `xichao_comments` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
ALTER TABLE `article_category` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- -

