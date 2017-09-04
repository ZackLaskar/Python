
customProperty = 'testcus1'
customPropertyValue = 'testcusval1'
WMQcfs = AdminConfig.list('MQQueueConnectionFactory').splitlines()

for wmqcf in WMQcfs:
        if wmqcf.find('testQCF') >= 0:
                #print AdminConfig.showAttribute( wmqcf, 'propertySet' )
				AdminConfig.create('J2EEResourceProperty',AdminConfig.showAttribute( wmqcf, 'propertySet' ), '[[name "%s"] [type "java.lang.String"] [description ""] [value "%s"] [required "false"]]' % (customProperty, customPropertyValue))
				AdminConfig.save()
				AdminNodeManagement.syncActiveNodes()

				
# WorkManager wsadmin
NodeName='Node1'
CellName='PSCell1'
serverName='TestCluster-Member1'
wmname="test2"
wmworkReqQFullAction='0'
wmminThreads='0'
wmnumAlarmThreads='2'
wmworkReqQSize='0'
wmmaxThreads='2'
wmisGrowable='true'
wmthreadPriority='5'
wmworkTimeout='0'
wmjndiName='/jndi/testco1'

AdminConfig.create('WorkManagerInfo', AdminConfig.getid('/Cell:%s/Node:%s/Server:%s/WorkManagerProvider:WorkManagerProvider/'% (CellName, NodeName, serverName)), '[[name "'+wmname+'"] [workReqQFullAction "'+wmworkReqQFullAction+'"] [minThreads "'+wmminThreads+'"] [category ""] [defTranClass ""] [daemonTranClass ""] [numAlarmThreads "'+wmnumAlarmThreads+'"] [workReqQSize "'+wmworkReqQSize+'"] [jndiName "'+wmjndiName+'"] [maxThreads "'+wmmaxThreads+'"] [serviceNames ""] [isGrowable "'+wmisGrowable+'"] [threadPriority "'+wmthreadPriority+'"] [description ""] [workTimeout "'+wmworkTimeout+'"]]')
 
AdminConfig.save()
AdminNodeManagement.syncActiveNodes()
