[TOC]



# 架构设计

## 典型的主从架构Master-Slave



# 核心组件

## Master节点: 它是大脑控制着



### etcd(所有的状态-状态修改完保留在etcd里)

举个例子：etcd里好比有一个镜像，它存储着所有集群的信息，可以通过etcd的信息重新恢复一个集群

### apiserver

- 所有操作的入口和出口核心组件都需要通过apiserver
- apiserver写入etcd并发送到Node节点的kubelet)
- 并且提供了认证、授权、访问控制、API注册和发现

### controller-manager
- 它是个管理者，我们定义一个服务，本身也是期望一个状态，也是通过controller-manager进行状态管理的
- 它会一直去检测集群的状态通过api，发现和定义的不一致就通过API去开始修正这个状态修正为我们定义的状
- 负责管理集群内的Node、Pod副本数、服务端点(Endpoint)、命名空间(NameSpace)、ServiceAccount、资源配合(ResourceQuota)
### scheduler
- 它是个调度者
- 它承上启下
>承上: 它通过API接收controller-manager的状态并根据manager期望的状态去调度资源
启下: 它通过API按照特定的调度算法和调度策略选择合适的一个Node然后发送给API，然后API下发指令到kubelet去执行

比如说我有一个应用需要使用4核8G，我该放在那台机器上更合理 



## Node节点: 实际干活的 

### kubelet(心跳、它来管理一个Pod的声明周期、Master的指令都会下发到它这里)

### container-runtime（管理底层容器的声明周期）

### kube-proxy(对外暴露Pod里面的服务)

# Add-ons插件

* Core-dns在kubernetes老版本里叫kube-dns，后来在新版本里叫core-dns负责为整个集群提供服务注册和服务发现

* ingress Controller为服务提供七层负载均衡
* metric-server手机节点和Pod资源使用
* Dashboard提供GUI，web图形界面

# Kubernetes接口

一直在说Kubernetes是一个编排工具，Kubernetes本身是不提供底层容器、网络、存储的，但是它暴露了对应的接口

比如说我实现了一个接口CRI并定义了规范，Dokcer支持这个规范Kubernetes就可以通过CRI去调用Docker去创建、销毁、管理Docker容器，那么Docker也可以成为了Kubernetes的底层容器

## CRI（Container Runtime Interface）

容器引擎运行时接口，可以通过这个CRI接口去管理容器资源

## CNI（Container Network Interface）

同理让容器网络通信

## CSI（Container Storage Interface）

同理让容器可以使用存储资源