# -*- coding: utf-8 -*-
"""
���������һ����Ȥ�����ӣ���Ҫʹ����deque��rotate������ʵ����һ������ѭ��
�ļ��ض���
"""
import sys
import time
from collections import deque

fancy_loading = deque('>--------------------')

while True:
    print '\r%s' % ''.join(fancy_loading),
    fancy_loading.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)