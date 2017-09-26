import requests
import telnetlib
import time
import json


dic  = {"1f10023":"192.168.1.1:10023","1f10026":"192.168.1.1:10026","2f10023":"192.168.1.2:10023","2f10026":"192.168.1.2:10026"}

def check():
    payload = []
    ts = int(time.time())
    for point in dic:
         ip = str(dic[point].split(':')[0])
         port = int(dic[point].split(':')[1])
         try:
             tn = telnetlib.Telnet(ip, port, timeout=3)
             time.sleep(0.5)
             print 'ok'
             tn.close()
             getdata = {
            "endpoint": "rpnsfront",
            "metric":  point,
            "timestamp": ts,
            "step": 60,
            "value": 1,
            "counterType": "GAUGE",
            "tags": "idc=yidong,loc=nanjing",
             }

         except  Exception as e:
             print e
             getdata = {
                 "endpoint": "rpnsfront",
                 "metric": point,
                 "timestamp": ts,
                 "step": 60,
                 "value": -1,
                 "counterType": "GAUGE",
                 "tags": "idc=yidong,loc=nanjing",
                 }

         payload.append(getdata)
    r = requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(payload))
    print r.text
if __name__ == "__main__":
    check()
