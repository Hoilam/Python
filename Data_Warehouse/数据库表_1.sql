/** 创建数据库表 **/
USE source
GO

-- 创建客户表
create table customer
(
	customer_number int not null identity(1,1) primary key,-- '客户编号，主键'
	customer_name varchar(50), -- '客户名称'
	customer_street_address varchar(50), --'客户住址'
	customer_zip_code int, --'邮编'
	customer_city varchar(30), --'所在城市'
	customer_state varchar(2) --'所在省份' 
);

-- 创建产品表
create table product
(
	product_code int not null identity(1,1) primary key,--'产品编码，主键'
	product_name varchar(30), --'产品名称'
	product_category varchar(30) --'产品类型'
);

-- 创建销售订单表
create table sales_order
(
	order_number int not null identity(1,1) primary key, --'订单号，主键'
	customer_number int, --'客户编号'
	product_code int, --'产品编码'
	order_date date, --'订单日期'
	entry_date date, --'登记日期'
	order_amount decimal(10,2) --'销售金额'
	foreign key(customer_number) references customer(customer_number) on delete cascade on update cascade,
	foreign key(product_code) references product(product_code) on delete cascade on update cascade
);


/** 数据仓库表 **/

USE source
GO

-- 创建客户维度表
create table dim_customer
(
	customer_sk int not null identity(1,1) primary key,--'主键，代理件'
	customer_number int, --'客户编号，业务主键'
	customer_name varchar(50), --'客户名称'
	customer_street_address varchar(50), --'客户住址'
	customer_zip_code int, --'邮编'
	customer_city varchar(30), --'所在城市'
	customer_state varchar(2), --'所在省份'
	effective_date date, --'生效日期'
	expiry_date date --'到期日期'
);

-- 创建产品维度表
create table dim_product
(
	product_sk int not null identity(1,1) primary key, --'主键，代理键'
	product_code int, --'产品编码，业务主键'
	product_name varchar(30), --'产品名称'
	product_category varchar(30), --'产品类型'
	effective_date date, --'生效日期'
	expiry_date date --'到货日期'
);

-- 创建订单维度表
create table dim_order
(
	order_sk int not null identity(1,1) primary key, --'主键，代理键'
	order_number int, --'订单号，业务主键'
	effective_date date, --'生效日期'
	expiry_date date --'到期日期'
)

-- 创建日期维度表
create table dim_date
(
	date_sk int not null identity(1,1) primary key, --'主键，代理键'
	date date, --'日期'
	month_name varchar(9), --'月份名称'
	month tinyint, --'月份'
	quarter tinyint, --'季度'
	year smallint, --'年'
	effective_date date, --'生效日期'
	expiry_date date--'到货日期'
)

-- 创建销售订单事实表
create table fact_sales_order
(
	order_sk int, --'订单维度主键'
	customer_sk int, --'客户维度主键'
	product_sk int, --'产品维度主键'
	order_date_sk int, --'日期维度主键'
	order_amount decimal(10,2) --'销售金额'
	foreign key(order_sk) references dim_order(order_sk) on delete cascade on update cascade,
	foreign key(customer_sk) references dim_customer(customer_sk) on delete cascade on update cascade,
	foreign key(product_sk) references dim_product(product_sk) on delete cascade on update cascade,
	foreign key(order_date_sk) references dim_date(date_sk) on delete cascade on update cascade
);


/** 创建过渡表 **/

-- 创建产品过渡表
create table product_stg
(
	product_code int,
	product_name varchar(30),
	product_category varchar(30)
);

-- 创建客户过渡表
create table customer_stg
(
	customer_number int,
	customer_name varchar(30),
	customer_street_address varchar(30),
	customer_zip_code int,
	custoemr_city varchar(30),
	customer_state varchar(2)
);
















































