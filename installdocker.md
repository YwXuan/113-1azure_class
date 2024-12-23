# Install Docker on Ubuntu 20.04 VM _2024.12.23

## 官方版本

### 移除舊版 Docker
```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

### Add Docker's official GPG key
```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

### Add the repository to Apt sources
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```


# 查看 doker images
```bash
sudo docker images

```

# 下載unbuntu20.04
```bash
sudo docker pull ubuntu:20.04
```

# 把 image 檔案放到容器
``` bash 
sudo docker run -t -i ubuntu:20.04 /bin/bash

```
## 不停止退出容器
使用鍵盤組合鍵 `Ctrl-p` 以及 `Ctrl-q` 來退出容器而不停止。

## 外面終止容器
使用以下命令停止容器：
```bash
sudo docker stop [CONTAINER ID]
```

## 重新開啟容器
使用以下命令重新啟動容器：
```bash
sudo docker restart [CONTAINER ID]
```

## 找 image
在 Docker Hub 上查找映像：[Docker Hub](https://hub.docker.com/)

## 分組
安裝 `nano` 編輯器並將用戶添加到 docker 組：
```bash
sudo apt install nano
sudo nano /etc/group
```
找到 `docker` 組並加入使用者。

## 以分離模式啟動容器
使用以下命令啟動容器：
```bash
docker run -idt [IMAGE_NAME]
```



