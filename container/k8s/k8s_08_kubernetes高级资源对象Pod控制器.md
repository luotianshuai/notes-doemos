[TOC]

# Replicset

## Replicset运行原理

* Replicset通过选择器来识别它创建的Pod
* 通过replicas来指定副本数量
* 通过template定义Pod的模板用于Pod的创建、扩容

## 创建Replicset应用

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: pod-nginx-rp
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx-container
  template:
    metadata:
      labels:
        app: nginx-container
    spec:
      containers:
        - name: nginx1
          image: nginx:1.21
          imagePullPolicy: IfNotPresent
          ports:
            - name: web            # 端口映射命名
              containerPort: 80    # 声明容器端口
              protocol: TCP        # 声明协议
```



> 注意因为Replicset类型是根据标签选择Pod的，如果Pod的标签和选择器不匹配就会在创建的时候报错
>
> error: unable to recognize "1-Replicset.yaml": no matches for kind "Replicset" in version "apps/v1"

## Replicset集群某台机器故障了故障也不会自动转移

# Deployment(建议)

ReplicSet可以确保在运行的时候指定副本数，但是Deployment是一个更高级别的概念，它管理Replicset并未Pod提供声明性更新以及许多其他功能，因此建议使用Deplyment而不是直接使用ReplicSet

* 使用Deployment自动创建Replicset，由Replicset自动在后台创建

* 升级: Recreate删除所有在创建、或者RollingUpdate滚动升级逐步替换

* 回滚：当升级出现问题可以回滚到上一个稳定版本或指定版本

* 扩容：扩大或缩小副本数

* 暂停和启动：对于每次升级都可以随时暂停或启动

    

> 和Replicset一样，同样需要通过selector去选择pod

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: pic-hb-nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      pic-hb-nginx-app: pic-hb-nginx-container
  template:
    metadata:
      labels:
        pic-hb-nginx-app: pic-hb-nginx-container
    spec:
      containers:
        - name: nginx1
          image: nginx:1.21
          imagePullPolicy: IfNotPresent
          ports:
            - name: web            # 端口映射命名
              containerPort: 80    # 声明容器端口
              protocol: TCP        # 声明协议
          livenessProbe:
            tcpSocket:
              port: 80
```

## 滚动升级

### 下1个上一个，上1个，下一个

```yaml
# 下一个上一个
  strategy:
   type: RollingUpdate
   rollingUpdate:
     maxSurge: 0
     maxUnavailable: 1
```

```yaml
# 上一个下一个
  strategy:
   type: RollingUpdate
   rollingUpdate:
     maxSurge: 1
     maxUnavailable: 0
```

### 先扩容百分值多少，在干掉百分之多少

```yaml
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 0
```

### 先干掉百分之多少，在启动百分值多少

```yaml
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 0
      maxUnavailable: 25%
```



## 升级版本和回滚

### 查看版本

```
root@cka001:~/yaml/pod-controler# kubectl rollout history deployment pic-hb-nginx
deployment.apps/pic-hb-nginx
REVISION  CHANGE-CAUSE
1         <none>
2         <none>
```

### 查看版本的信息

```
root@cka001:~/yaml/pod-controler# kubectl rollout history deployment pic-hb-nginx --revision=1
deployment.apps/pic-hb-nginx with revision #1
Pod Template:
  Labels:	pic-hb-nginx-app=pic-hb-nginx-container
	pod-template-hash=78c9df86cb
  Containers:
   nginx1:
    Image:	nginx:1.21
    Port:	80/TCP
    Host Port:	8081/TCP
    Liveness:	tcp-socket :80 delay=0s timeout=1s period=10s #success=1 #failure=3
    Environment:	<none>
    Mounts:	<none>
  Volumes:	<none>
```

### 回滚

```
root@cka001:~/yaml/pod-controler# kubectl rollout undo deployment pic-hb-nginx --to-revision=1
deployment.apps/pic-hb-nginx rolled back

# 如果--to-revision不加参数默认回滚最后一个版本
```

> 如果版本信息是一致的默认保留最新的一个版本号，回滚了1后，1没有了，改为3了

```
root@cka001:~/yaml/pod-controler# kubectl rollout history deployment pic-hb-nginx
deployment.apps/pic-hb-nginx
REVISION  CHANGE-CAUSE
2         <none>
3         <none>


```

# DaemonSet

1. daemonsets可以保证指定的pod在每个节点上都会运行一个，且只运行一个

2. 适用于需要部署agent的场景， 如监控agent、flume等agent类型的机器
3. 当节点加入了kubernetes集群后不需要操作他会自动的去部署DaemonSet集群
4. 当节点被删除后，被移除节点的DaemonSet的pod会被删除
5. 如果是DaemonSet的pod被杀死、崩溃、会自动在该Node节点自动创建DaemonSet新的Pod



## 配置

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: monitoring-agent
spec:
  selector:
    matchLabels:
      monitoring-agent-app: monitoring-agent-container
  template:
    metadata:
      labels:
        monitoring-agent-app: monitoring-agent-container
    spec:
      volumes:
        - name: monitoring-dir
          hostPath:
            path: /monitoring/agent/
      hostNetwork: true
      containers:
        - name: zabbix-agent
          image: zabbix/zabbix-agent
          imagePullPolicy: IfNotPresent
          ports:
            - name: zabbix-port            # 端口映射命名
              containerPort: 10050         # 声明容器端口
          livenessProbe:
            tcpSocket:
              port: 10050
```

## 例子

DaemonSet 部署ingress + 污点，实现专机转用

# StatefulSet

能够保证Pod的每个副本在整个生命周期名称是不变的，这个只有StatefulSet能保证，而其他Controller不提供这个功能

其他Controller当某个Pod发生故障需要删除并重新启动时，Pod的名称会放生变化

StatefulSet会保证副本按照固定的顺序启动、更新、回滚

* 稳定的持久化存储，即Pod重新调度后还能访问到相同的持久化存储，基于PVC实现
* 稳定的网络标识，即Pod重新调度后Pod的Name和HostName不变，基于（Headless就是么有ClusterIP的server实现）
* 有序部署，有序扩展，即Pod是有顺序的，比如上一个Pod必须是Running或者Redy的才继续，且0~1，1~2，2~N
* 有序收缩，从N~0

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: pic-hb-nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      pic-hb-nginx-app: pic-hb-nginx-container
  serviceName: pic-hb-nginx-container
  template:
    metadata:
      labels:
        pic-hb-nginx-app: pic-hb-nginx-container
    spec:
      containers:
        - name: nginx1
          image: nginx:1.21
          imagePullPolicy: IfNotPresent
          ports:
            - name: web            # 端口映射命名
              containerPort: 80    # 声明容器端口
              protocol: TCP        # 声明协议
          livenessProbe:
            tcpSocket:
              port: 80
```

# Job & cronJob

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: test-job
spec:
  backoffLimit: 4
  template:
    metadata:
      labels:
        app: test-job
    spec:
      containers:
      - name: test-job
        image: busybox
        command: ["echo",  "hello world"]
      restartPolicy: OnFailure


```

```yaml
apiVersion: batch/v1beta1
kind: CronJob
metadata:
 name: hello #Cronjob的名称
spec:
  schedule: "* * * * *"   #job执行的周期，cron格式的字符串
  suspend: true
  startingDeadlineSeconds: 120
  successfulJobsHistoryLimit: 3
  jobTemplate:  #job模板
    spec:
      backoffLimit: 4
      template:
        metadata:
          labels:
            app: hello-cronjob
        spec:
          containers:
          - name: hello-cronjob
            image: busybox
            command: ["/bin/sh","-c","date;echo  Hello from the Kubernetes cluster"] #job具体执行的任务
          restartPolicy: OnFailure


```

