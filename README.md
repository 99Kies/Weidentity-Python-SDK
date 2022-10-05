# Weidentity-Python-SDK
Weidentity-Python-SDK
## 支持版本
Python3.6+

## 环境配置
- CentOS/Ubuntu	7.2 / 16.04，64位	部署 RestServer 用
- JDK	1.8+	推荐使用 1.8u141 及以上
- FISCO-BCOS 节点	1.3.8（即中央仓库的1.2.5）或 2.x	确保它可以和部署 Server 机器互相连通，可 telnet 其 channelPort 端口
- Gradle	4.6+	同时支持 4.x 和 5.x 版本的 Gradle
- MySQL	5 +	需要MySQL存储必要的链上数据进行缓存
- Python 3 调用 weidentity sdk
## FISCO BCOS 链
[请食用官网最新部署文档](https://fisco-bcos-documentation.readthedocs.io/zh_CN/latest/docs/installation.html)
## 部署 Weidentity 合约
[请食用官网最新部署文档](https://weidentity.readthedocs.io/zh_CN/latest/docs/weidentity-installation-by-web.html)
## 部署 Weidentity Rest Serivce
[请食用官网最新部署文档](https://weidentity.readthedocs.io/zh_CN/latest/docs/weidentity-rest-deploy.html)
部署成功之后，rest service接口成功暴露在 <http://ip:6001>，自此我们的环境就搭建完成了。

<hr style=" border:solid; width:100px; height:1px;" color=#000000 size=1">


## How to use

1. 下载weidentity python sdk
```bash
pip install pyweidentity
```

2. 托管模式示例
```python
from pyweidentity.weidentityService import weidentityService

URL = "http://192.168.80.144:6001"
# WeIdentity RestService URL

weid = weidentityService(URL)
create_weid = weid.create_weidentity_did()
print(create_weid)
```


3. 轻客户端模式示例
```python
from pyweidentity.weidentityClient import weidentityClient
import random

URL = "http://192.168.80.144:6001"
# WeIdentity RestService URL

weid = weidentityClient(URL)
privKey = "0xc4a116fb87ae9b8b87842b0f46e1bbf71c37fdae1104fd6d3fd2041e23c8c68e"
nonce = str(random.randint(1, 999999999999999999999999999999))
create_weid = weid.create_weidentity_did(privKey, nonce)
print(create_weid)
```