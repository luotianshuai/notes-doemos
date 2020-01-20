[TOC]

## 备注

操作系统: CentOS Linux release 7.4.1708 (Core)
内核版本: 3.10.0-693.el7.x86_64

## Docker 安装

```sh
# 备份机器上的yum配置文件
cd /etc/
mv yum.repos.d yum.repos.d.back
mkdir yum.repos.d
cd yum.repos.d


# 下载国内的镜像源
wget http://mirrors.aliyun.com/repo/Centos-7.repo
wget http://mirrors.163.com/.help/CentOS7-Base-163.repo
wget http://mirrors.aliyun.com/repo/epel-7.repo


# 重建cache
yum clean all
yum makecache

# 安装docker
yum -y install docker

# 启动服务并设置为开机启动
systemctl enable docker
```

## docker 镜像检索下载

- 检索镜像
- 下载镜像

### 检索镜像

![镜像检索标识](./resource/Docker-1-1.png)

### 下载镜像

```sh
[root@localhost ~]# docker pull docker.io/redis
Trying to pull repository docker.io/library/redis ...
latest: Pulling from docker.io/library/redis
8ec398bc0356: Pull complete
da01136793fa: Pull complete
cf1486a2c0b8: Pull complete
a44f7da98d9e: Pull complete
c677fde73875: Pull complete
727f8da63ac2: Pull complete
Digest: sha256:90d44d431229683cadd75274e6fcb22c3e0396d149a8f8b7da9925021ee75c30
Status: Downloaded newer image for docker.io/redis:latest
```

如果报错:`**x509: certificate has expired or is not yet valid**`本地时间不对同步下时间

```sh
# 安装ntpdate工具
yum -y install ntp ntpdate
# 同步
ntpdate cn.pool.ntp.org
```

## Docker 本地镜像管理

> 对已经下载到本地的镜像进行操作

- 查看本地仓库镜像
- 删除本地镜像 rmi (rm images)

```sh
# 查看本地镜像有那些
docker images

# 删除本地镜像使用rmi
docker rmi 9b188f5fb1e6
```

## Docker Images 启停管理

> images 启停管理

- 运行本地 images
- 查看正在运行的 images
- 停正在运行的 images
- 启动已停的 images
- 删除在管理列表里的 images
