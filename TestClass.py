'''
Created on Oct 24, 2019

@author: stsm
'''

class TestClass(object):
    '''
    classdocs
    '''
    testOk = 0
    testFailed = 0
    

    def __init__(self):
        '''
        Constructor
        '''
        
    @staticmethod
    def countTestOk():
        TestClass.testOk += 1
        
    @staticmethod   
    def getTestOk():
        return TestClass.testOk
    
    @staticmethod 
    def countTestFailed():
        TestClass.testFailed +=1
        
    @staticmethod 
    def getTestFailed():
        return TestClass.testFailed
        
        