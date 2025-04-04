# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long, too-many-statements, super-with-arguments

VnetConfiguration = {
    "infrastructureSubnetId": None,
    "dockerBridgeCidr": None,
    "platformReservedCidr": None,
    "platformReservedDnsIP": None
}

ManagedEnvironment = {
    "location": None,
    "tags": None,
    "properties": {
        "daprAIInstrumentationKey": None,
        "vnetConfiguration": None,  # VnetConfiguration
        "appLogsConfiguration": None,
        "customDomainConfiguration": None,  # CustomDomainConfiguration,
        "workloadProfiles": None,
        "infrastructureResourceGroup": None,
        "openTelemetryConfiguration": None
    }
}

CustomDomainConfiguration = {
    "dnsSuffix": None,
    "certificateValue": None,
    "certificatePassword": None,
    "certificateKeyVaultProperties": None
}

AppLogsConfiguration = {
    "destination": None,
    "logAnalyticsConfiguration": None
}

LogAnalyticsConfiguration = {
    "customerId": None,
    "sharedKey": None
}

# Containerapp

Dapr = {
    "enabled": False,
    "appId": None,
    "appProtocol": None,
    "appPort": None,
    "httpReadBufferSize": None,
    "httpMaxRequestSize": None,
    "logLevel": None,
    "enableApiLogging": None
}

EnvironmentVar = {
    "name": None,
    "value": None,
    "secretRef": None
}

ContainerResources = {
    "cpu": None,
    "memory": None
}

VolumeMount = {
    "volumeName": None,
    "mountPath": None,
    "subPath": None
}

Container = {
    "image": None,
    "name": None,
    "command": None,
    "args": None,
    "env": None,  # [EnvironmentVar]
    "resources": None,  # ContainerResources
    "volumeMounts": None,  # [VolumeMount]
}

SecretVolumeItem = {
    "secretRef": None,
    "path": None,
}

Volume = {
    "name": None,
    "storageType": "EmptyDir",  # AzureFile, EmptyDir, Secret or NfsAzureFile
    "storageName": None,   # None for EmptyDir or Secret, otherwise name of storage resource
    "secrets": None,  # [SecretVolumeItem]
    "mountOptions": None,
}

ScaleRuleAuth = {
    "secretRef": None,
    "triggerParameter": None
}

QueueScaleRule = {
    "queueName": None,
    "queueLength": None,
    "auth": None  # ScaleRuleAuth
}

CustomScaleRule = {
    "type": None,
    "metadata": {},
    "auth": None  # ScaleRuleAuth
}

HttpScaleRule = {
    "metadata": {},
    "auth": None  # ScaleRuleAuth
}

ScaleRule = {
    "name": None,
    "azureQueue": None,  # QueueScaleRule
    "custom": None,  # CustomScaleRule
    "http": None,  # HttpScaleRule
}

Secret = {
    "name": None,
    "value": None,
    "keyVaultUrl": None,
    "identity": None
}

Scale = {
    "minReplicas": None,
    "maxReplicas": None,
    "rules": []  # list of ScaleRule
}

ServiceBinding = {
    "serviceId": None,
    "name": None
}

JobScale = {
    "minExecutions": None,
    "maxExecutions": None,
    "pollingInterval": None,
    "rules": []  # list of ScaleRule
}

TrafficWeight = {
    "revisionName": None,
    "weight": None,
    "latestRevision": False
}

BindingType = {

}

CustomDomain = {
    "name": None,
    "bindingType": None,  # BindingType
    "certificateId": None
}

Ingress = {
    "fqdn": None,
    "external": False,
    "targetPort": None,
    "transport": None,  # 'auto', 'http', 'http2', 'tcp'
    "exposedPort": None,
    "allowInsecure": False,
    "traffic": None,  # TrafficWeight
    "customDomains": None,  # [CustomDomain]
    "ipSecurityRestrictions": None,  # [IPSecurityRestrictions]
    "stickySessions": None  # StickySessions
}

RegistryCredentials = {
    "server": None,
    "username": None,
    "passwordSecretRef": None
}

Template = {
    "revisionSuffix": None,
    "containers": None,  # [Container]
    "initContainers": None,  # [Container]
    "scale": Scale,
    "volumes": None,  # [Volume]
    "serviceBinds": None  # [ServiceBinding]
}

Configuration = {
    "secrets": None,  # [Secret]
    "activeRevisionsMode": None,  # 'multiple' or 'single'
    "ingress": None,  # Ingress
    "dapr": Dapr,
    "registries": None  # [RegistryCredentials]
}

JobTemplate = {
    "containers": None,  # [Container]
    "initContainers": None,  # [Container]
    "volumes": None  # [Volume]
}

# Added template for starting job executions
JobExecutionTemplate = {
    "containers": None,  # [Container]
    "initContainers": None  # [Container]
}

JobConfiguration = {
    "secrets": None,  # [Secret]
    "triggerType": None,  # 'manual' or 'schedule' or 'event'
    "replicaTimeout": None,
    "replicaRetryLimit": None,
    "manualTriggerConfig": None,  # ManualTriggerConfig
    "scheduleTriggerConfig": None,  # ScheduleTriggerConfig
    "eventTriggerConfig": None,  # EventTriggerConfig
    "registries": None,  # [RegistryCredentials]
    "dapr": None
}

ManualTriggerConfig = {
    "replicaCompletionCount": None,
    "parallelism": None
}

ScheduleTriggerConfig = {
    "replicaCompletionCount": None,
    "parallelism": None,
    "cronExpression": None
}

EventTriggerConfig = {
    "replicaCompletionCount": None,
    "parallelism": None,
    "scale": None,  # [JobScale]
}

UserAssignedIdentity = {

}

ManagedServiceIdentity = {
    "type": None,  # 'None', 'SystemAssigned', 'UserAssigned', 'SystemAssigned,UserAssigned'
    "userAssignedIdentities": None  # {string: UserAssignedIdentity}
}

ServiceConnector = {
    "properties": {
        "targetService": {
            "id": None,
            "type": "AzureResource"
        },
        "authInfo": {
            "authType": None,
        },
        "scope": None,
    }
}

Service = {
    "type": None
}

ContainerApp = {
    "location": None,
    "identity": None,  # ManagedServiceIdentity
    "properties": {
        "environmentId": None,
        "configuration": None,  # Configuration
        "template": None,  # Template
        "workloadProfileName": None
    },
    "tags": None,
    "kind": None
}

ContainerAppsJob = {
    "location": None,
    "identity": None,  # ManagedServiceIdentity
    "properties": {
        "environmentId": None,
        "configuration": None,  # JobConfiguration
        "template": None,  # JobTemplate
        "workloadProfileName": None
    },
    "tags": None
}

MaintenanceConfiguration = {
    "name": "default",
    "properties": {
        "scheduledEntries": [
            {
                "weekDay": None,
                "startHourUtc": None,
                "durationHours": None
            }
        ]
    }
}

SessionPool = {
    "location": None,
    "properties": {
        "environmentId": None,
        "poolManagementType": None,
        "containerType": None,
        "customContainerTemplate": None,
        "secrets": None,
        "dynamicPoolConfiguration": None,
        "scaleConfiguration": None,
        "sessionNetworkConfiguration": None
    }
}

SessionCodeInterpreterExecution = {
    "codeInputType": None,
    "executionType": None,
    "code": None,
    "timeoutInSeconds": None
}

DaprComponentResiliency = {
    "properties": {
        "inboundPolicy": {
            "timeoutPolicy": {
                "responseTimeoutInSeconds": None,
            },
            "httpRetryPolicy": {
                "maxRetries": None,
                "retryBackOff": {
                    "initialDelayInMilliseconds": None,
                    "maxIntervalInMilliseconds": None,
                }
            },
            "circuitBreakerPolicy": {
                "consecutiveErrors": None,
                "timeoutInSeconds": None,
                "intervalInSeconds": None
            }
        },
        "outboundPolicy": {
            "timeoutPolicy": {
                "responseTimeoutInSeconds": None,
            },
            "httpRetryPolicy": {
                "maxRetries": None,
                "retryBackOff": {
                    "initialDelayInMilliseconds": None,
                    "maxIntervalInMilliseconds": None,
                }
            },
            "circuitBreakerPolicy": {
                "consecutiveErrors": None,
                "timeoutInSeconds": None,
                "intervalInSeconds": None
            }
        }
    }
}

ContainerAppsResiliency = {
    "properties": {
        "timeoutPolicy": None,
        "httpRetryPolicy": None,
        "tcpRetryPolicy": None,
        "circuitBreakerPolicy": None,
        "tcpConnectionPool": None,
        "httpConnectionPool": None
    }
}

HttpRetryPolicy = {
    "maxRetries": None,
    "retryBackOff": {
        "initialDelayInMilliseconds": None,
        "maxIntervalInMilliseconds": None,
    },
    "matches": {
        "headers": None,
        "httpStatusCodes": None,
        "errors": None
    }
}

TcpConnectionPool = {
    "maxConnections": None
}

TimeoutPolicy = {
    "responseTimeoutInSeconds": None,
    "connectionTimeoutInSeconds": None
}

TcpRetryPolicy = {
    "maxConnectAttempts": None
}

CircuitBreakerPolicy = {
    "consecutiveErrors": None,
    "intervalInSeconds": None,
    "maxEjectionPercent": None
}

HttpConnectionPool = {
    "http1MaxPendingRequests": None,
    "http2MaxRequests": None
}

ContainerAppCertificateEnvelope = {
    "location": None,
    "properties": {
        "password": None,
        "value": None,
        "certificateKeyVaultProperties": None
    }
}

DaprComponent = {
    "properties": {
        "componentType": None,  # str
        "ignoreErrors": None,  # str
        "initTimeout": None,  # str
        "metadata": None,  # [DaprMetadata]
        "scopes": None,  # [str]
        "secrets": None,  # [Secret]
        "secretStoreComponent": None,  # str
        "serviceComponentBind": None,  # DaprServiceComponentBinding
        "version": None,  # str
    }
}

DaprServiceComponentBinding = {
    "name": None,  # str
    "serviceId": None,  # str
    "metadata": None,  # Dict[str, str]
}

DaprMetadata = {
    "name": None,  # str
    "value": None,  # str
    "secretRef": None  # str
}

SourceControl = {
    "properties": {
        "repoUrl": None,
        "branch": None,
        "githubActionConfiguration": None  # [GitHubActionConfiguration]
    }

}

GitHubActionConfiguration = {
    "registryInfo": None,  # [RegistryInfo]
    "azureCredentials": None,  # [AzureCredentials]
    "image": None,  # str
    "contextPath": None,  # str
    "publishType": None,  # str
    "os": None,  # str
    "runtimeStack": None,  # str
    "runtimeVersion": None,  # str
    "buildEnvironmentVariables": None  # [EnvironmentVar]
}

RegistryInfo = {
    "registryUrl": None,  # str
    "registryUserName": None,  # str
    "registryPassword": None  # str
}

AzureCredentials = {
    "clientId": None,  # str
    "clientSecret": None,  # str
    "tenantId": None,  # str
    "subscriptionId": None  # str
}

ContainerAppCustomDomainEnvelope = {
    "properties": {
        "configuration": {
            "ingress": {
                "customDomains": None
            }
        }
    }
}

ContainerAppCustomDomain = {
    "name": None,
    "bindingType": "SniEnabled",
    "certificateId": None
}

ManagedEnvironmentStorageProperties = {
    "location": None,
    "properties": {
        "azureFile": None,
        "nfsAzureFile": None,
    }
}

AzureFileProperties = {
    "accountName": None,
    "accountKey": None,
    "accessMode": None,
    "shareName": None
}

NfsAzureFileProperties = {
    "server": None,
    "accessMode": None,
    "shareName": None
}

ManagedCertificateEnvelop = {
    "location": None,  # str
    "properties": {
        "subjectName": None,  # str
        "validationMethod": None  # str
    }
}

# ContainerApp Patch
ImageProperties = {
    "imageName": None,
    "targetContainerName": None,
    "targetContainerAppName": None,
    "revisionMode": None,
}

ImagePatchableCheck = {
    "targetContainerAppName": None,
    "targetContainerName": None,
    "revisionMode": None,
    "targetImageName": None,
    "oldRunImage": None,
    "newRunImage": None,
    "id": None,
    "reason": None,
}

OryxRunImageTagProperty = {
    "fullTag": None,
    "framework": None,
    "version": None,
    "os": None,
    "architectures": None,
    "support": None,
}


# model for preview extension
ConnectedEnvironment = {
    "extendedLocation": None,
    "tags": None,
    "location": None,
    "properties": {
        "staticIp": None,
        "daprAIConnectionString": None
    }
}

ExtendedLocation = {
    "name": None,
    "type": None
}

AppInsightsConfiguration = {
    "connectionString": None
}

OpenTelemetryConfiguration = {
    "destinationsConfiguration": None,
    "tracesConfiguration": None,
    "logsConfiguration": None,
    "metricsConfiguration": None
}

DestinationsConfiguration = {
    "dataDogConfiguration": None
}

DataDogConfiguration = {
    "site": None,
    "key": None
}

TracesConfiguration = {
    "destinations": []
}

LogsConfiguration = {
    "destinations": []
}

MetricsConfiguration = {
    "destinations": []
}

JavaComponent = {
    "properties": {
        "componentType": None,
        "serviceBinds": None
    }
}

RuntimeJava = {
    "enableMetrics": True,
    "javaAgent": {
        "enabled": False,
        "logging": {}
    }
}

DotNetComponent = {
    "properties": {
        "componentType": "AspireDashboard"
    }
}

JavaLoggerSetting = {
    "logger": None,
    "level": None
}
