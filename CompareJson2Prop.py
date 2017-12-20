# converts Json to ":" seperated property file
# converts property file to dictionary
# compares diff dictFromUCD & dictFromXLDeploy, print relevant changes into a file.

import os
import json

def JSONtoProp(filename):
    json_data = open(filename).read()
    data = json.loads(json_data)
    n = os.path.splitext(filename)[0]
    newfile = n+'.prop'
    with open(newfile, 'w') as outfile:
        for key in data:
            outfile.write(key+":"+data[key]+"\n")
    return newfile

def load_properties(filetoCompare, sep=":", comment_char="#"):
    props = {}
    with open(filetoCompare, "rt") as f:
        l = line.strip()
        if l and not l.startswith(comment_char):
            key_value = l.split(sep)
            key = key_value[0].strip()
            value = sep.join(key_value[1].strip().strip('"'))
            props[key] = value
    return props


def GenfileForUCD(file2write, dictFromUCD, dictFromXLDeploy):
    with open(file2write, 'w') as latestfile:
        for key in dictFromUCD:
            if key in dictFromXLDeploy:
                if dictFromUCD[key] != dictFromXLDeploy[key]:
                    print "FromUrbanCode =>",key,":",dictFromUCD[key]
                    print "FromXLDeploy =>",key,":",dictFromXLDeploy[key]
                    latestfile.write(key+":"+dictFromXLDeploy[key]+"\n")
                else:
                    latestfile.write(key+":"+dictFromUCD[key]+"\n")
            else:
                latestfile.write(key+":"+dictFromUCD[key]+"\n")
        return file2write
    
FileFromXLDeploy = "someFile.json"
print "Converting JSON to prop"
fileFromXLDeploytoProp = JSONtoProp(fileFromXLDeploy)
print "Converted."

print "loading ", fileFromXLDeploytoProp,"to dictionary"
AS = load_properties(fileFromXLDeploytoProp, sep=":")


FiletoCompareFromUCD = "SomeFileFromUCD.txt"
UCD = load_properties(FiletoCompareFromUCD, sep="=")

print "Difference to be uploaded."
f = GenfileForUCD(fileFromXLDeploytoProp+'.upoad2UCD', UCD, AS)
print "This file can be directly uploaded to UCD", f