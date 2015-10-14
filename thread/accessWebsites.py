#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request,time
hosts = ["http://yahoo.com", "http://google.com", "http://amazon.com","http://ibm.com", "http://apple.com"]
startTime = time.time()
for host in hosts:
    response = urllib.request.urlopen(host)
    print(response.read(1024))

print('elapsed time:%s' % (time.time()-startTime))