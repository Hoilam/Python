/** ���ݲֿ���� **/

-- 1���������ݿ�

create database source
on primary
(
	/* �����ļ��ľ������� */
	name = 'source_data',	--�������ļ����߼�����
	filename = 'F:\project\source_data.mdf',	--�������ļ�����������
	size = 5mb,	--�������ļ��ĳ�ʼ��С
	maxsize = 100mb,	--�������ļ����������ֵ
	filegrowth = 15%	--�������ļ���������
)

log on 
(
 /* ��־�ļ��ľ�������������������ͬ�� */
	name = 'source_log',
	filename = 'F:\project\source_log.ldf',
	size = 5mb,
	filegrowth = 1 mb
)
