[TOC]

# Kubernetes版本号含义

Kubernetes版本表示为xyz，其中x是主要版本，y是次要版本，z是补丁版本，遵循[语义版本控制术语](http://semver.org/)。有关更多信息，请参阅[Kubernetes发布版本](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/release/versioning.md)。

## Kubernetes 发行版与 github 分支的关系

简单来讲，kubernetes项目存在3类分支(branch)，分别为
-  master
- release-X.Y
- release-X.Y.Z

master分支上的代码是最新的，每隔2周会生成一个发布版本(release)，由新到旧以此为`master`-->`alpha`-->`beta`-->`Final release`

这当中存在一些cherry picking的规则，也就是说从一个分支上挑选一些必要pull request应用到另一个分支上

我们可以认为`X.Y.0`为稳定的版本，这个版本号意味着一个`Final release`。一个`X.Y.0`版本会在`X.(Y-1).0`版本的3到4个月后出现。

 `X.Y.Z`为经过cherrypick后解决了必须的安全性漏洞、以及影响大量用户的无法解决的问题的补丁版本。

 总体而言，我们一般关心`X.Y.0`(稳定版本)，和`X.Y.Z`(补丁版本)的特性。

- 例子
    `v1.14.0` : `1`为主要版本 : 14为次要版本 : `0`为补丁版本

## Kubernetes每个版本的支持周期

Kubernetes项目维护最新三个次要版本的发布分支。结合上述**一个`X.Y.0`版本会在`X.(Y-1).0`版本的3到4个月后出现**的描述，也就是说1年前的版本就不再维护，每个次要版本的维护周期为9~12个月，就算有安全漏洞也不会有补丁版本。



## 新版本和旧版本的区别

新版本与旧版本区别主要在于**应用了社区中经过cherrypick挑选出来的PR以及修复了安全性漏洞、没有workaround(临时解决办法)的bug。** 以下链接中维护了所有当前的发行版的链接，可在此链接中查询相应版本与之前版本的区别: [https://github.com/kubernetes/k](https://github.com/kubernetes/kubernetes/releases)

每个稳定版本之间的release note也可以在kubernetes官网上查阅到: [https://kubernetes.io/docs/setup/release/notes/](https://kubernetes.io/docs/setup/release/notes/) 这其中包括了一些版本升级前必须要确认的事宜，以`v1.14`为例: [https://kubernetes.io/docs/setup/release/notes/#no-really-you-must-read-this-before-you-upgrade](https://kubernetes.io/docs/setup/release/notes/%23no-really-you-must-read-this-before-you-upgrade)



## 新版本对我们开发app调用k8s API接口有什么影响

由于k8s本身是基于api的为服务架构，k8s系统内部也是通过互相调用api来运作的，总体而言kubernetes api在设计时遵循向上和/或向下兼容的原则。

k8s的api是一个api的集合，称之为"API groups"。每一个API group维护着3个主要版本，分别是

* `GA`

* `Beta`

* `Alpha`

API的弃用只会通过在新的`API group`启用的同时宣告旧`API group`将会弃用的方式来推进。

GA版本在宣告启用后将会向下兼容12个月或3个发行版。

Beta版本则为9个月或3个发行版。

而Alpha则会立刻启用。 

这个遵循kubernetes版本的升级规则，也就是整体而言集群升级不支持跨度在2个Final release发行版之上的操作。 每个发行版的release note中也有对API重大改动的描述。开发者们可以参阅其修改API。



## 在生产环境中是否应该尽量使用新版本

从结论上来说，是的。原因也是由于上述的发行版都存在这对应的生命周期。 但值得注意的时，升级集群理论上只支持跨度为2个次要版本的操作。


