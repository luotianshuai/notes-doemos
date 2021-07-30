[TOC]

# kubernetes前世今生

## Kubernetes的诞生

2013年容器化技术Docker开源问世之后，有效的解决软件运行时环境差异带来的问题，达到其 Build once, Run anywhere

期间google也加入了容器平台【LMCTY是Let me contain that for you的缩写。它是Google的容器技术栈的开源版本】，想强制容器化份额，引领容器化技术，但是呢发现干不过Docker

秉承着既然在底层干不过你，往上层走后面去兼容收编你的态度，2014年Google开源了内部自己的容器编排系统：Borg，2015年Kubernetes的V1.0版本正式发布



## Kubernetes的标准化

随着Kubernetes的大面积使用，使用者开始担心Google一家独大，人心惶惶，担心后面会不是有什么幺蛾子比如说闭源、付费啊、安全啊等问题，这些问题如果不解决的话，你细品~ 你敢用吗？

所以在2015年7月，Google联合Linux基金会【Linux Foundation】组建了人们现在熟知CNCF基金会【】

CNCF的建立为相关容器技术生态制定行业标准。这一系列举措成功让 K8s 成为云原生基础设施生态的核心，CNCF 也跻身全球最成功的开源基金会行列

* 解决了人们的担忧问题，大量巨头开始加入CNCF，人多力量大

* 2017年的时候Kubernetes基本上已经剩下容器编排大战

    

## Kubernetes优势使其赢得了容器编排大战

* 大厂出品是Google多年容器编排的系统的开源版本，大家对其有非常大的认可度
* CNCF基金会解决了大家对后续Kubernetes的担忧问题【闭源、收费、安全】等问题
* 大量巨头的加入使Kubernetes的发展如虎添翼飞速发展
* Kubernetes具备很强的横向扩展能力、并且架构设计采用了传统的Master-Slave模式易于接受
* Kubernetes在功能也非常的强大包括、调度、服务发现、健康检测、平滑升级回滚等

## Kubernetes版本

### 版本号的含义

* Kubernetes版本表示为xyz，其中x是主要版本，y是次要版本，z是补丁版本，[遵循语义版本控制术语](https://semver.org/lang/zh-CN/)
* 我们一般关心X.Y.0(稳定版本),比如:v1.21.0

```
k8s 发行版与 github 分支的关系
简单来讲，kubernetes项目存在3类分支(branch)
* 分别为master
* release-X.Y
* release-X.Y.Z

k8s 发行版与 github 分支的关系
简单来讲，kubernetes项目存在3类分支(branch)
* 分别为master
* release-X.Y
* release-X.Y.Z

master分支上的代码是最新的，每隔2周会生成一个发布版本(release)，由新到旧以此为master-->alpha-->beta-->Final release
这当中存在一些cherry picking的规则，也就是说从一个分支上挑选一些必要pull request应用到另一个分支上
我们可以认为X.Y.0为稳定的版本，这个版本号意味着一个Final release。
一个X.Y.0版本会在X.(Y-1).0版本的3到4个月后出现。 
X.Y.Z为经过cherrypick后解决了必须的安全性漏洞、以及影响大量用户的无法解决的问题的补丁版本。 
总体而言，我们一般关心X.Y.0(稳定版本)，和X.Y.Z(补丁版本)的特性。

例子
v1.21.0 : 1为主要版本 : 21为次要版本 : 0为补丁版本
```

[kubernetes版本](https://github.com/kubernetes/kubernetes/releases)

## Kubernetes的应用领域

* 最早期的应用部署
* 数据中心
* 各大云平台：华为、腾讯、阿里，可以快速创建kubernetes
* 在比如餐饮业把他们整套系统包括下单、收单、发货等等系统都上到了Kubernetes上
* 边缘计算比如说在国内有很多的工厂制造业都在咨询相关的技术

