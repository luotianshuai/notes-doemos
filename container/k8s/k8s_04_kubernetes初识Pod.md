[TCO]

# Node资源介绍

Node是kubernetes的节点，根据节点类型可以分为slave和master节点，slave节点统一由master管理

```
kubectl get nodes                 # 查看nodes简要信息
kubectl get nodes -o wide         # 查看nodes的扩展信息
kubectl describe nodes            # 查看nodes的详细信息
kubectl get nodes cka01 -o yaml   # 获取某个特定节点的信息并用yaml展示出来


kubectl describe nodes cka01      # 获取nodes详细信息需要关注的几个点
Conditions:
  Type                 Status .....  Reason                       Message
  ----                 ------ .....  ------                       -------
  NetworkUnavailable   False  .....  CalicoIsUp                   Calico is running on this node
  MemoryPressure       False  .....  KubeletHasSufficientMemory   kubelet has sufficient memory available
  DiskPressure         False  .....  KubeletHasNoDiskPressure     kubelet has no disk pressure
  PIDPressure          False  .....  KubeletHasSufficientPID      kubelet has sufficient PID available
  Ready                True   .....  KubeletReady                 kubelet is posting ready status. AppArmor enabled
  
  网络是否有异常、内存是否有充足、硬盘是否有压力、Pid是否充足、是否准备就绪



Capacity: # 当前节点的容量
  cpu:                2
  ephemeral-storage:  41151808Ki
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  memory:             4045784Ki
  pods:               110
Allocatable:  # 当前节点还可以分配多少资源
  cpu:                2
  ephemeral-storage:  37925506191
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  memory:             3943384Ki
  pods:               110
  
  
  # 事件是我们经常拍错的时候需要看的，比如说我现在创建了一个应用，如果我这个应用是在我执行kubect创建到它running之前出的问题
  # 比如说节点资源不够或者它的镜像下载失败
  # 这一部分的内容会以事件形式提示出来
  Events:
  Type    Reason                   Age                    From        Message
  ----    ------                   ----                   ----        -------
  Normal  Starting                 45h                    kubelet     Starting kubelet.
  Normal  NodeAllocatableEnforced  45h                    kubelet     Updated Node Allocatable limit across pods
  Normal  NodeHasSufficientMemory  45h                    kubelet     Node cka01 status is now: NodeHasSufficientMemory
  Normal  NodeHasSufficientPID     45h                    kubelet     Node cka01 status is now: NodeHasSufficientPID
  Normal  NodeHasNoDiskPressure    45h                    kubelet     Node cka01 status is now: NodeHasNoDiskPressure
  
  
  # 如果你已经running起来了这个时候报错，它属于应用的报错
```

