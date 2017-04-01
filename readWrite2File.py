#-----------------------------------------------------------------------# 
# Zack: Python I/O documentation :       			        #
# Notes : 1) Basic read write operations  				#
#	  2) Using context manager        				#
#-----------------------------------------------------------------------#

'''Open and read a file :

file = open('/users/zach/test/test.txt','r')
print file.name     #Prints the name of the file object.
print file.mode     # f.mode tells file is open in which mode(read, write..)
print file.read()   # reads the content of the file assigned to the file object file
print file.closed   #checks if the file object is closed or not.
file.close()        #closes the file object.
print file.closed   #using f.closed again to check if the file is closed.
'''

''' BEST PRACTICE : use a context manager for reading writing a file. Advantages of using context manager:
                    > this allow us to work with file within a block of code and once you are out of that block
                      the file automatically is closed.
'''
with open('/users/zach/test/test.txt', 'r') as file:
    #for x in file:   #using a loop to read all the lines of this file object.
    #    print x

    f = file.readline() #reading lines without loop.
    print f
    #file.seek(0) #Takes the cursor back to the first line of the file.
    #f = file.readline()
    #print f
    #file.close()
    #print file.closed

with open('/users/zach/test/test2.txt','w') as x:
    x.write('Hello, there\n')
    x.write('second line\n')
    x.write('third line\n')

''' reading and writing into files simoultaenously '''
with open('/users/muzakkir/test/test.txt','r') as rf:
    with open('/users/muzakkir/test/test3.txt','w') as wf:
        for line in rf:
            wf.write(line)

'''Copying files other then texts like jpg's..'''
with open('/Users/zach/Pictures/eurotrip/dslr/22DSC_017.jpg','rb') as rf:
    with open('/users/muzakkir/Desktop/test.jpg','wb') as wf:
        for line in rf:
            wf.write(line)

