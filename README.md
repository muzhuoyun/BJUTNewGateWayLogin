# 北工大新网关认证脚本

## 用法

### 1. 填入信息
在 `context.py` 中填入学号和密码信息：
```python
UserAccount = '替换为学号'
UserPassWord = '替换为密码'
```
### 2. 使用有线网登录网关
```shell
python3 mainLan.py -t 认证类型（ipv6&ipv4、ipv6、ipv4三种类型可选。）
```
或者
```cmd
python mainLan.py -t 认证类型
```

### 3. 使用有线网登出网关
```shell
python3 mainLan.py --logout
```
或者
```cmd
python mainLan.py --logout
```

### 4. 在宿舍使用WIFI登录网关
```shell
python3 mainWlan.py -t 认证类型（ipv6&ipv4、ipv6两种类型可选，因为暂时没有找到ipv4认证的接口或者方案。）
```
或者
```cmd
python mainWLan.py -t 认证类型
```

### 5. 在宿舍使用WIFI登出网关
```shell
python3 mainWlan.py --logout
```
或者
```cmd
python mainWLan.py --logout
```