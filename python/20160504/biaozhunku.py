#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: biaozhunku.py
#time: 5/5/16 12:35 AM

import os
print os.getcwd()
os.system('mkdir today')
if os.path.isdir('today'):
    os.removedirs('today')