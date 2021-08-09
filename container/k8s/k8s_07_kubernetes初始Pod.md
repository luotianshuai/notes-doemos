[TOC]

# 初识Pod

Pods是Kubernetes集群的最小管理单元，我们在发布的时候不是发布的容器，而是Pod

Pod里包含了1个或者多个容器（container）、存储、网络、以及如何运行的规范

## 为什么会有Pod这种模式

因为在很多情况下，一个服务可能是由: web程序、memcached、mysql紧密耦合才能提供服务的，所以有了pod这个概念

<img src="images/image-20210806094000669.png" alt="image-20210806094000669" style="zoom:50%;" />

## Pod主要有两种使用

* 单Pod单容器：One-container-per-Pod，最常见的Kubernetes用例，在这种情况下可以将Pod视为单个容器的封装，而Kubernetes直接管理Pod而不是容器
* 运行多个需要协同工作的容器的Pod：Pod封装由多个容器组成的应用程序，这些容器紧密耦合共享资源

## 如何管理容器

* 网络：每个Pod会分配一个唯一的IP，Pod中每个容器都共享网络命名空间，包括IP地址端口，Pod内的容器可里理解为在一个主机上并且可以使用localhosts通信。当Pod中的容器与Pod外部通信必须协调他们如何使用共享资源（比如端口）
* 存储：Pod可以指定一组共享存储卷。Pod中的所有容器都可以访问共享存储卷，从而允许这些容器共享数据。如果需要重新启动其中一个容器，则卷还允许卷中的数据持久存储

## 

* 每当启动一个Pod，同时会启动一个pause容器（伴随容器），pause容器伴随的Pod启动，伴随的Pod销毁。
* pause容器实现了Pod容器共享网络空间



> 备注:k8s并没有针对运行时、网络、存储提供相应的组件只是提供了对应的接口
>
> CRI（Container Runtime Interface），CNI（Container Network Interface）,CSI（Container Storage Interface）

在容器内部通过pause容器实现了Pod容器共享网络空间


## Pod的运行状态

| Value               | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| Pending(待定状态)   | The Pod has been accepted by the Kubernetes cluster, but one or more of the containers has not been set up and made ready to run. This includes time a Pod spends waiting to be scheduled as well as the time spent downloading container images over the network.（一般是等待镜像下载或者网络就绪） |
| Running（正常运行） | The Pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. |
| Succeeded           | All containers in the Pod have terminated in success, and will not be restarted. |
| Failed              | All containers in the Pod have terminated, and at least one container has terminated in failure. That is, the container either exited with non-zero status or was terminated by the system. |
| Unknown             | For some reason the state of the Pod could not be obtained. This phase typically occurs due to an error in communicating with the node where the Pod should be running.（一般是到网络不通导致） |
|                     |                                                              |
|                     |                                                              |



![image-20210806095821840](images/image-20210806095821840.png)

# 创建Pod

## 通过yaml创建

通过yaml创建

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-mem
  labels:
    app: pmem
spec:
  containers:
   - name: container-mem
     image: plinux/stress
     command: ["stress"]
     args: ["--vm", "1", "--vm-bytes", "150M", "--vm-hang", "1"] 
```



```
root@cka01:~/yaml# kubectl create -f memory-demon.yaml

root@cka01:~/yaml# kubectl get pod -o wide
NAME      READY   STATUS    RESTARTS   AGE   IP              NODE    NOMINATED NODE   READINESS GATES
pod-mem   1/1     Running   0          58s   10.244.204.71   cka03   <none>           <none>
```

## 镜像下载策略

### 创建Pod的时候指定镜像下载策略

我们制定了镜像，镜像下载有3中模式

* Always：每次都下载
* Never：只是用本地镜像，从不下载
* IfNotPresent：只有当本地没有的时候才去下载

```yaml
....
  containers:
   - name: container-mem
     image: plinux/stress
     imagePullPolicy: IfNotPresent
     command: ["stress"]
     args: ["--vm", "1", "--vm-bytes", "150M", "--vm-hang", "1"] 
```

### 对已经创建的Pod修改

```
 kubectl edit pod pod-mem
```

## Pod资源配额

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: demon-1
    
---
apiVersion: v1
kind: Pod
metadata:
  name: pod-mem
  namespace: demon-1
spec:
  containers:
   - name: container-mem
     image: polinux/stress
     imagePullPolicy: IfNotPresent
     resources:
       limits:
         memory: "200Mi"   # 这里限制最多200M
       requests:
         memory: "100Mi"   # 我请求100M哪里有资源调度到哪里去
     command: ["stress"]
     args: ["--vm", "1", "--vm-bytes", "150M", "--vm-hang", "1"]   # 这里程序运行需要150M会一直用150M

```

> 小技巧: 看上面我们已经接触到Namespace了现在可以通过-n先锁定命名空间在锁定资源了，这样在使用table的时候可以自动补全

```
root@cka01:~/yaml# kubectl -n demon-1 get pod pod-mem 
NAME      READY   STATUS    RESTARTS   AGE
pod-mem   1/1     Running   0          6m39s
```

## 注意事项

* 如果删除了Namespaces里面的资源都会被删除

# 登录Pod容器

先创建一个

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: demon
    
---
apiVersion: v1
kind: Pod
metadata:
  name: pod-mem
  namespace: demon
spec:
  containers:
   - name: container-mem-1
     image: polinux/stress
     imagePullPolicy: IfNotPresent
     resources:
       limits:
         memory: "200Mi"
       requests:
         memory: "100Mi"
     command: ["stress"]
     args: ["--vm", "1", "--vm-bytes", "150M", "--vm-hang", "1"] 
   - name: container-mem-2
     image: polinux/stress
     imagePullPolicy: IfNotPresent
     resources:
       limits:
         memory: "200Mi"
       requests:
         memory: "100Mi"
     command: ["stress"]
     args: ["--vm", "1", "--vm-bytes", "150M", "--vm-hang", "1"]
```



```
# 默认登录第一个容器
kubectl -n demon exec pod-mem -it bash

# 如果多个容器可以选择制定容器
kubectl -n demon exec pod-mem -it -c container-mem-1 bash
```

# 通过标签选择Pod

先创建一个Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-mem
  labels: 
    app: test
spec:
  containers:
   - name: container-mem-1
     image: polinux/stress
     imagePullPolicy: IfNotPresent
     resources:
       limits:
         memory: "200Mi"
       requests:
         memory: "100Mi"
     command: ["stress"]
     args: ["--vm", "1", "--vm-bytes", "150M", "--vm-hang", "1"] 
```

## apply申请-更新

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-mem
  labels: 
    app: demon
spec:
  containers:
   - name: container-mem-1
     image: polinux/stress
     imagePullPolicy: IfNotPresent
     resources:
       limits:
         memory: "200Mi"
       requests:
         memory: "100Mi"
     command: ["stress"]
     args: ["--vm", "1", "--vm-bytes", "150M", "--vm-hang", "1"] 
```

修改了后现在就不能用create了，需要是apply~

# edit 或通过patch修改

```
kubectl edit pod pod-mem
```

```
kubectl patch pod pod-mem -p '"metadata": {"labels": {"app": "demon"}}'
```

> 这两种修改的方式如果只修改labels，annannotations不会被修改，很容易忘记，所以一般建议都通过yaml去做

# init container

这个容器比较特殊比如说你有一个nginx容器，你需要先把nginx配置文件拉下来在启动nginx服务，这个时候可以使用init，如果先启动的nginx容器在拉配置，会导致nginx配置不生效

* init container总是需要执行完且成功
* 如果init container执行失败kubernetes会一直尝试去执行它知道成功
* 如果指定了多个init container会把所有的init container都执行完才执行后面的容器启动

## 应用场景

* 进行应用初始化，比如下载配置文件拉代码
* 服务启动前的依赖检查，比如web服务启动前先验证mysql是否启动

## 例子

yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-mem
  labels: 
    app: demon
spec:
  containers:
   - name: container-mem-1
     image: polinux/stress
     imagePullPolicy: IfNotPresent
     resources:
       limits:
         memory: "200Mi"
       requests:
         memory: "100Mi"
     command: ["stress"]
     args: ["--vm", "1", "--vm-bytes", "150M", "--vm-hang", "1"] 
   - name: container-mem-2
     image: polinux/stress
     imagePullPolicy: IfNotPresent
     resources:
       limits:
         memory: "200Mi"
       requests:
         memory: "100Mi"
     command: ["stress"]
     args: ["--vm", "1", "--vm-bytes", "150M", "--vm-hang", "1"]

  initContainers:
   - name: container-init-1
     image: busybox:1.28
     imagePullPolicy: IfNotPresent
     command: ["sh", "-c", "echo init containers 1 && sleep 10"]
   - name: container-init-2
     image: busybox:1.28
     imagePullPolicy: IfNotPresent
     command: ["sh", "-c", "echo init containers 2 && sleep 20"]
```



```
kubectl create -f 4-mem.yaml

root@cka01:~/yaml# kubectl get pod --watch
NAME      READY   STATUS     RESTARTS   AGE
pod-mem   0/2     Init:0/2   0          41s
pod-mem   0/2     Init:1/2   0          42s
pod-mem   0/2     Init:1/2   0          43s
pod-mem   0/2     PodInitializing   0          63s
pod-mem   2/2     Running           0          64s
```

# static pod 静态Pod

它不是由API管理的而是由节点上的kubelet通过配置文件进行管理的，如果挂了kubelet就会自动拉起它

* Static Pod总是绑定在一个特定的节点上
* Kubelet会自动尝试为Static Pod去注册一个镜像POD，虽然不可以用来管理但是可以看到它

Kubeadm部署的集群Static Pod默认放在/etc/kubernetes/manifests/ 目录中

`创建一个静态Pod`

```yaml
root@cka03:/etc/kubernetes/manifests# cat nginx.yaml 
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels: 
    app: nginx
spec:
  containers:
    - name: nginx-1
      image: nginx
      imagePullPolicy: IfNotPresent
      ports:
        - name: container-nginx
          containerPort: 80
          protocol: TCP
```


