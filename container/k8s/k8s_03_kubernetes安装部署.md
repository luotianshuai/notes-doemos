[TOC]


# 部署方式对比
| 部署方式 | 优点                                                         | 缺点                                                         | 是否支持容器化                       |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------ |
| 源码部署 | 能快速熟悉kubernetes架构和组件构成和组件间的耦合关系         | 部署繁琐、复杂且易出错、后期升级维护麻烦                     | 否                                   |
| RKE      | 使用方便快捷1条命令、1个配置文件并且能自动给Kubernetes组件做HA | 全部组件都做成了docker image部署后想定制修改需要重新改yaml文件 | 全部容器化                           |
| Kubeadm  | kubernetes社区推荐的部署工具、能紧跟社区版本、部署起来方便快捷 | 镜像在google奖项仓库国内使用非常麻烦、没有自动的HA需要手动配置 | 部分容器化、如kubelete组件没有容器化 |



## 源码部署优缺点

### 缺点

- 部署起来比较复杂
- 后期的升级维护比较复杂

### 优点

* 可以很快熟悉它的架构，但是在生产中使用的时候也会逐步去熟悉他



## 容器部署的优点

* 后期维护升级只需要升级下image就OK

# 安装Kubernetes

## Ubuntu安装Docker

```sh
# 系统版本
ubuntu1~18.04
# 准备工作（所有节点操作）

1. 配置主机名

hostnamectl set-hostname cka01 --static
hostnamectl set-hostname cka02 --static
hostnamectl set-hostname cka03 --static

2. 修改/etc/hosts

#以master为例

vim /etc/hosts
192.168.0.131 cka01


3. 修改apt源(国内机器需要修改)

# 清空/etc/apt/sources.list，并添加如下内容

deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse


# 执行apt源更新操作

apt update -y 

# 开启命令补全
# enable bash completion in interactive shells
# vim /etc/bash.bashrc
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi


4. 清空防火墙规则 并 关闭防火墙
iptables -F
ufw disable

5. 关闭swap分区
swapoff -a

6. 修改内核参数(启用ipv4转发和关闭swap分区)

cat >/etc/sysctl.d/k8s.conf<<EOF
  net.ipv4.ip_forward = 1
  vm.swappiness = 0
EOF
sysctl -p /etc/sysctl.d/k8s.conf

6. 加载内核模块

cat > /etc/modules-load.d/modules.conf<<EOF
br_netfilter
ip_vs
ip_vs_rr
ip_vs_wrr
ip_vs_sh
nf_conntrack_ipv4
EOF

for i in br_netfilter ip_vs ip_vs_rr ip_vs_wrr ip_vs_sh nf_conntrack_ipv4;do modprobe $i;done

7. 安装docker
# 国内
  # 允许apt使用https使用存储库
  apt -y install apt-transport-https ca-certificates curl software-properties-common
  # 添加docker官网的秘钥 # 安docker

  curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
  sudo add-apt-repository "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"

# 国外
apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  
apt update -y

# 查看docker版本
apt-cache madison docker-ce
# 安装
apt-get install -y docker-ce=5:19.03.15~3-0~ubuntu-bionic containerd.io

# 
mkdir -p /etc/docker

cat > /etc/docker/daemon.json<<EOF
{
    "exec-opts": ["native.cgroupdriver=systemd"],
    "log-driver": "json-file",
    "log-opts": {
        "max-size": "100m",
        "max-file": "10"
    },
    "registry-mirrors": ["https://pqbap4ya.mirror.aliyuncs.com"]
}
EOF

systemctl restart docker
systemctl enable docker

# 检查docker状态
docker info

# 只有ubuntu会有提示不支持内存限制警告解决方法: WARNING: No swap limit support
    修改: /etc/default/grub
    里面的内容:GRUB_CMDLINE_LINUX配置新增键值对: cgroup_enable=memory swapaccount=1

    # 更新grub然后重启
    update-grub && reboot

# 如果iptables默认是Drop的话需要改下
    # 临时
      iptables -P FORWARD ACCEPT
    # 永久
      vim /lib/systemd/system/docker.service
        server下新增: ExecStartPost=/sbin/iptables -P FORWARD ACCEPT

8. 安装kubeadm、kubectl、kubelet

# 国内
apt-get update && apt-get install -y apt-transport-https
curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | apt-key add - 
cat > /etc/apt/sources.list.d/kubernetes.list<<EOF 
deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main
EOF
apt update -y 
apt-cache madison kubelet

apt install -y kubelet=1.20.5-00  kubeadm=1.20.5-00  kubectl=1.20.5-00 
# 国外
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl
sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
apt update -y 
apt-cache madison kubelet
apt install -y kubelet=1.20.5-00  kubeadm=1.20.5-00  kubectl=1.20.5-00 



# 安装master(只在master上操作)

kubeadm config print init-defaults  > kubeadm-config.yaml

apiVersion: kubeadm.k8s.io/v1beta2
bootstrapTokens:
- groups:
  - system:bootstrappers:kubeadm:default-node-token
  token: abcdef.0123456789abcdef
  ttl: 24h0m0s
  usages:
  - signing
  - authentication
kind: InitConfiguration
localAPIEndpoint:
  advertiseAddress: 192.168.0.180
  bindPort: 6443
nodeRegistration:
  criSocket: /var/run/dockershim.sock
  name: cka01
  taints:
  - effect: NoSchedule
    key: node-role.kubernetes.io/master
---
apiServer:
  timeoutForControlPlane: 4m0s
apiVersion: kubeadm.k8s.io/v1beta2
certificatesDir: /etc/kubernetes/pki
clusterName: kubernetes
controllerManager: {}
dns:
  type: CoreDNS
etcd:
  local:
    dataDir: /var/lib/etcd
imageRepository: registry.cn-hangzhou.aliyuncs.com/google_containers
kind: ClusterConfiguration
kubernetesVersion: v1.20.5
networking:
  dnsDomain: cluster.local
  serviceSubnet: 10.96.0.0/12
  podSubnet: 10.244.0.0/16
scheduler: {}


kubeadm init --config kubeadm-config.yaml

Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:
# 添加自动补全
kubectl completion -h
  # 临时
    source <(kubectl completion bash)
  # 永久Ubuntu
    kubectl completion bash > ~/.kube/completion.bash.inc
    echo "source ~/.kube/completion.bash.inc" >> .profile

# 部署网络插件

curl https://docs.projectcalico.org/manifests/calico.yaml -O

kubectl apply -f calico.yaml

# 添加节点

kubeadm join 192.168.0.180:6443 --token abcdef.0123456789abcdef \
    --discovery-token-ca-cert-hash sha256:d19eafe0f6ea680a75aca46bdedf9ea20da869a09ff5923d335277ff95d4094e


# 在所有节点设置kubelet开机自启动
systemctl enable kubelet
```

# kubectl 如何简单快速了解

> 记住我们操作的是资源

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
persistentvolumes                 pv           v1                                     false        PersistentVolume


# 查看资源
kubectl get nodes										# 获取node节点
kubectl create namespace damon1			# 创建一个namespace
kubectl delete namespaces damon1    # 删除一个namespace

```

# Kubernetes网络插件对比

## Kubernetes网络

Kubernetes 对所有网络设施的实施，都需要满足以下的基本要求（除非有设置一些特定的网络分段策略）：

- 节点上的 Pod 可以不通过 NAT 和其他任何节点上的 Pod 通信
- 节点上的代理（比如：系统守护进程、kubelet）可以和节点上的所有Pod通信



| 列表       | Overlay                                    | L3 Routing                   | Underlay                             |
| ---------- | ------------------------------------------ | ---------------------------- | ------------------------------------ |
| 描述       | 二层报文被封装了IP数据中                   | 通过IP路由的方式进行数据交互 | 直接使用宿主所在的底层网络组件和功能 |
| 网络要求   | IP可达                                     | IP可达                       | IP可达                               |
| 性能       | 中性能损耗60%                              | 性能损耗30%                  | 几乎接近原生性能                     |
| 集群外访问 | Ingress/NodePort                           | Ingress/NodePort             | Ingress/NodePort                     |
| 访问控制   | NetworkPolicy                              | NetworkPolicy                | Iptables、宿主所在网络控制           |
| IP类型     | 虚拟IP                                     | 虚拟IP                       | 物理IP                               |
| 静态IP     | 不支持                                     | 不支持                       | 支持                                 |
| 场景       | 对性能要求不高，网络环境简单               | 大多数场景                   | 对性那个呢要求较高需要支持静态IP     |
| 开源产品   | Flannel-vxlan、OpenShift-sdn、Cisco-contiv | Clico、Flannel-HostGW        | MACvlan、lpvlan、sriov               |