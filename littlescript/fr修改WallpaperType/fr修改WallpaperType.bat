@echo off
::��ɽ�� 1:54 2015/11/9

::fr�޸�WallpaperType 
::http://www.bathome.net/thread-38056-1-1.html

::fr��һ������֧��������ʽ�����滻�������й��ߣ�
::������վ��http://baiy.cn/utils/fr/index.htm

::ȥ��-stdout������ֱ���޸�ԭ�ļ�

::ֱ���޸�ԭ�ļ�
fr -r:"\"WallpaperType\":\d+," -t:"\"WallpaperType\":1," -trc x.json


::�޸ĵ����ݣ�ԭ�ļ����޸�,�ض�����������ļ���
fr -r:"\"WallpaperType\":\d+," -t:"\"WallpaperType\":1," -stdout -trc x.json>test.txt

pause
