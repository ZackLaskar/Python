import os
import hashlib
import tempfile
import shutil


list = os.popen('svn list http://Jazz/svn/TestApp/')
for i in list.readlines():
    print i.strip()

dirpath = tempfile.mkdtemp()
print ("dirpath :", dirpath)
os.chdir(dirpath)
print ("Current working dir :", os.getcwd())
print ("Checking out TestApp")
os.popen('svn checkout http://Jazz/svn/TestApp/')
os.popen('svn cleanup dirpath')
print ("content of this dir.")
print (os.listdir(dirpath))
print ("Removing temp dir ")
os.chdir('..')
print ("Current working dir :", os.getcwd())

#shutil.rmtree(dirpath)
	
	
def generate_MD5(filename):
    hasher = hashlib.md5()
    with open(filename, 'rb') as open_file:
        content = open_file.read()
        hasher.update(content)
    print (hasher.hexdigest())


generate_MD5(r'Z:\SVNRepositories\TEST\branches\Integration\README.md')
