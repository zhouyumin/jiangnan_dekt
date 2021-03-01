# @Time : 2020/10/30 8:32 
# @Author : zym
# @File : second_course.py 
# @Software: PyCharm
import requests

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


def signup():
    session = requests.session()
    res = session.request(method='get', url='http://dekt.jiangnan.edu.cn/biz/activity/student/list', params=query_param,
                          headers=header)
    res.encoding = res.apparent_encoding
    data = res.json()
    for each in data['data']['list']:
        print('活动id:' + each['id'])
        print('活动名称:' + each['hdmc'])
        print('活动地点:' + each['hddd'])
        print('学时:' + str(each['xs']))
        print('招募人数:' + str(each['zmrs']))
        print('报名人数:' + str(each['bmrs']))
        print('报名开始时间:' + each['bmkssj'])
        print('报名结束时间:' + each['bmjssj'])
        print('开始时间:' + each['kssj'])
        print('结束时间:' + each['jssj'])
        print('开始自动报名')
        res = session.post('http://dekt.jiangnan.edu.cn/biz/activity/signup', json={'id': each['id']}, headers=header)
        print(res.text)


if __name__ == '__main__':
    signup()
