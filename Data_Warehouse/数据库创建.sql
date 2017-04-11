/** 数据仓库测试 **/

-- 1、创建数据库

create database source
on primary
(
	/* 数据文件的具体描述 */
	name = 'source_data',	--主数据文件的逻辑名称
	filename = 'F:\project\source_data.mdf',	--主数据文件的物理名称
	size = 5mb,	--主数据文件的初始大小
	maxsize = 100mb,	--主数据文件增长的最大值
	filegrowth = 15%	--主数据文件的增长率
)

log on 
(
 /* 日志文件的具体描述，各参数含义同上 */
	name = 'source_log',
	filename = 'F:\project\source_log.ldf',
	size = 5mb,
	filegrowth = 1 mb
)
