[TOC]

# Namespaces作用

Kubernetes的资源分为全局资源名Namespaces资源

```
root@cka01:~# kubectl api-resources
NAME                              SHORTNAMES   APIVERSION                             NAMESPACED   KIND
bindings                                       v1                                     true         Binding
componentstatuses                 cs           v1                                     false        ComponentStatus
configmaps                        cm           v1                                     true         ConfigMap
endpoints                         ep           v1                                     true         Endpoints
events                            ev           v1                                     true         Event
limitranges                       limits       v1                                     true         LimitRange
namespaces                        ns           v1                                     false        Namespace
nodes                             no           v1                                     false        Node
persistentvolumeclaims            pvc          v1                                     true         PersistentVolumeClaim
```

但是可以通过Namespaces去对资源进行统一管理

* 资源配额
* 资源隔离（Namespaces_A可以有一个nginx_app，Namespaces_B也可以有一个nginx_app）
* Namespaces不能嵌套
* 一个资源只能属于一个Namespaces

```
# 
root@cka01:~# kubectl get namespaces 
NAME              STATUS   AGE
default           Active   46h         # 默认空间
kube-public       Active   46h				 # 这个命名空间是自动创建的所有用户（包括未验证的用户）都可以读取
kube-system       Active   46h				 # kubernetes系统创建的对象命名空间
kube-node-lease   Active   46h				 
	# kubernetes发送心跳有助于确定节点的稳定性
	# 心跳有两种形式: NodeStatus 和 Lease对象
	# 每个节点的kube-node-lease都关联了一个Lease对象，可以在集群扩展的时候提高心跳检测的性能
	
# 注意: 系统创建的namespaces是无法删除的
```

# 管理namespaces

## 通过命令管理

```
# 添加
kubectl create namespace damon1
# 删除
kubectl delete namespaces damon1
```

## 通过yaml管理（推荐）


### api version说明

#### Alpha level（预期版：不建议用）

* 版本包含alpha(例如：v1alpha)
* 启用该特性可能会暴露Bug默认禁用
* 可能随时取消这个特性，并且不通知
* 在以后的软件版本，API可能会修改并且可能会不兼容且不通知
* 由于Bug风险增加和缺乏长期支持，建议仅在测试短期测试集群启用

#### Beta level（测试版: 可以用但是最好用在非关键业务）

* 版本包含beat（例如：v1beta1）
* 代码经过了很好的测试，启用该特性被认为安全的，默认启用
* 对整体的特性支持不会被删除，尽管细节可能会发生变化
* 在随后的beta版本中，可能会发生变化，但是会提供迁移到下一个版本的说明，可能需要删除或重新创建API对象，编辑过程可能需要一些思考。对于依赖改特性的应用程序，可能需要停机
* 由于后续版本可能会出现版本不兼容，建议只用于非关键业务。如果有多个可以用来升级的集群可以相对放宽该限制
* 处于beta版本可以进行反馈，但是如果进入稳定版就不会进行修改了

#### Stable level （稳定版: 放心用）

* 版本: v整数（例如: v1）
* 稳定版本将在后续版本中使用

```
apiextensions.k8s.io/v1
# 会发现在版本前面还有一段: apiextensions.k8s.io/  这个是API组进行归类管理的
```

## 帮助

可以通过： kubectl api-resources   来查看资源的对应的API版本

```
root@cka01:~/yaml# kubectl api-resources |grep -i namespaces
namespaces                        ns           v1                                     false        Namespace
```

都有那些api可以通过: kubectl api-versions查看

可以通过： kubectl explain namespaces  去查看资源说明来编写

```
root@cka01:~/yaml# kubectl explain namespaces
KIND:     Namespace
VERSION:  v1

DESCRIPTION:
     Namespace provides a scope for Names. Use of multiple namespaces is
     optional.

FIELDS:
   apiVersion   <string>
     APIVersion defines the versioned schema of this representation of an
     object. Servers should convert recognized schemas to the latest internal
     value, and may reject unrecognized values. More info:
     https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources

   kind <string>
     Kind is a string value representing the REST resource this object
     represents. Servers may infer this from the endpoint the client submits
     requests to. Cannot be updated. In CamelCase. More info:
     https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds

   metadata     <Object>
     Standard object's metadata. More info:
     https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata

   spec <Object>
     Spec defines the behavior of the Namespace. More info:
     https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status

   status       <Object>
     Status describes the current status of a Namespace. More info:
     https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status

root@cka01:~/yaml# 
```



## 创建

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: demon
  labels:
    app: demon
```

kubectl create -f my-namespaces.yaml

```
root@cka01:~/yaml# kubectl get namespaces 
NAME              STATUS   AGE
default           Active   47h
demon             Active   37s
kube-node-lease   Active   47h
kube-public       Active   47h
kube-system       Active   47h
root@cka01:~/yaml# kubectl get namespaces demon --show-labels
NAME    STATUS   AGE    LABELS
demon   Active   100s   app=demon
```



## 删除

kubectl delete -f my-namespaces.yaml
