#!/usr/bin/python3
# -*- coding: utf-8 -*-
import threading,datetime
class threadClass(threading.Thread):
    def run(self):
        now = datetime.datetime.now()
        print ("%s says Hello World at time: %s" %(self.getName(), now))

for i in range(3):
    t = threadClass()
    t.start()