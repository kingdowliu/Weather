#!/usr/bin/python
#-*-encoding=utf-8-*-
import requests
import json
import itchat
import datetime


def getWeather():
    url='http://t.weather.sojson.com/api/weather/city/101240210'  # 这里将101240210替换成想要查询的城市的代码
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0'}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    # 今日信息
    today = data['data']['forecast'][0]['ymd']
    today_hightem = data['data']['forecast'][0]['high']
    today_lowtem = data['data']['forecast'][0]['low']
    today_win = data['data']['forecast'][0]['fx']+' '+data['data']['forecast'][0]['fl']
    today_wea = data['data']['forecast'][0]['type']
    notice = data['data']['forecast'][0]['notice']

    # 明日信息
    tomorrow = data['data']['forecast'][1]['ymd']
    tomorrow_hightem = data['data']['forecast'][1]['high']
    tomorrow_lowtem = data['data']['forecast'][1]['low']
    tomorrow_win = data['data']['forecast'][1]['fx'] + ' ' + data['data']['forecast'][1]['fl']
    tomorrow_wea = data['data']['forecast'][1]['type']

    # 数据
    today_data = '['+today +']' + '\n    ' + '温度：' + today_hightem  + '/' + today_lowtem + '\n    ' + '天气：' + today_wea + '\n    ' + '风力：' + today_win + '\n\n'
    tomorrow_data = '['+tomorrow +']' + '\n    ' + '温度：' + tomorrow_hightem  + '/' + tomorrow_lowtem + '\n    ' + '天气：' + tomorrow_wea + '\n    ' + '风力：' + tomorrow_win + '\n\n'
    notice = '温馨提醒：' + notice
    info = [today_data, tomorrow_data, notice]

    return info

def run():
    info = []
    info = getWeather()
    
    account = itchat.get_friends(NickName)  # 此处NickName请修改至你需要发送的朋友的微信备注
    for item in account:
        if item['RemarkName'] == NickName:
            user = item['UserName']
            
    # 给自己发送信息，发送至文件传输助手
    itchat.send('【西安天气】\n\n' + info[0] + info[1] + info[2], toUserName='filehelper')
    
    # 给朋友发送信息
    itchat.send('【西安天气】\n\n' + info[0] + info[1] + info[2], toUserName=user)

if __name__=='__main__':
    itchat.auto_login(hotReload=True, enableCmdQR=True)
    while True:
        time = str(datetime.datetime.now().strftime('%H%M%S'))
        if time == '090000':  # 这里自己修改时间，090000代表早上九点整发送
            run()

