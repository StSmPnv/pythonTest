'''
Created on Oct 24, 2019

@author: stsm
'''
from fsTestClass.TestClass import TestClass

class test1a(TestClass):
    def dotest(self):
        TestClass.countTestOk()
        print(TestClass.getTestOk())
        TestClass.countTestOk()
        print(TestClass.getTestOk())
    
    
if __name__ == '__main__':
    pass