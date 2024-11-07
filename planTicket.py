from itertools import filterfalse

import requests
import json

from station import stations

class Planinfo:
    def __init__(self):
        global flag
        flag='1'
        url=self.getUrl()
        plan=self.getData(url,flag)
        self.Print(plan,flag)
    def getUrl(self):
        startflag = False
        endflag = False
        global flag
        flightflag='0'
        while startflag == False:
            start = input("请输入始发地：\n")
            startflag = stations.__contains__(start)
            if startflag == False:
                print('始发地输入错误！')
        while endflag == False:
            end = input("请输入目的地：\n")
            endflag = stations.__contains__(end)
            if endflag == False:
                print('目的地输入错误！')

        self.date = input("请输入日期(格式为xxxx-xx-xx)：\n")
        while flightflag!='1' and flightflag!='2':
            flightflag=input("请选择单程（1）或是往返（2）")
            flag=flightflag
            if flightflag=='1':
                flightway="Oneway"
                flightflag='1'
            elif flightflag=='2':
                flightway="Roundtrip"
                flightflag='2'
            else:print("输入错误")
        url = 'https://flights.ctrip.com/itinerary/api/12808/lowestPrice?flightWay=' \
              +flightway+'&dcity=' \
              + stations[start] + '&acity=' \
              + stations[end] + '&direct=true&army=false'
        return url
    def getData(self,url,flag):
        response = requests.get(url)
        datajson=json.loads(response.text)
        if flag=='1':
            dirt=(datajson["data"])["oneWayPrice"][0]#单程机票数据 字典
            return dirt
        elif flag=='2':
            dirt=(datajson["data"])["roundTripPrice"]#往返机票数据 字典
            return dirt

    def Print(self,dirt,flag):
        if flag=='1':
            print(dirt)
            #for key, value in dirt.items():
            #    print("日期"+key+"   价格"+str(value))
        elif flag=='2':
            print(dirt)
messages=Planinfo()