[TOC]



# Label和Annotation

## Label

* 用来标识元信息
* Controller和Service可以通过Label selector 控制Pod的生命周期
* 对调度产生影响：比如说我创建某个应用，我可以让它运行到某个打了标签的节点上或者不运行在打了某个标签的节点上
* 影响NetworkPolicy



## Annotaion

* 它是注释信息、不影响调度
* 可以被程序应用获取信息

# 如何创建使用Label和Annotaion

## 通过命令行

```
# 添加
kubectl label/annotaion <resource> foo=bar
# 删除
kubectl label/annotaion <resource> foo


root@cka01:~# kubectl label nodes cka01 disktype=ssd
node/cka01 labeled
root@cka01:~# kubectl get nodes cka01 --show-labels
NAME    STATUS   ROLES                  AGE   VERSION   LABELS
cka01   Ready    control-plane,master   45h   v1.20.5   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,disktype=ssd,kubernetes.io/arch=amd64,kubernetes.io/hostname=cka01,kubernetes.io/os=linux,node-role.kubernetes.io/control-plane=,node-role.kubernetes.io/master=


root@cka01:~# kubectl label nodes cka01 disktype-
node/cka01 labeled
root@cka01:~# kubectl get nodes cka01 --show-labels
NAME    STATUS   ROLES                  AGE   VERSION   LABELS
cka01   Ready    control-plane,master   45h   v1.20.5   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=cka01,kubernetes.io/os=linux,node-role.kubernetes.io/control-plane=,node-role.kubernetes.io/master=
```

> 小TIPS：kubernetes的角色就是通过label来标识的，kubenetes通过它来获取当前节点的角色信息

```
root@cka01:~# kubectl get nodes --show-labels
NAME    STATUS   ROLES                  AGE   VERSION   LABELS
cka01   Ready    control-plane,master   46h   v1.20.5   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=cka01,kubernetes.io/os=linux,node-role.kubernetes.io/control-plane=,node-role.kubernetes.io/master=
cka02   Ready    <none>                 46h   v1.20.5   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=cka02,kubernetes.io/os=linux
cka03   Ready    <none>                 46h   v1.20.5   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=cka03,kubernetes.io/os=linux

# 你会发先master节点上会多出一个node-role.kubernetes.io/master=  他截取的是: node-role.kubernetes.io/  和 =中间的内容: master
# 看看效果
root@cka01:~# kubectl label nodes cka02 node-role.kubernetes.io/worker=
node/cka02 labeled
root@cka01:~# kubectl get nodes --show-labels
NAME    STATUS   ROLES                  AGE   VERSION   LABELS
cka01   Ready    control-plane,master   46h   v1.20.5   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=cka01,kubernetes.io/os=linux,node-role.kubernetes.io/control-plane=,node-role.kubernetes.io/master=
cka02   Ready    worker                 46h   v1.20.5   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=cka02,kubernetes.io/os=linux,node-role.kubernetes.io/worker=
cka03   Ready    <none>                 46h   v1.20.5   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=cka03,kubernetes.io/os=linux


```



## 通过yaml定义

### 定义Label

```yml
labels:
	environment: production
	app: nginx
```

定义Annotaion

```yaml
annotaion:
	imageregistry: "https://hub.docker.com"
```

