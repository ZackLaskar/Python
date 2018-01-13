import os, sys, re
globalcount = 0
placeholderFoundinDict = []
placeholderFoundinnotFoundDict = []
fileSearched = []

Dict = {"{{hello}}":"world",
"{{23a}}":"42s",
"{{drwxr-xr-a}}":"permission",
"{{pwd}}":"presetWorkginDir",
"{{forJython}}":"yesForJython",
"{{Muzakki}}":"Laskar",
"{{Muz}}":"Las",
"{{readerXml1}}":"xmlfile",
"{{UserName_from_JSON}}":"jassUser",
"{{Password_from_JSON}}":"jassPassword"}

def validFile(pathname, *fileExtension):
    if os.path.splitext(pathname)[1] in fileExtension:
        return True
    return False

def RecursiveFileSearch(top, tokenReplacer):
    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        if os.path.isdir(pathname) == 1:
            # It's a directory, recurse into it
            RecursiveFileSearch(pathname, tokenReplacer)
        elif os.path.isfile(pathname) == 1 and os.path.splitext(f)[1] in sys.argv :
            # It's a file, call the tokenReplacer function
            fileSearched.append(f)
            tokenReplacer(pathname, Dict)
        else:
            # Unknown file type
            print ('Skipping %s' % pathname)
    return (placeholderFoundinDict, placeholderFoundinnotFoundDict, globalcount, fileSearched)

def tokenReplacer(file, Dict):
    print 'Looking into', file, ". Searching placeholders."
    global globalcount
    countPlaceholderfound = 0
    countPlaceholdernotfound = 0
    my_file = open(file, 'r')
    lines = my_file.readlines()
    for line in lines:
        index = lines.index(line)
        if re.search('{{.*}}', line):
            match = re.search('{{.*}}', line).group(0)
            if match:
                globalcount += 1
                if len(match.split("}}")) < 3:
                    if match in Dict:
                        print "Found =>",match, ". Replacing with =>", Dict[match]
                        lines[index] = line.replace(match, Dict[match])
                        placeholderFoundinDict.append(match)
                        countPlaceholderfound += 1
                    else:
                        print "No key in Dictionary for", match
                        placeholderFoundinnotFoundDict.append(match)
                        countPlaceholdernotfound += 1
                if len(match.split("}}")) > 2:
                    z = line
                    for x in match.split("}}"):
                        m = re.search('{{.*', x)
                        globalcount += 1
                        if m:
                            n = m.group(0) + '}}'
                            if n in Dict:
                                print "Found match", n, "Replacing with ", Dict[n]
                                z = z.replace(n, Dict[n])
                                placeholderFoundinDict.append(n)
                                countPlaceholderfound += 1
                            else:
                                print "No key in Dictionary for", n
                                placeholderFoundinnotFoundDict.append(n)
                                countPlaceholdernotfound += 1
                    lines[index] = z
    #print lines
    my_file.close()
    if countPlaceholderfound:
        my_file = open(file,'w')
        my_file.writelines(lines)
        print ("\n")
        my_file.close()
    if placeholderFoundinDict:
        print "Total placeholders found and replaced ", len(placeholderFoundinDict)
        print placeholderFoundinDict
    if placeholderFoundinnotFoundDict:
        print "Total placeholders not replaced. (placeholder key not found in Dict)", len(placeholderFoundinnotFoundDict)
        print placeholderFoundinnotFoundDict
    if not placeholderFoundinDict and placeholderFoundinnotFoundDict:
        print "No placeholder found in any file."
    return (placeholderFoundinDict, placeholderFoundinnotFoundDict, globalcount)

if __name__ == '__main__':
    #fileExtension = ('.xml','.prop')
    srcDir = "/Users/home/PycharmProjects/LearningPy/forJython/Xmls"
    print "Only file with following extn with be searched ", sys.argv
    (placeholderFoundinDict, placeholderFoundinnotFoundDict, globalcount, fileSearched) = RecursiveFileSearch(srcDir, tokenReplacer)
    print "SUMMARY:"
    print "File Searched :", fileSearched
    print "Placeholder found in dict and replaced in files :", placeholderFoundinDict
    print "Placeholder not found in dict and not replace in any files:", placeholderFoundinnotFoundDict
