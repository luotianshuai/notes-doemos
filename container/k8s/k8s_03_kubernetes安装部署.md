[TOC]


## 部署方式对比
| 部署方式 | 优点                                                         | 缺点                                                         | 是否支持容器化                       |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------ |
| 源码部署 | 能快速熟悉kubernetes架构和组件构成和组件间的耦合关系         | 部署繁琐、复杂且易出错、后期升级维护麻烦                     | 否                                   |
| RKE      | 使用方便快捷1条命令、1个配置文件并且能自动给Kubernetes组件做HA | 全部组件都做成了docker image部署后想定制修改需要重新改yaml文件 | 全部容器化                           |
| Kubeadm  | kubernetes社区推荐的部署工具、能紧跟社区版本、部署起来方便快捷 | 镜像在google奖项仓库国内使用非常麻烦、没有自动的HA需要手动配置 | 部分容器化、如kubelete组件没有容器化 |





# 安装Kubernetes

## Ubuntu安装Docker

```
# step 1: 安装必要的一些系统工具
sudo apt-get update
sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common
# step 2: 安装GPG证书
curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
# Step 3: 写入软件源信息
sudo add-apt-repository "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
# Step 4: 更新并安装Docker-CE
sudo apt-get -y update
sudo apt-get -y install docker-ce

# 安装指定版本的Docker-CE:
# Step 1: 查找Docker-CE的版本:
# apt-cache madison docker-ce
#   docker-ce | 17.03.1~ce-0~ubuntu-xenial | https://mirrors.aliyun.com/docker-ce/linux/ubuntu xenial/stable amd64 Packages
#   docker-ce | 17.03.0~ce-0~ubuntu-xenial | https://mirrors.aliyun.com/docker-ce/linux/ubuntu xenial/stable amd64 Packages
# Step 2: 安装指定版本的Docker-CE: (VERSION例如上面的17.03.1~ce-0~ubuntu-xenial)
# sudo apt-get -y install docker-ce=[VERSION]

```

### 优化TABLE自动补全

Centos需要安装一个包就可以了，但是ubuntu只需要启用一个配置即可，vim /etc/bash.bashrc

```
# enable bash completion in interactive shells
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi


```

### 解决问题

当执行`docker info`看到有提示: WARNING: No swap limit support，只有Ubuntu的系统会有这个问题

```
# step 1 修改配置
vim /etc/default/grub
# GRUB_CMDLINE_LINUX 新增cgroup_enable=memory swapaccount=1
GRUB_CMDLINE_LINUX="cgroup_enable=memory swapaccount=1 net.ifnames=0 consoleblank=600 console=tty0 console=ttyS0,115200n8 nospectre_v2 nopti noibrs noibpb"

# step2 更新grub并重启
update-grub && reboot
```

修改默认的:iptables FORWARD 默认策略并持久化

```
# step 1 修改: /lib/systemd/system/docker.service
# 在Service下面新增
ExecStartPost=/sbin/iptables -P FORWARD ACCEPT

# step2 重启docker
systemctl daemon-reload && systemctl restart docker

```

### 修改Docker的daemon.json

```
cat > /etc/docker/daemon.json <<EOF
{
	"exec-opts": "native.cgroupdirver=systemd",
	"log-dirver": "json-file",
	"log-opts": {"max-size": "100m"},
	"storage-dirver": "overlay2"
}

EOF
```



