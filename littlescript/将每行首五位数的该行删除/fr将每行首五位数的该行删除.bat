@echo off
::��ɽ�� 5:51 2015/11/8

::fr��ÿ������λ���ĸ���ɾ�� 
::http://www.bathome.net/thread-38036-1-1.html

::fr��һ������֧��������ʽ�����滻�������й��ߣ�
::������վ��http://baiy.cn/utils/fr/index.htm

::ȥ��-stdout������ֱ���޸�ԭ�ļ�


fr -r:"^\d{5},.*\r?\n?" -t -stdout -trc a.txt

pause