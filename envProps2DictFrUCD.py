
env="hello=world,ucdIncludeExtension=.xml,.prop,.cfg,key=value1,key2=value2,jvmARgs=-Dservelog=$(server_log_root),Heapmin=48,heapmax=100,ucdExcludeExtn=.xls,.xsd,.xls"

y = env.split(",")
x = [i for i in y if "=" not in i]
for i in x:
    y[y.index(i) - 1:y.index(i) + 1] = [','.join(y[y.index(i) - 1:y.index(i) + 1])]

DictP = {}
for i in y:
    DictP[i.split("=", 1)[0]] = i.split("=", 1)[1]




