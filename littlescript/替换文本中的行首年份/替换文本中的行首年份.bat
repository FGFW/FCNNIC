goto code
::ע����
�滻�ı��е��������
fr ���ط���ͬsed
���߰�װbatch-cn ����bcn gt fr�����������
http://baiy.cn/utils/fr/index.htm

:code
copy a1.txt aa1.txt /y

::fr aa1.txt -r:(^2015)(/\d+/\d+) -t:"2013\2"
::fr aa1.txt -r:(^2014)(/\d+/\d+) -t:"2012\2"

::ʹ��^�޶��滻���׵����
fr aa1.txt -r:^2015 -t:2013
fr aa1.txt -r:^2014 -t:2012

pause
