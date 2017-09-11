AdminApp.edit('BPCExplorer_PSSingleCluster', [' -MapWebModToVH', [[ '.*', '.*', 'default_host' ]]])

AdminConfig.save()

AdminNodeManagement.syncActiveNodes()
