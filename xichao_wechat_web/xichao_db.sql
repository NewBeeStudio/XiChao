



-- ---
-- Globals
-- ---

-- SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
-- SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'xichao_article'
-- 
-- ---

DROP TABLE IF EXISTS `xichao_article`;
		
CREATE TABLE `xichao_article` (
  `id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  `title` MEDIUMTEXT NULL DEFAULT NULL,
  `image_path` VARCHAR(256) NULL DEFAULT NULL,
  `article` MEDIUMTEXT NULL DEFAULT NULL,
  `category` INTEGER NULL DEFAULT NULL,
  `posttime` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- ---
-- Table 'xichao_comments'
-- 
-- ---

DROP TABLE IF EXISTS `xichao_comments`;
		
CREATE TABLE `xichao_comments` (
  `comment_id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  `comment` MEDIUMTEXT NULL DEFAULT NULL,
  `comment_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `poster_id` VARCHAR(256) NULL DEFAULT NULL,
  `articleID` INTEGER NULL DEFAULT NULL,
  PRIMARY KEY (`comment_id`)
);

-- ---
-- Foreign Keys 
-- ---


-- ---
-- Table Properties
-- ---

-- ALTER TABLE `xichao_article` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `xichao_comments` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Test Data
-- ---

-- INSERT INTO `xichao_article` (`id`,`title`,`image_path`,`article`,`category`,`posttime`) VALUES
-- ('','','','','','');
-- INSERT INTO `xichao_comments` (`comment_id`,`comment`,`comment_time`,`poster_id`,`articleID`) VALUES
-- ('','','','','');


