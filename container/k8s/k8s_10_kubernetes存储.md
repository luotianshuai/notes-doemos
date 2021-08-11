[TOC]

# 临时存储

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

