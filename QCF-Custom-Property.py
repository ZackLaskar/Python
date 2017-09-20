
# Script add Custom property to QCF
# PropertySet creation of J2EEResource if it a new one
# else use the already created propertySet and create custom property.


# Create new QCF
#AdminTask.createWMQConnectionFactory('"WebSphere MQ JMS Provider(cells/PSCell1/clusters/TestCluster|resources.xml#builtin_mqprovider)"', '[-type QCF -name testQCF133 -jndiName /jm/testQcf123 -description -qmgrName QMGR1 -wmqTransportType BINDINGS_THEN_CLIENT -qmgrSvrconnChannel -qmgrHostname QMGRhostname -qmgrPortNumber 1414 ]') 
#AdminConfig.save()
#AdminNodeManagement.syncActiveNodes()
#CellName='PSCell1'
customProperty = 'testcus1323'
customPropertyValue = 'testcus23val13'
WMQcfs = AdminConfig.list('MQQueueConnectionFactory').splitlines()
for wmqcf in WMQcfs:
       # if wmqcf.find('testQCF13') >= 0:
	 if re.search( testQCF13$, wmqcf): # make sure you find the exact match of the qcf name
				#print wmqcf
				propSet = AdminConfig.showAttribute( wmqcf, 'propertySet' )
				print "propSet :", propSet
				if propSet == None:
					newPropSet = AdminConfig.create('J2EEResourcePropertySet',wmqcf,[])
					propSet = AdminConfig.showAttribute(wmqcf, 'propertySet')
					#AdminConfig.save()
					AdminConfig.create('J2EEResourceProperty',propSet, '[[name "%s"] [type "java.lang.String"] [description ""] [value "%s"] [required "false"]]' % (customProperty, customPropertyValue))
					AdminConfig.save()
					AdminNodeManagement.syncActiveNodes()
				else:
					print "propSet :", propSet
					AdminConfig.create('J2EEResourceProperty',AdminConfig.showAttribute( wmqcf, 'propertySet' ), '[[name "%s"] [type "java.lang.String"] [description ""] [value "%s"] [required "false"]]' % (customProperty, customPropertyValue))
					AdminConfig.save()
					AdminNodeManagement.syncActiveNodes()
