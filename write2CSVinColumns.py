#---------------------------------------------------------------------------------------------------------------------------------------#
# Checks files in a directory and segregates filenames based on their extension and prints them in csv file under respective extn name. #
#---------------------------------------------------------------------------------------------------------------------------------------#

import os, csv, sys

Extensionlist = []
uniquelist = []
def extenstionreader(path):
    os.chdir(path)
    for files in os.listdir(os.getcwd()):
        ext = os.path.splitext(files)
        Extensionlist.append(ext[-1])
        for i in Extensionlist:  # this loops is to create a unique list of extensions.
            if i not in uniquelist:
                uniquelist.append(i)
    return uniquelist


extenstionreader("/Users/Muzakkir/Downloads")
testdic= {}
for files in os.listdir("/Users/Muzakkir/Downloads"):
    for extn in uniquelist:
        if extn in os.path.splitext(files):
            testdic.setdefault(extn, []).append(files)

# finding the key which has highest number of values assigned to it.
maxLenOfKeyValueFromtestdic = max([len(testdic[i]) for i in testdic.keys()])

#Now adding null value to all the other keys which have less number of values assigned to them then max valued key.
#making the length of values same for the dict keys so that we can use the zip function below
for j in testdic.keys():
    while len(testdic[j]) != maxLenOfKeyValueFromtestdic:
        testdic[j].append(None)     #appending None values to keys whose number of values are not same as max valued key

with open('/users/Muzakkir/PycharmProjects/LearningPy/samples/usage.csv', 'wb') as csvfileread:
    writer = csv.writer(csvfileread, delimiter = ",")
    writer.writerow(sorted(testdic.keys()))
    writer.writerows(zip(*[testdic[key] for key in sorted(testdic.keys())])) #with writerows you can pass multiple values
    #for items in zip(*[testdic[key] for key in sorted(testdic.keys())]):    #the above writerows can be written using a loop on sequence
    #    writer.writerow(items)                                              # and iterating over writer.writerow(items)
