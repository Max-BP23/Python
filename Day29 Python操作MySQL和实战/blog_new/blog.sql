/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50731
Source Host           : localhost:3306
Source Database       : blog

Target Server Type    : MYSQL
Target Server Version : 50731
File Encoding         : 65001

Date: 2021-08-01 15:24:06
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `text` text NOT NULL,
  `read_count` int(11) DEFAULT '0',
  `comment_count` int(11) DEFAULT '0',
  `up_count` int(11) DEFAULT '0',
  `down_count` int(11) DEFAULT '0',
  `user_id` int(11) NOT NULL,
  `ctime` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_article_user` (`user_id`),
  CONSTRAINT `fk_article_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of article
-- ----------------------------
INSERT INTO `article` VALUES ('1', 'jwt解密', '武沛齐', '102', '10', '1', '2', '1', '2021-11-11 11:11:00');
INSERT INTO `article` VALUES ('2', '底层存储原理', 'pu于', '10000', '2', '10', '0', '1', '2021-11-11 11:11:00');
INSERT INTO `article` VALUES ('3', '学习Python', 'sql', '0', '0', '0', '0', '4', '2021-08-01 14:39:16');

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(255) NOT NULL,
  `user_id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  `ctime` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comment_user` (`user_id`),
  KEY `fk_comment_article` (`article_id`),
  CONSTRAINT `fk_comment_article` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`),
  CONSTRAINT `fk_comment_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of comment
-- ----------------------------
INSERT INTO `comment` VALUES ('1', 'wupeiqi', '1', '1', '2021-11-11 11:11:00');
INSERT INTO `comment` VALUES ('2', 'yuchao', '2', '1', '2021-11-11 11:11:00');
INSERT INTO `comment` VALUES ('3', 'alex', '3', '2', '2021-11-11 11:11:00');

-- ----------------------------
-- Table structure for up_down
-- ----------------------------
DROP TABLE IF EXISTS `up_down`;
CREATE TABLE `up_down` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `choice` tinyint(4) NOT NULL,
  `user_id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  `ctime` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_up_down_user` (`user_id`),
  KEY `fk_up_down_article` (`article_id`),
  CONSTRAINT `fk_up_down_article` FOREIGN KEY (`article_id`) REFERENCES `article` (`id`),
  CONSTRAINT `fk_up_down_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of up_down
-- ----------------------------
INSERT INTO `up_down` VALUES ('1', '1', '1', '1', '2021-11-11 11:11:00');
INSERT INTO `up_down` VALUES ('2', '0', '2', '1', '2021-11-11 11:11:00');
INSERT INTO `up_down` VALUES ('3', '1', '3', '2', '2021-11-11 11:11:00');
INSERT INTO `up_down` VALUES ('4', '0', '4', '1', '2021-08-01 15:10:14');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(16) NOT NULL,
  `nickname` varchar(16) NOT NULL,
  `mobile` char(11) NOT NULL,
  `password` varchar(64) NOT NULL,
  `email` varchar(64) NOT NULL,
  `ctime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', '\r\nwupwiqi', '武沛齐', '15131255089', '123', 'XXX@live.com', '2021-11-11 11:11:00');
INSERT INTO `user` VALUES ('2', 'yuchao', 'pu于', '19988761234', '123', 'XXXXX@XX.com', '2021-11-11 11:11:00');
INSERT INTO `user` VALUES ('3', 'alex', '土鳖', '15866541123', '123', 'ff@XX.com', '2021-11-11 11:11:00');
INSERT INTO `user` VALUES ('4', 'MAX', 'max', '18518763629', '123', '876733887@qq.com', '2021-08-01 14:30:12');
