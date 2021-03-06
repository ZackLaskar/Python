# Wrote this code to read a custom property file into a dictionary.
# Python implementation for IBM WAS ( i.e, Jython ) does not have that cool configParser module as Python to read/parse a properties file.
# This code reads values of a particular section in the properties file into a dictionary.
# Usage: PropFileReader function should be passed the following arguments - 1. The property file,  2. the section to be read from it.
# 	 Eg: Refer Test2Dict.properties for example of the property file to be used for this code.


file = "/Users/Muzakkir/forJython/Test2Dict.properties"

def PropFileReader(file, value):
    f = open(file)
    content = f.readlines()
    content = [i.rstrip() for i in content]
    list1 = [content[item] for item in range(content.index("[" + value + "_Start]") + 1, content.index("[" + value + "_End]"))]
    fieldnames = list1[0].split(",")
    list2 = [i.split(",") for i in list1[1:]]
    mydict = {}
    for item in list2:
        for k, v in zip(fieldnames, item):
            mydict.setdefault(k,[]).append(v)
    return mydict

#mydict = PropFileReader(file, 'ConnectionFactories')

def creat_CF():
    mydict = PropFileReader(file, 'ConnectionFactories')   #passing the "ConnectionFactories" section to be read by the PropFileReader function.
    print mydict['url'][2]
    print mydict['name'][2]
    print mydict['jndiname'][2]
    #print mydict
    #print type(mydict['name'])
    #for key, value in mydict.items():
     #   print key, value

creat_CF()
