#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys

path = ''''''
dirs = os.listdir( path )

# 输出所有文件和文件夹
for file in dirs:
	with open(path+'\\'+file, "a") as f:
		f.write('\n\n')
		print("adll new line ",file)
