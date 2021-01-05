-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2021-01-05 18:50:32
-- 服务器版本： 5.6.50-log
-- PHP 版本： 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `sql_course`
--

-- --------------------------------------------------------

--
-- 表的结构 `lease`
--

CREATE TABLE `lease` (
  `username` varchar(20) NOT NULL COMMENT '登陆账号',
  `name` varchar(20) NOT NULL COMMENT '租客姓名',
  `link` varchar(255) NOT NULL COMMENT '联系方式',
  `use` varchar(255) DEFAULT NULL COMMENT '租房用途',
  `uuid` int(60) NOT NULL COMMENT '发布id'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 触发器 `lease`
--
DELIMITER $$
CREATE TRIGGER `del` AFTER DELETE ON `lease` FOR EACH ROW begin
	UPDATE publish 
	SET flag=0
	where uuid=old.uuid;
end
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `insert` AFTER INSERT ON `lease` FOR EACH ROW begin
	UPDATE publish 
	SET flag=1 
	where uuid=new.uuid;
end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- 表的结构 `login`
--

CREATE TABLE `login` (
  `username` varchar(20) NOT NULL COMMENT '登陆账号',
  `password` varchar(20) NOT NULL COMMENT '登陆密码',
  `count` decimal(10,2) NOT NULL COMMENT '共收',
  `deliver` decimal(10,2) NOT NULL COMMENT '交付',
  `balance` decimal(10,2) NOT NULL COMMENT '余额'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `login`
--

INSERT INTO `login` (`username`, `password`, `count`, `deliver`, `balance`) VALUES
('honus', '123456', '600.00', '480.00', '120.00');

-- --------------------------------------------------------

--
-- 表的结构 `publish`
--

CREATE TABLE `publish` (
  `username` varchar(20) NOT NULL COMMENT '登陆账号',
  `name` varchar(20) NOT NULL COMMENT '用户名',
  `address` varchar(255) NOT NULL COMMENT '地址',
  `room` varchar(255) NOT NULL COMMENT '房号',
  `unit_type` varchar(255) NOT NULL COMMENT '户型',
  `price` decimal(10,2) NOT NULL COMMENT '出租价格',
  `link` varchar(255) NOT NULL COMMENT '联系方式',
  `flag` int(1) NOT NULL COMMENT '标识出租与否',
  `uuid` int(60) NOT NULL COMMENT '该发布信息id',
  `begintime` int(255) NOT NULL COMMENT '开始时间',
  `endtime` int(255) UNSIGNED NOT NULL COMMENT '结束时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `publish`
--

INSERT INTO `publish` (`username`, `name`, `address`, `room`, `unit_type`, `price`, `link`, `flag`, `uuid`, `begintime`, `endtime`) VALUES
('hzy', 'hzy', '中国石油大学(华东)', '19号楼', '一室一厅', '400.00', '15784938293', 0, 19297844, 1609776000, 1669219200),
('gh', 'gh', '山东省青岛市黄岛区', '19号楼', '三室一厅', '400.00', '15789483829', 0, 19418919, 1611763200, 1795061063),
('guowei', 'gw', '山西省', '山西大道70号', '三室一厅', '500.00', '16598569851', 0, 27824647, 1609827872, 1795104000);

-- --------------------------------------------------------

--
-- 表的结构 `unit_type`
--

CREATE TABLE `unit_type` (
  `type` varchar(255) NOT NULL,
  `count` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `unit_type`
--

INSERT INTO `unit_type` (`type`, `count`) VALUES
('一室一厅', 0),
('三室一厅', 0),
('两室一厅', 0),
('四室两厅', 0);

--
-- 转储表的索引
--

--
-- 表的索引 `lease`
--
ALTER TABLE `lease`
  ADD PRIMARY KEY (`uuid`) USING BTREE;

--
-- 表的索引 `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`username`);

--
-- 表的索引 `publish`
--
ALTER TABLE `publish`
  ADD PRIMARY KEY (`uuid`) USING BTREE;

--
-- 表的索引 `unit_type`
--
ALTER TABLE `unit_type`
  ADD PRIMARY KEY (`type`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
