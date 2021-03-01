### 江南大学第二课堂自动报名

**简单修改一下参数就能运行，具体如下**

```python
# 使用方式： Cookie Authorization 和 userId 填自己的 登录第二课堂后进入活动中心按F12监听网络就能获取
header = {
    'Authorization': '',  # 填自己的
    'Cookie': '',  # 填自己的
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'
}

query_param = {
    'hdmc': '',
    'orgId': '',
    'size': '10',
    'page': '1',
    'userId': '',  # 学号
    'xyId': '12200',
    'grade': '2018',  # 年级
    'type': '5'  # 参数说明 1：预热中 2：招募中 3：进行中 4：已结束 5：全部活动
}
```

