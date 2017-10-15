# Lists certain configs and parameter of websphere application server resources.

Cell = AdminControl.getCell()
scopeID = AdminConfig.getid( '/Cell:'+Cell+'/ServerCluster:TestCluster/')

def applicationDetails():
	print "Application Config Info :"
	print "*"*70
	app = 'BPCExplorer_PSSingleCluster'
	#print "\n".join(AdminApp.view('BPCExplorer_PSSingleCluster','-CtxRootForWebMod').splitlines()[-3:])
	#print "Application",AdminApp.view('BPCExplorer_PSSingleCluster', '-MapWebModToVH').splitlines()[-1]
	#print "Applicaton Mapped To",AdminApp.view('BPCExplorer_PSSingleCluster', ['-MapModulesToServers']).splitlines()[-1].replace("+","\n\t\t\t\t")
	#TaskNames = AdminApp.view( 'BPCExplorer_PSSingleCluster', '-tasknames').splitlines()
	for name in ('MapModulesToServers', 'CtxRootForWebMod', 'MapWebModToVH'):
		x = AdminApp.view( app, '-'+name ).splitlines()[-1]
		print x
	print "-"*70,"\n"
	

def JVM():
	print "JVM Args:"
	print "*"*70
	clusterID=AdminConfig.getid('/ServerCluster:PSSingleCluster/')
	clusMemlist = AdminConfig.list('ClusterMember', clusterID).splitlines()
	#print clusMemlist
	for i in clusMemlist:
		serverName = AdminConfig.showAttribute( i, 'memberName' )	
		print serverName
		jpd = AdminConfig.list("JavaProcessDef", AdminConfig.getid('/Server:' + serverName))
		jvm = AdminConfig.showAttribute(jpd, "jvmEntries")
		#print jvm[0]
		jvm = jvm.replace('[','"').replace(']','"')
		print jvm
		print "genericJvmArguments:\t\t", AdminConfig.showAttribute( '%s' % (jvm) , "genericJvmArguments")
		print "initialHeapSize:\t\t",AdminConfig.showAttribute( '%s' % (jvm) , "initialHeapSize")
		print "maximumHeapSize:\t\t",AdminConfig.showAttribute( '%s' % (jvm) , "maximumHeapSize")
		webcontainer = AdminConfig.list('WebContainer', AdminConfig.getid('/Server:' + serverName))
		vh = AdminConfig.show(webcontainer, 'defaultVirtualHostName').replace("[","").replace("]","").split()[1]
		if vh:
			print "WebContainerVirtualHost:\t",vh
	print "-"*70,"\n"	

	# list all clusters and cluster members
	#clusters = AdminConfig.list('ServerCluster', AdminConfig.getid( '/Cell:PSCell1/')).splitlines()	
	#for cluster in clusters:
	#	clusName = AdminConfig.showAttribute( cluster, 'name')
	#	clusterID=AdminConfig.getid('/ServerCluster:'+clusName+'/')
	#	clusterList=AdminConfig.list('ClusterMember', clusterID).splitlines()
	#	print clusterList
	#	print clusName,":",[ AdminConfig.showAttribute( i, 'memberName' ) for i in clusterList]
	

def getobjectCustomProperties(object):
	#AdminConfig.showAttribute('" + object +"','propertySet')
	return AdminConfig.showAttribute(object,"propertySet")

def QCF():
	WMQcfs = AdminConfig.list('MQQueueConnectionFactory', AdminConfig.getid( '/Cell:PSCell1/ServerCluster:TestCluster/')).splitlines()
	print "\nQueue Connection Factory"
	print "*"*70
	for wmqcf in WMQcfs:
		#print wmqcf
		print "QCFName:\t",AdminConfig.showAttribute( wmqcf, 'name')
		print "jndiName:\t",AdminConfig.showAttribute( wmqcf, 'jndiName')
		print "queueManager:\t",AdminConfig.showAttribute( wmqcf, 'queueManager')
		print "host:\t\t",AdminConfig.showAttribute( wmqcf, 'host')
		print "port:\t\t",AdminConfig.showAttribute( wmqcf, 'port')
		print "transportType:\t",AdminConfig.showAttribute( wmqcf, 'transportType')
		print "channel:\t",AdminConfig.showAttribute( wmqcf, 'channel')
		x = AdminConfig.showAttribute(wmqcf, "propertySet")
		#print x
		#print "QCF Name:\t" + AdminConfig.showAttribute( wmqcf, "name" )
		resProperties = AdminConfig.showAttribute('"%s"' % ( x ),'resourceProperties').split()
		if resProperties:
			print "Custom Properties : "
			for resProperty in resProperties:
				strResProperty = resProperty.replace('[','').replace(']','')
				nameResProperty = AdminConfig.showAttribute(strResProperty,"name")
				print "\t\t",nameResProperty
				#print AdminConfig.showAttribute(strResProperty,"type")
				print "\t\t",AdminConfig.showAttribute(strResProperty,"value")
				#print AdminConfig.showAttribute(strResProperty,"required")
			print "\n"
		else:
			print "No custom property found."
	print "-"*70,"\n"
	
def Queues():
	print "Queues info:"
	print "*"*70
	scopeID = AdminConfig.getid('/Cell:PSCell1/ServerCluster:TestCluster/')
	print "\nQueues Information"
	MQQueues = AdminConfig.list('MQQueue', scopeID ).splitlines()
	for queue in MQQueues:
		print "QueueName:\t\t",AdminConfig.showAttribute( queue, 'name')
		print "jndiName:\t\t",AdminConfig.showAttribute( queue, 'jndiName')
		print "baseQueueName:\t\t",AdminConfig.showAttribute( queue, 'baseQueueName')			
	print "-"*70,"\n"
	
#AdminConfig.list('JDBCProvider', AdminConfig.getid( '/Cell:PSCell1/ServerCluster:TestCluster/'))
def showDatasources():
	print "DataSource:"
	print "*"*70
	dsourcesEntries = AdminConfig.list('DataSource', AdminConfig.getid( '/Cell:PSCell1/ServerCluster:TestCluster/')).splitlines() 
	for dsource in dsourcesEntries:
		print dsource
		dsource_name = AdminConfig.showAttribute( dsource, 'name')
		#print "DataSourceName:\t\t",dsource_name
		print "JDBC Provider:\t\t", AdminConfig.showAttribute( dsource, 'name')
		print "JNDI:\t\t\t",AdminConfig.showAttribute(  dsource, 'jndiName' )
		print "DSHelperClass:\t\t",AdminConfig.showAttribute(  dsource, 'datasourceHelperClassname' )
		#print AdminConfig.showAttribute(  dsource, 'authDataAlias')
		dsource_name = AdminConfig.showAttribute( dsource, 'name')
		J2EEPropSet = AdminConfig.showAttribute( dsource, 'propertySet' )
		propList = AdminConfig.list('J2EEResourceProperty', J2EEPropSet).splitlines()
		for prop in propList: 
			if AdminConfig.showAttribute( prop, 'name') == 'URL':
				print "URL:\t\t\t", AdminConfig.showAttribute(prop, 'value')
		print "Connection Pool Parameters :"
		pool = AdminConfig.showAttribute(dsource,'connectionPool')
		oldMin = AdminConfig.showAttribute( pool , 'minConnections' )
		oldMax = AdminConfig.showAttribute( pool , 'maxConnections' )
		#print dsource_name
		print "Maximum Connections:\t", oldMax
		print "Minimum Connections:\t", oldMin
		print "\n"
	print "-"*70,"\n"

def showJdbcProviders():
	print "JDBC Provider info:"
	print "*"*70
	providerEntries = AdminConfig.list('JDBCProvider', AdminConfig.getid( '/Cell:PSCell1/ServerCluster:TestCluster/')).splitlines()
	for provider in providerEntries:
		providerName = AdminConfig.showAttribute( provider, "name" )
		providerDescription = AdminConfig.showAttribute( provider, "description" )
		providerClasspath = AdminConfig.showAttribute( provider, "classpath" )
		providerImplementationClassName = AdminConfig.showAttribute( provider, "implementationClassName" )
		print "JDBCProvider Name:\t" + providerName
		print "Description: \t\t" + providerDescription
		print "Classpath: \t\t" + providerClasspath
		print "Class Name: \t\t" + providerImplementationClassName
		print  "\n"
	print "-"*70,"\n"
	
def WorkManager():
		print "WorkManager info :"
		print "*"*70
		WorkMgrs = AdminConfig.list('WorkManagerInfo', AdminConfig.getid( '/Cell:PSCell1/ServerCluster:TestCluster/')).splitlines()
		#print WorkMgrs
		for wm in WorkMgrs:
			match = AdminConfig.showAttribute(wm, 'name')
			if match  not in  ['DefaultWorkManager', 'AsyncRequestDispatcherWorkManager']:
				#print match
				print "WorkManagerName:\t\t",AdminConfig.showAttribute(wm, 'name')
				print "jndiName:\t\t\t",AdminConfig.showAttribute(wm, 'jndiName')
				print "workReqQFullAction:\t\t",AdminConfig.showAttribute(wm, 'workReqQFullAction')
				
		print "-"*70,"\n"
	
applicationDetails()
WorkManager()		
Queues()
QCF()
JVM()
showDatasources()
showJdbcProviders()