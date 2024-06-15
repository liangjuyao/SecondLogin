# 广州理工学院 校园网登录

## 使用方法

1. 下载仓库
2. 安装Python3
3. 进入文件夹，打开命令行
4. 安装依赖
   ```pip install -r requirements.txt```
5. 填写账号密码
```python
post_data = {  
    'user_account': ',0,' + '',
    'user_password': '',
}
```
6. 例如
```python
post_data = {  
    'user_account': ',0,' + '学号',
    'user_password': '密码',
}
```

## 打包
可以在项目根目录下控制台输入
```cmd
pyinstaller -D -w -i Windows.ico 校园网.py
```
