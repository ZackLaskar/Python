# jython to get WAS application status.

apps = AdminApp.list().split("\n")

def appStatus(appname):
    val = AdminControl.completeObjectName('type=Application,name='+appname+',*')
    if val != "":
        print "\trunning    -|->",  appname
    else:
        print "\t{stopped}  -|->",  appname
        
def AppStatusPrint():
    print "\n"
    print "\t Status    |\tApplication"
    print "\t-----------|-----------------------"
    for ap in apps:
        appStatus(ap)
    print "\n"

AppStatusPrint()

