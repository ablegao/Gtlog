-- create database play28_db;

use play28_db;
DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `username` varchar(15) NOT NULL COMMENT '名称',
  `passwd` char(32) NOT NULL COMMENT '密码',
  `nickname` varchar(15) NOT NULL COMMENT '昵称',
  `mail` varchar(100) NOT NULL COMMENT '邮箱',
  `regist_ip` int(10) DEFAULT NULL COMMENT '用户注册IP Int 格式',
  `regist_time` int(11) NOT NULL COMMENT '用户注册时间',
  `login_ip` int(10) NOT NULL COMMENT '最后登录IP',
  `login_time` int(11) NOT NULL COMMENT '最后登录时间',
  `is_del` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否删除，1为删除.default 0',
  `logincount` int(11) NOT NULL COMMENT '登录次数',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COMMENT='用户表' AUTO_INCREMENT=0 ;

INSERT INTO `users` (`id`, `username`, `passwd`, `nickname`, `mail`, `regist_ip`, `regist_time`, `login_ip`, `login_time`, `is_del`, `logincount`) VALUES
(1, 'admin', '21232f297a57a5a743894a0e4a801fc3', '', 'admin@admin.com',  NULL, 0, 2130706433, 1355072975, 0, 2);


DROP TABLE IF EXISTS `blog_content`;
CREATE TABLE IF NOT EXISTS `blog_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `user_id` int(11) NOT NULL COMMENT '添加用户id',
  `cate_id`	int(11) NOT NULL DEFAULT 1 COMMENT '',
  `title` varchar(32) NOT NULL COMMENT '标题',
  `content` text NOT NULL COMMENT '标题',
  `tags`	varchar(30) NULL COMMENT '标签',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `is_del`	tinyint NOT NULL DEFAULT 0 COMMENT '删除',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COMMENT='blog正文内容表' AUTO_INCREMENT=0 ;
