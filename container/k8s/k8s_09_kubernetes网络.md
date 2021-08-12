[TOC]

# Service

Pod是有生命周期的，它们可以被创建、也可以被销毁，然而一旦它们被销毁生命就永远结束。通过Deployment and ReplicationsSet能够创建pods并控制副本数量，每个Pod都会获取它自己的IP地址，当进行副本迁移、扩缩容的时候IP会发生变化

kubernetes Server定义了这样一种抽象：通过Selector将Pod进行逻辑分组，并指定访问他们的策略使这一组Pod能够被Service访问

## service类型

* ClusterIP：通过集群的内部IP暴露服务，选择改制，服务职能在集群访问，这也是默认的
* NodePort：通过给每个Node上的IP和静态端口暴露服务，NodePort服务会路由到ClusterIP服务，这个ClusterIP服务会自动创建。通过请求<NodeIP>:<NodePort>，可以从集群外部访问一个NodePort服务，默认NodePort端口范围是：30000-32767，如果需要修改则在apiserver的启动命令里添加如下参数-service-node-port-range=1~65535
* LoadBalancer: 使用云提供的负载均衡器，可以向外暴露服务，外部的负载均衡器可以路由到NodePort服务和ClusterIP服务
* ExternalName: 此模式主要面向运行在集群外部的服务，通过它可以将外部的服务映射到K8s集群，且具备k8s内服务的一些特征（如具备namespace等属性），来为集群内部提供服务，此模式要求kube-dns的版本为1.7或以上。这种模式和前三种模式（除了HEADLESS SERVICE）最大的不同是重定向依赖的是dns层次，而不是kube-proxy



ClusterIP只能被内部访问

NodePort对外暴露端口相对危险

LoadBalancer这个是使用云提供商的自建的就没有



我们创建了service后，proxy监听到创建了service，写上对应的路由规则，实现路由的转发

## service的代理模式

### iptables

iptables代理模式

在这种模式下，kube-proxy监听Kubernetes控制节点添加和删除Service的Endpoint对象，对于每个服务，它都安装iptables规则，该规则捕获到服务ClusterIP的Port流量，并将该流量重定向到服务器的后端之一，对于每个Endpoint对象，它将安装iptables规则，该规则选择一个后端Pod

默认情况下，iptables模式下的kube-proxy会回见选择一个后端

优点：
* kube-proxy制作规则创建和同步减少kube-proxy压力
* 流量转发由内核的netiux netfiter处理，而无需在用户空间和内核空间之前切换性能更强

缺点:
在大规模集群下，随着service的数量越来越多iptables规则成倍增长，大量规则同时也会产生一些问题

* iptables规则匹配延时：因为iptables采用的线性匹配即匹配因给数据进行线性的遍历整个规则集知道匹配否则退出，这种带来的问题就是，当iptables过大的时候性能会急速下降，因为相应的匹配延时会增加
* iptables规则更新延时：在实际使用过程中不断创建sergvice，修改service，删除service，这其实也转换成对iptables的不断修改，因为iptables是非增量更新，也就意味着，你上述操作它都是把全部规则复制出来，然后在修改，修改完在赋值回去而这个过程还会锁表
* QPS抖动问题：kube-proxy会周期性的更新iptables规则，大量的iptables规则更新会花很长时间，期间回缩表造成qps抖动

### ipvs

IPVS代理模式

在ipvs模式下，kube-proxy监控kubernetes服务和断电，调用netlink端口以相应的创建IPVS规则，并定期将IPVS规则与Kubernetes服务和端点同步。改控制循环可以确保IPVS状态与所需状态匹配。访问服务时，IPVS将流量定向到后端Pod之一

IPVS代理模式基于类似iptables模式的netfilter挂钩函数，但是使用哈希表作为基础的数据结构，并在内核空间中工作，这意味着，与iptables模式下的kube-proxy相比，IPVS模式下的kube-proxy可以以更低的延迟重定向流量，兵器在同步代理规则的时候具有更好的性能。与其他代理模式相比，IPVS模式还支持更高的网络吞吐量

IPVS主要有三种模式: 
* DR模式：调度器LB直接修改报文的目的MAC地址为后端真实服务器地址，服务器响应处理后的报文无需经过调度LB直接返回给客户端，这种模式也是性能最好的
* TUN模式：LB接收到客户请求包，进行ip Tunnel封装。即在原有的包头加上IP Tunnel的包头。然后发给后端真实服务器，真实的服务器将响应处理后的数据直接发给客户端
* NAT模式： LB接收到客户端的请求报文修改目的IP地址为后端真实服务器IP地址另外也修改后端服务器发过来的响应包围源IP地址。kube-proxy的IPVS模式用的NAT模式因为DR,TUN模式都不支持端口映射

IPVS提供了更多算法来平衡后端Pod的流量:
* rr： 轮训
* lc：链接数最小（打开的链接最少）
* dh：目标哈希
* sh：源哈希
* sed：最短预期延迟
* nq：永不排队

## service练习

### ClusterIP

```yaml
apiVersion: v1
kind: Service
metadata:
  name: webserver
spec:
  type: ClusterIP
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: nginx-c    # service是通过标签来选择pod
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx-c
  strategy:
   type: RollingUpdate
   rollingUpdate:
     maxSurge: 25%
     maxUnavailable: 0
  template:
    metadata:
      labels:
        app: nginx-c
    spec:
      containers:
        - name: nginx1
          image: nginx:1.10
          imagePullPolicy: IfNotPresent
          ports:
            - name: web            # 端口映射命名
              containerPort: 80    # 声明容器端口
              protocol: TCP        # 声明协议
          livenessProbe:
            tcpSocket:
              port: 80
```



```
root@cka001:~/yaml/service# kubectl get endpoints
endpoints                        endpointslices.discovery.k8s.io
root@cka001:~/yaml/service# kubectl get endpoints
NAME         ENDPOINTS                                               AGE
kubernetes   172.24.238.8:6443                                       2d
webserver    192.168.102.30:80,192.168.112.22:80,192.168.112.23:80   78s
root@cka001:~/yaml/service# kubectl get svc
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP   2d
webserver    ClusterIP   10.110.188.120   <none>        80/TCP    2m22s
```

* 扩容后endpoints就会自动跟新，同样是根据selector获取pod的ip

## nodePort

```yaml
apiVersion: v1
kind: Service
metadata:
  name: webserver
spec:
  type: NodePort
  ports:
  - name: http
    port: 80
    nodePort: 30080
    protocol: TCP
    targetPort: 80
  selector:
    app: nginx-c
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx-c
  strategy:
   type: RollingUpdate
   rollingUpdate:
     maxSurge: 25%
     maxUnavailable: 0
  template:
    metadata:
      labels:
        app: nginx-c
    spec:
      containers:
        - name: nginx1
          image: nginx:1.10
          imagePullPolicy: IfNotPresent
          ports:
            - name: web            # 端口映射命名
              containerPort: 80    # 声明容器端口
              protocol: TCP        # 声明协议
          livenessProbe:
            tcpSocket:
              port: 80

```

## 总结

service是4层的转发IP:端口，也可以对外提供访问但是有个问题就是

* 如果使用nodeportPod多的情况下很快被用光
* 安全隐患

解决办法: ingress

# ingress

ingress是一个API对象，用于集中管理集群服务的外部访问，通常是HTTP

kubernetes中应用七层负载的实现，可以通过创建ingress实现针对URL、path、ssl的请求转发

必须有一个ingress Controller才能使ingress生效。否则创建ingress资源无效

ingress-controller会运行一个Pod副本，这个pod里面的容器安装了反向代理软件，通过读取添加的Server，动态生成负载均衡器的反向代理配置，添加对应的ingress服务后，里面的规则包含了对应规则，里面有域名和对应的Service-backend



目前使用最多的是ingress-nginx



## 部署ingress

```
git clone https://github.com/kubernetes/ingress-nginx.git
rsync -avgp ingress-nginx/deploy/static/provider/kind/deploy.yaml .
```



```yaml

apiVersion: v1
kind: Namespace
metadata:
  name: ingress-nginx
  labels:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx

---
# Source: ingress-nginx/templates/controller-serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  labels:
    helm.sh/chart: ingress-nginx-3.35.0
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/version: 0.48.1
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: controller
  name: ingress-nginx
  namespace: ingress-nginx
automountServiceAccountToken: true
---
# Source: ingress-nginx/templates/controller-configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  labels:
    helm.sh/chart: ingress-nginx-3.35.0
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/version: 0.48.1
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: controller
  name: ingress-nginx-controller
  namespace: ingress-nginx
data:
---
# Source: ingress-nginx/templates/clusterrole.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  labels:
    helm.sh/chart: ingress-nginx-3.35.0
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/version: 0.48.1
    app.kubernetes.io/managed-by: Helm
  name: ingress-nginx
rules:
  - apiGroups:
      - ''
    resources:
      - configmaps
      - endpoints
      - nodes
      - pods
      - secrets
    verbs:
      - list
      - watch
  - apiGroups:
      - ''
    resources:
      - nodes
    verbs:
      - get
  - apiGroups:
      - ''
    resources:
      - services
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - extensions
      - networking.k8s.io   # k8s 1.14+
    resources:
      - ingresses
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - ''
    resources:
      - events
    verbs:
      - create
      - patch
  - apiGroups:
      - extensions
      - networking.k8s.io   # k8s 1.14+
    resources:
      - ingresses/status
    verbs:
      - update
  - apiGroups:
      - networking.k8s.io   # k8s 1.14+
    resources:
      - ingressclasses
    verbs:
      - get
      - list
      - watch
---
# Source: ingress-nginx/templates/clusterrolebinding.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  labels:
    helm.sh/chart: ingress-nginx-3.35.0
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/version: 0.48.1
    app.kubernetes.io/managed-by: Helm
  name: ingress-nginx
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: ingress-nginx
subjects:
  - kind: ServiceAccount
    name: ingress-nginx
    namespace: ingress-nginx
---
# Source: ingress-nginx/templates/controller-role.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  labels:
    helm.sh/chart: ingress-nginx-3.35.0
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/version: 0.48.1
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: controller
  name: ingress-nginx
  namespace: ingress-nginx
rules:
  - apiGroups:
      - ''
    resources:
      - namespaces
    verbs:
      - get
  - apiGroups:
      - ''
    resources:
      - configmaps
      - pods
      - secrets
      - endpoints
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - ''
    resources:
      - services
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - extensions
      - networking.k8s.io   # k8s 1.14+
    resources:
      - ingresses
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - extensions
      - networking.k8s.io   # k8s 1.14+
    resources:
      - ingresses/status
    verbs:
      - update
  - apiGroups:
      - networking.k8s.io   # k8s 1.14+
    resources:
      - ingressclasses
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - ''
    resources:
      - configmaps
    resourceNames:
      - ingress-controller-leader-nginx
    verbs:
      - get
      - update
  - apiGroups:
      - ''
    resources:
      - configmaps
    verbs:
      - create
  - apiGroups:
      - ''
    resources:
      - events
    verbs:
      - create
      - patch
---
# Source: ingress-nginx/templates/controller-rolebinding.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  labels:
    helm.sh/chart: ingress-nginx-3.35.0
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/version: 0.48.1
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: controller
  name: ingress-nginx
  namespace: ingress-nginx
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: ingress-nginx
subjects:
  - kind: ServiceAccount
    name: ingress-nginx
    namespace: ingress-nginx
---
# Source: ingress-nginx/templates/controller-service-webhook.yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    helm.sh/chart: ingress-nginx-3.35.0
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/version: 0.48.1
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: controller
  name: ingress-nginx-controller-admission
  namespace: ingress-nginx
spec:
  type: ClusterIP
  ports:
    - name: https-webhook
      port: 443
      targetPort: webhook
  selector:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/component: controller
---
# Source: ingress-nginx/templates/controller-service.yaml
apiVersion: v1
kind: Service
metadata:
  annotations:
  labels:
    helm.sh/chart: ingress-nginx-3.35.0
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/version: 0.48.1
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: controller
  name: ingress-nginx-controller
  namespace: ingress-nginx
spec:
  type: NodePort
  ports:
    - name: http
      port: 80
      protocol: TCP
      targetPort: http
    - name: https
      port: 443
      protocol: TCP
      targetPort: https
  selector:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/component: controller
---
# Source: ingress-nginx/templates/controller-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    helm.sh/chart: ingress-nginx-3.35.0
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/version: 0.48.1
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: controller
  name: ingress-nginx-controller
  namespace: ingress-nginx
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: ingress-nginx
      app.kubernetes.io/instance: ingress-nginx
      app.kubernetes.io/component: controller
  revisionHistoryLimit: 10
  strategy:
    rollingUpdate:
      maxUnavailable: 1
    type: RollingUpdate
  minReadySeconds: 0
  replicas: 2
  template:
    metadata:
      labels:
        app.kubernetes.io/name: ingress-nginx
        app.kubernetes.io/instance: ingress-nginx
        app.kubernetes.io/component: controller
    spec:
      dnsPolicy: ClusterFirst
      containers:
        - name: controller
          image: k8s.gcr.io/ingress-nginx/controller:v0.48.1@sha256:e9fb216ace49dfa4a5983b183067e97496e7a8b307d2093f4278cd550c303899
          imagePullPolicy: IfNotPresent
          lifecycle:
            preStop:
              exec:
                command:
                  - /wait-shutdown
          args:
            - /nginx-ingress-controller
            - --election-id=ingress-controller-leader
            - --ingress-class=nginx
            - --configmap=$(POD_NAMESPACE)/ingress-nginx-controller
            - --validating-webhook=:8443
            - --validating-webhook-certificate=/usr/local/certificates/cert
            - --validating-webhook-key=/usr/local/certificates/key
            - --publish-status-address=localhost
          securityContext:
            capabilities:
              drop:
                - ALL
              add:
                - NET_BIND_SERVICE
            runAsUser: 101
            allowPrivilegeEscalation: true
          env:
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: POD_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
            - name: LD_PRELOAD
              value: /usr/local/lib/libmimalloc.so
          livenessProbe:
            failureThreshold: 5
            httpGet:
              path: /healthz
              port: 10254
              scheme: HTTP
            initialDelaySeconds: 10
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          readinessProbe:
            failureThreshold: 3
            httpGet:
              path: /healthz
              port: 10254
              scheme: HTTP
            initialDelaySeconds: 10
            periodSeconds: 10
            successThreshold: 1
            timeoutSeconds: 1
          ports:
            - name: http
              containerPort: 80
              protocol: TCP
              hostPort: 80
            - name: https
              containerPort: 443
              protocol: TCP
              hostPort: 443
            - name: webhook
              containerPort: 8443
              protocol: TCP
          volumeMounts:
            - name: webhook-cert
              mountPath: /usr/local/certificates/
              readOnly: true
          resources:
            requests:
              cpu: 100m
              memory: 90Mi
      nodeSelector:
        ingress-node: 'true'
      hostNetwork: true
      tolerations:
        - effect: NoSchedule
          key: node-role.kubernetes.io/master
          operator: Equal
      serviceAccountName: ingress-nginx
      terminationGracePeriodSeconds: 0
      volumes:
        - name: webhook-cert
          secret:
            secretName: ingress-nginx-admission
---
# Source: ingress-nginx/templates/admission-webhooks/validating-webhook.yaml
# before changing this value, check the required kubernetes version
# https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#prerequisites
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  labels:
    helm.sh/chart: ingress-nginx-3.35.0
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/version: 0.48.1
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: admission-webhook
  name: ingress-nginx-admission
webhooks:
  - name: validate.nginx.ingress.kubernetes.io
    matchPolicy: Equivalent
    rules:
      - apiGroups:
          - networking.k8s.io
        apiVersions:
          - v1beta1
        operations:
          - CREATE
          - UPDATE
        resources:
          - ingresses
    failurePolicy: Fail
    sideEffects: None
    admissionReviewVersions:
      - v1
      - v1beta1
    clientConfig:
      service:
        namespace: ingress-nginx
        name: ingress-nginx-controller-admission
        path: /networking/v1beta1/ingresses
---
# Source: ingress-nginx/templates/admission-webhooks/job-patch/serviceaccount.yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: ingress-nginx-admission
  namespace: ingress-nginx
  annotations:
    helm.sh/hook: pre-install,pre-upgrade,post-install,post-upgrade
    helm.sh/hook-delete-policy: before-hook-creation,hook-succeeded
  labels:
    helm.sh/chart: ingress-nginx-3.35.0
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/version: 0.48.1
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: admission-webhook
---
# Source: ingress-nginx/templates/admission-webhooks/job-patch/clusterrole.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: ingress-nginx-admission
  annotations:
    helm.sh/hook: pre-install,pre-upgrade,post-install,post-upgrade
    helm.sh/hook-delete-policy: before-hook-creation,hook-succeeded
  labels:
    helm.sh/chart: ingress-nginx-3.35.0
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/version: 0.48.1
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: admission-webhook
rules:
  - apiGroups:
      - admissionregistration.k8s.io
    resources:
      - validatingwebhookconfigurations
    verbs:
      - get
      - update
---
# Source: ingress-nginx/templates/admission-webhooks/job-patch/clusterrolebinding.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: ingress-nginx-admission
  annotations:
    helm.sh/hook: pre-install,pre-upgrade,post-install,post-upgrade
    helm.sh/hook-delete-policy: before-hook-creation,hook-succeeded
  labels:
    helm.sh/chart: ingress-nginx-3.35.0
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/version: 0.48.1
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: admission-webhook
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: ingress-nginx-admission
subjects:
  - kind: ServiceAccount
    name: ingress-nginx-admission
    namespace: ingress-nginx
---
# Source: ingress-nginx/templates/admission-webhooks/job-patch/role.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: ingress-nginx-admission
  namespace: ingress-nginx
  annotations:
    helm.sh/hook: pre-install,pre-upgrade,post-install,post-upgrade
    helm.sh/hook-delete-policy: before-hook-creation,hook-succeeded
  labels:
    helm.sh/chart: ingress-nginx-3.35.0
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/version: 0.48.1
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: admission-webhook
rules:
  - apiGroups:
      - ''
    resources:
      - secrets
    verbs:
      - get
      - create
---
# Source: ingress-nginx/templates/admission-webhooks/job-patch/rolebinding.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: ingress-nginx-admission
  namespace: ingress-nginx
  annotations:
    helm.sh/hook: pre-install,pre-upgrade,post-install,post-upgrade
    helm.sh/hook-delete-policy: before-hook-creation,hook-succeeded
  labels:
    helm.sh/chart: ingress-nginx-3.35.0
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/version: 0.48.1
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: admission-webhook
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: ingress-nginx-admission
subjects:
  - kind: ServiceAccount
    name: ingress-nginx-admission
    namespace: ingress-nginx
---
# Source: ingress-nginx/templates/admission-webhooks/job-patch/job-createSecret.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: ingress-nginx-admission-create
  namespace: ingress-nginx
  annotations:
    helm.sh/hook: pre-install,pre-upgrade
    helm.sh/hook-delete-policy: before-hook-creation,hook-succeeded
  labels:
    helm.sh/chart: ingress-nginx-3.35.0
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/version: 0.48.1
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: admission-webhook
spec:
  template:
    metadata:
      name: ingress-nginx-admission-create
      labels:
        helm.sh/chart: ingress-nginx-3.35.0
        app.kubernetes.io/name: ingress-nginx
        app.kubernetes.io/instance: ingress-nginx
        app.kubernetes.io/version: 0.48.1
        app.kubernetes.io/managed-by: Helm
        app.kubernetes.io/component: admission-webhook
    spec:
      containers:
        - name: create
          image: docker.io/jettech/kube-webhook-certgen:v1.5.1
          imagePullPolicy: IfNotPresent
          args:
            - create
            - --host=ingress-nginx-controller-admission,ingress-nginx-controller-admission.$(POD_NAMESPACE).svc
            - --namespace=$(POD_NAMESPACE)
            - --secret-name=ingress-nginx-admission
          env:
            - name: POD_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
      restartPolicy: OnFailure
      serviceAccountName: ingress-nginx-admission
      securityContext:
        runAsNonRoot: true
        runAsUser: 2000
---
# Source: ingress-nginx/templates/admission-webhooks/job-patch/job-patchWebhook.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: ingress-nginx-admission-patch
  namespace: ingress-nginx
  annotations:
    helm.sh/hook: post-install,post-upgrade
    helm.sh/hook-delete-policy: before-hook-creation,hook-succeeded
  labels:
    helm.sh/chart: ingress-nginx-3.35.0
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/version: 0.48.1
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/component: admission-webhook
spec:
  template:
    metadata:
      name: ingress-nginx-admission-patch
      labels:
        helm.sh/chart: ingress-nginx-3.35.0
        app.kubernetes.io/name: ingress-nginx
        app.kubernetes.io/instance: ingress-nginx
        app.kubernetes.io/version: 0.48.1
        app.kubernetes.io/managed-by: Helm
        app.kubernetes.io/component: admission-webhook
    spec:
      containers:
        - name: patch
          image: docker.io/jettech/kube-webhook-certgen:v1.5.1
          imagePullPolicy: IfNotPresent
          args:
            - patch
            - --webhook-name=ingress-nginx-admission
            - --namespace=$(POD_NAMESPACE)
            - --patch-mutating=false
            - --secret-name=ingress-nginx-admission
            - --patch-failure-policy=Fail
          env:
            - name: POD_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
      restartPolicy: OnFailure
      serviceAccountName: ingress-nginx-admission
      securityContext:
        runAsNonRoot: true
        runAsUser: 2000
```

### 注意事项

* 修改了nodeSelector
* 修改为hostNetwork模式占用宿主80和443

```
    Ports:         80/TCP, 443/TCP, 8443/TCP
    Host Ports:    80/TCP, 443/TCP, 8443/TCP
```

## 使用ingress

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: webserver
spec:
  rules:
  - host: www.example.com
    http:
      paths:
      - backend:
          service:
            name: webserver
            port:
              number: 80
        path: /
        pathType: Prefix
---
apiVersion: v1
kind: Service
metadata:
  name: webserver
spec:
  type: ClusterIP
  ports:
  - name: http
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: nginx-c
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx-c
  strategy:
   type: RollingUpdate
   rollingUpdate:
     maxSurge: 25%
     maxUnavailable: 0
  template:
    metadata:
      labels:
        app: nginx-c
    spec:
      containers:
        - name: nginx1
          image: nginx:1.10
          imagePullPolicy: IfNotPresent
          ports:
            - name: web            # 端口映射命名
              containerPort: 80    # 声明容器端口
              protocol: TCP        # 声明协议
          livenessProbe:
            tcpSocket:
              port: 80
```

## service和ingress的关系

