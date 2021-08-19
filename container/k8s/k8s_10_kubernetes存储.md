[TOC]

# VOLUMES应用场景

* 容器数据需要持久化存储的时候（正常容器在销毁后数据也随之销毁）
* Pod里面有多个容器需要共享数据的时候

# 容器存储

## Pod数据临时：emptyDir

emptyDir在Pod分配给节点时，首先创建有一个卷，这个卷开始是空的，容器内所有的container都可以挂载这个卷把数据同时写在一个地方

* emptyDir声明周期会随着Pod终结而终结
* 如果Pod异常退出emptyDir不会被销毁

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web1
  labels:
    type: nginx
  annotations:
    description: "hello kubernetes"
spec:
  volumes:
    - name: html-data
      emptyDir:

  containers:
    - name: test-vm-1
      image: polinux/stress
      imagePullPolicy: IfNotPresent
      volumeMounts:
        - name: html-data
          mountPath: /usr/share/nginx/html
      command: ["stress"]
      args: ["--vm", "1", "--vm-bytes", "150M", "--vm-hang", "1"]
    - name: nginx1
      image: nginx:1.21
      imagePullPolicy: IfNotPresent
      volumeMounts:
        - name: html-data
          mountPath: /usr/share/nginx/html
      ports:
        - name: web            # 端口映射命名
          containerPort: 80    # 声明容器端口
          protocol: TCP        # 声明协议
          hostPort: 8081       # 将声明的容器端口映射到宿主机

```

## hostPath

`hostPath` 卷能将主机节点文件系统上的文件或目录挂载到你的 Pod 中

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web1
  labels:
    type: nginx
  annotations:
    description: "hello kubernetes"
spec:
  volumes:
    - name: html-data
      path: /data/nginx/html/

  containers:
    - name: test-vm-1
      image: polinux/stress
      imagePullPolicy: IfNotPresent
      volumeMounts:
        - name: html-data
          mountPath: /usr/share/nginx/html
      command: ["stress"]
      args: ["--vm", "1", "--vm-bytes", "150M", "--vm-hang", "1"]
    - name: nginx1
      image: nginx:1.21
      imagePullPolicy: IfNotPresent
      volumeMounts:
        - name: html-data
          mountPath: /usr/share/nginx/html
      ports:
        - name: web            # 端口映射命名
          containerPort: 80    # 声明容器端口
          protocol: TCP        # 声明协议
          hostPort: 8081       # 将声明的容器端口映射到宿主机
```

# 持久化存储

## 持久卷: PV(Persistent Volume)

PersistenVolume（PV）：对存储资源创建和使用的抽象，使得存储作为集群中的资源管理，分为有静态与动态。
PersistentVolumeClaim（PVC）：让用户不需要关心具体的Volume实现细节

PV：提供者、提供存储容量
PVC：消费者、消费容量
注：PV与PVC成绑定关系。

容器应用-->卷需求模板-->数据卷定义

### pv和pvc的关系

pv和pvc是1v1对应的，当一个pv被pvc绑定后将不会被其他pvc绑定

### pv访问模式

```
PersistentVolume 卷可以用资源提供者所支持的任何方式挂载到宿主系统上。 如下表所示，提供者（驱动）的能力不同，每个 PV 卷的访问模式都会设置为 对应卷所支持的模式值。 例如，NFS 可以支持多个读写客户，但是某个特定的 NFS PV 卷可能在服务器 上以只读的方式导出。每个 PV 卷都会获得自身的访问模式集合，描述的是 特定 PV 卷的能力。

访问模式有：
不能被多个node读写
    ReadWriteOnce -- 卷可以被一个节点以读写方式挂载；
      * 块存储
      * hostpath
	
可以被多node读取，文件系统: nfs/clusterfs
ReadOnlyMany -- 卷可以被多个节点以只读方式挂载；
ReadWriteMany -- 卷可以被多个节点以读写方式挂载。
在命令行接口（CLI）中，访问模式也使用以下缩写形式：

RWO - ReadWriteOnce
ROX - ReadOnlyMany
RWX - ReadWriteMany
```

### pv的三种回收策略

* 保留（Retain）：允许人工处理保留数据，默认，正常pvc和pv绑定后，我们删除pvc数据不会被请求
* 回收（Recycle）：将执行清理操作，之后可以被其他pvc使用
* 删除（Delete）：诸如 AWS EBS、GCE PD、Azure Disk 或 OpenStack Cinder 卷这类关联存储资产也被删除（仅 NFS 和 HostPath 支持回收（Recycle）。 AWS EBS、GCE PD、Azure Disk 和 Cinder 卷都支持删除（Delete））

### PV状态

- Available（可用）-- 卷是一个空闲资源，尚未绑定到任何申领；
- Bound（已绑定）-- 该卷已经绑定到某申领；
- Released（已释放）-- 所绑定的申领已被删除，但是资源尚未被集群回收；
- Failed（失败）-- 卷的自动回收操作失败。

### 创建一个pv

### 创建一个pvc

