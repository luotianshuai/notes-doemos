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

## Docker 容器管理

> 容器启停 启停管理

- 通过一个镜像创建一个容器
- 查看已启动的容器列表
- 启、停、重启已经在容器列表的容器
- 查看容器使用的资源
- 删除在管理列表里的 images

### 通过一个镜像创建一个容器

```python
# 如果本地不存images会向远程仓库获取
docker run -itd --name="redis-test" -p 6379:6379 docker.io/redis

# 常用参数 -itd --name  -p
"""
-i: 以交互模式运行容器，通常与 -t 同时使用；
-t: 为容器重新分配一个伪输入终端，通常与 -i 同时使用；
-d: 后台运行容器，并返回容器ID；

--name="test-redis"为启动的images起一个名称；

-p: 指定端口映射，格式为：主机(宿主)端口:容器端口

后面跟镜像名称

"""
```

### 查看已启动的容器列表

```python
[root@localhost ~]# docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
68a268ed5113        docker.io/redis     "docker-entrypoint..."   15 hours ago        Up 15 hours         0.0.0.0:6379->6379/tcp   redis-test

"""
CONTAINER ID: 容器 ID。
IMAGE: 使用的镜像。
COMMAND: 启动容器时运行的命令。
CREATED: 容器的创建时间。
STATUS: 容器状态。
    状态有7种：
        created（已创建）
        restarting（重启中）
        running（运行中）
        removing（迁移中）
        paused（暂停）
        exited（停止）
        dead（死亡）
"""
```

### 启、停、重启、删除 已经在容器列表的容器

```python
[root@localhost ~]# docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
68a268ed5113        docker.io/redis     "docker-entrypoint..."   16 hours ago        Up 2 minutes        0.0.0.0:6379->6379/tcp   redis-test
# docker ps -a 展示所有容器列表的信息包含已经停止的
[root@localhost ~]# docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                     PORTS                    NAMES
e080292abd47        docker.io/nginx     "nginx -g 'daemon ..."   35 seconds ago      Exited (0) 5 seconds ago                            nginx-test
68a268ed5113        docker.io/redis     "docker-entrypoint..."   16 hours ago        Up 2 minutes               0.0.0.0:6379->6379/tcp   redis-test
[root@localhost ~]#

# 启动已停止的容器
docker start e080292abd47

# 停止已启动的容器
docker stop 68a268ed511

# 重启已启动的容器(容器容器已停止的话直接拉起)
docker restart e080292abd47

# 从容器列表删除已停掉的容器
docker rm e080292abd47

# 从容器列表中删除已经启动的容器,加-f强制删除
docker rm -f 68a268ed5113

```

### 如何进入容器

> Docker 是进程的容器必须启动一个前台任务

- 启用一个交互终端
- 直接进入启动的 daocker 容器内不再开启一个终端(不推荐很容易误操作退出)

```sh
# 打开一个交互式的shell
docker exec -it a82cf07ddc39 "/bin/bash"

#
docker attach --sig-proxy=false centos

```

### 查看容器使用的资源

```python
[root@localhost ~]# docker stats --no-stream
CONTAINER           CPU %               MEM USAGE / LIMIT       MEM %               NET I/O             BLOCK I/O           PIDS
a82cf07ddc39        0.19%               8.375 MiB / 972.6 MiB   0.86%               656 B / 656 B       0 B / 0 B           4

```

[CONTAINER]：容器 ID
[CPU %]：CPU 百分比的使用情况。
[MEM USAGE / LIMIT]：当前使用的内存和最大可以使用的内存。
[MEM %]：以百分比的形式显示内存使用情况。
[NET I/O]：网络 I/O 数据。
[BLOCK I/O]：磁盘 I/O 数据。
[PIDS]：PID 号
