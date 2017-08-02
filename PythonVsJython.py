# In jython, syntax - if "string" in ds: does not work throws below error probably beacuse WAS has a very old python implementation for jython.
# TypeError: string member test needs char left operand
# Here are example of two different codes doing the same thing only thing is the first one does not work in jython

#Works in Python not in jython.

DS = ['"BPM Business Process Choreographer data source(cells/PSCell1/clusters/PSSingleCluster|resources.xml#DataSource_1479002431909)"\r','"IBM Business Space data source(cells/PSCell1/clusters/PSSingleCluster|resources.xml#DataSource_1479002429850)"\r']
x="Choreographer"
for ds in DS:
    if x in ds:
        print ds


# Used the below alternative code in jython.

DS = ['"BPM Business Process Choreographer data source(cells/PSCell1/clusters/PSSingleCluster|resources.xml#DataSource_1479002431909)"\r','"IBM Business Space data source(cells/PSCell1/clusters/PSSingleCluster|resources.xml#DataSource_1479002429850)"\r']
x="Choreographer"
for ds in DS:
    if ds.find(x) >= 0:
        #print ds.find(x)
        print ds
