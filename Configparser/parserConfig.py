#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys,os,ConfigParser

#OOP
class Config:
    def __init__(self,path):
        self.path = path
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(self.path)

    def get(self,field,key):
        result = ""
        try:
            result = self.cf.get(field,key)
        except:
            result = ""
        return result

    def set(self,field,key,value):
        try:
            self.cf.set(field,key,value)
            cf.write(open(self.path),'w')
        except:
            return False
        return True


#functional
def readConfig(configFilePath,field,key):
    cf = ConfigParser.ConfigParser()
    try:
        cf.read(configFilePath)
        result = cf.get(field,key)
    except:
        sys.exit(1)
    return result

def writeConfig(configFilePath,field,key,value):
    cf = ConfigParser.ConfigParser()
    try:
        cf.read(configFilePath)
        cf.set(field,key,value)
        cf.write(open(configFilePath,'w'))
    except:
        sys.exit(1)
    return True


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(1)

    configFilePath = sys.argv[1]
    field = sys.argv[2]
    key = sys.argv[3]
    if len(sys.argv) == 4:
        print(readConfig(configFilePath,field,key))
    else:
        value = sys.argv[4]
        writeConfig(configFilePath,field,key,value)
