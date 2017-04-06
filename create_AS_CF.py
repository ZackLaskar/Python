'''
Wrote this to automate some JMS resource creation in WAS using a csv file
NOTE : full wsadmin commands are not updated in this script.
'''

import os, sys

cellId = AdminControl.getCell()

def create_AS(file):
    ASlist = csvreader(file)
    for items in range(len(ASlist)):
            AS = [i.rstrip() for i in ASlist[items]]
            print("Do stuff by calling : "+AS[0]+" Node: "+AS[0])
            AdminTask.createWMQActivationSpec('...')
            AdminConfig.save()
            print "Successfull"
    syncNodes()
    
def create_CF(file):
    CFlist = csvreader(file)
    for items in range(len(CFlist)):
        CF = [i.rstrip() for i in CFlist[items]]
        print("Do stuff by passing items in the list CF "+CF[1]+"Node :"+CF[0])
        ConFact = AdminTask.createWMQConnectionFactory('....')
        pool = AdminConfig.showAttribute(ConFact, 'connectionPool')
        AdminConfig.modify(pool, [['reapTime', 180],['agedTimeout', 360]])
        AdminConfig.save()
        print "Successfull"
    syncNodes()
    
def syncNodes():
    AdminNodeManagement.syncActiveNodes()

def csvreader(file):
    line = file.readline().strip()
    lines = file.readlines()
    list1 = []
    for i in range(len(lines)):
        list1.append(lines[i].split","))
    return list1

ASfile = open("/tmp/ActivationSpecfication.csv")
CFfile = open("/tmp/ConnectionFactory.csv")


create_AS(ASfile)
create_CF(CFfile)
