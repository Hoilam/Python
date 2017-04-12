/** �������ݿ�� **/
USE source
GO

-- �����ͻ���
create table customer
(
	customer_number int not null identity(1,1) primary key,-- '�ͻ���ţ�����'
	customer_name varchar(50), -- '�ͻ�����'
	customer_street_address varchar(50), --'�ͻ�סַ'
	customer_zip_code int, --'�ʱ�'
	customer_city varchar(30), --'���ڳ���'
	customer_state varchar(2) --'����ʡ��' 
);

-- ������Ʒ��
create table product
(
	product_code int not null identity(1,1) primary key,--'��Ʒ���룬����'
	product_name varchar(30), --'��Ʒ����'
	product_category varchar(30) --'��Ʒ����'
);

-- �������۶�����
create table sales_order
(
	order_number int not null identity(1,1) primary key, --'�����ţ�����'
	customer_number int, --'�ͻ����'
	product_code int, --'��Ʒ����'
	order_date date, --'��������'
	entry_date date, --'�Ǽ�����'
	order_amount decimal(10,2) --'���۽��'
	foreign key(customer_number) references customer(customer_number) on delete cascade on update cascade,
	foreign key(product_code) references product(product_code) on delete cascade on update cascade
);


/** ���ݲֿ�� **/

USE source
GO

-- �����ͻ�ά�ȱ�
create table dim_customer
(
	customer_sk int not null identity(1,1) primary key,--'�����������'
	customer_number int, --'�ͻ���ţ�ҵ������'
	customer_name varchar(50), --'�ͻ�����'
	customer_street_address varchar(50), --'�ͻ�סַ'
	customer_zip_code int, --'�ʱ�'
	customer_city varchar(30), --'���ڳ���'
	customer_state varchar(2), --'����ʡ��'
	effective_date date, --'��Ч����'
	expiry_date date --'��������'
);

-- ������Ʒά�ȱ�
create table dim_product
(
	product_sk int not null identity(1,1) primary key, --'�����������'
	product_code int, --'��Ʒ���룬ҵ������'
	product_name varchar(30), --'��Ʒ����'
	product_category varchar(30), --'��Ʒ����'
	effective_date date, --'��Ч����'
	expiry_date date --'��������'
);

-- ��������ά�ȱ�
create table dim_order
(
	order_sk int not null identity(1,1) primary key, --'�����������'
	order_number int, --'�����ţ�ҵ������'
	effective_date date, --'��Ч����'
	expiry_date date --'��������'
)

-- ��������ά�ȱ�
create table dim_date
(
	date_sk int not null identity(1,1) primary key, --'�����������'
	date date, --'����'
	month_name varchar(9), --'�·�����'
	month tinyint, --'�·�'
	quarter tinyint, --'����'
	year smallint, --'��'
	effective_date date, --'��Ч����'
	expiry_date date--'��������'
)

-- �������۶�����ʵ��
create table fact_sales_order
(
	order_sk int, --'����ά������'
	customer_sk int, --'�ͻ�ά������'
	product_sk int, --'��Ʒά������'
	order_date_sk int, --'����ά������'
	order_amount decimal(10,2) --'���۽��'
	foreign key(order_sk) references dim_order(order_sk) on delete cascade on update cascade,
	foreign key(customer_sk) references dim_customer(customer_sk) on delete cascade on update cascade,
	foreign key(product_sk) references dim_product(product_sk) on delete cascade on update cascade,
	foreign key(order_date_sk) references dim_date(date_sk) on delete cascade on update cascade
);


/** �������ɱ� **/

-- ������Ʒ���ɱ�
create table product_stg
(
	product_code int,
	product_name varchar(30),
	product_category varchar(30)
);

-- �����ͻ����ɱ�
create table customer_stg
(
	customer_number int,
	customer_name varchar(30),
	customer_street_address varchar(30),
	customer_zip_code int,
	custoemr_city varchar(30),
	customer_state varchar(2)
);
















































