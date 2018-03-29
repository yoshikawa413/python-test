# -*- coding:utf-8 -*-
import os

fifo = 'hoge1'

os.mkfifo(fifo)
while 1:
  with open(fifo) as f:
    a = f.read()
    print a
