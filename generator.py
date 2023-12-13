import requests
import httpx
import random
import time
from threading import Thread
import sys
import os
import requests
from tls_client import Session
class Generator:
        def __init__(self, Chat, Proxy):
                self.IP, self.Port = Proxy[0], int(Proxy[1])
                self.Connect()
        def save_id(self, newid):
            ids = open("ids.txt", "a+")
            ids.write(newid + "\n")
            ids.close()
        def Connect(self):
            proxy_log = {
                "http://": f"http://{self.IP}:{self.Port}", "https://": f"http://{self.IP}:{self.Port}"
            }
            try:
                url = "https://xat.com/web_gear/chat/auser3.php"
                response = httpx.get(url, proxies=proxy_log, timeout=10)
           
                if response.status_code == 200:
                    newid = response.text
                    print(newid)
                    self.save_id(newid)
                else:
                    time.sleep(1)
            except httpx.ProxyError:
                pass
            except httpx.ReadError:
                pass
            except httpx.ConnectTimeout:
                pass
            except httpx.ReadTimeout:
                pass
            except httpx.ConnectError:
                pass
            except httpx.ProtocolError:
                pass
            except:
                try:
                    print("Protocol Error") 
                except: 
                    pass
                
        
class init:
        def save_proxies(self, proxies):
            with open("proxies.txt", "w") as file:
                file.write("\n".join(proxies))

        def get_proxies(self):
            try:
                url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"
                response = requests.get(url, allow_redirects=True)

                if response.status_code == 200:
                    proxies = response.text.splitlines()
                    self.save_proxies(proxies)
                else:
                    time.sleep(1)
                    self.get_proxies()
            except:
                  exit()

        def check_proxies_file(self):
            self.get_proxies()
                
        def Stop(self):
                exit()
                
        def Start(self):
                #self.check_proxies_file()
                Proxies = open('proxies.txt', 'r').read() 
                Proxies = Proxies.split('\n')
                Chat = 1
                for Proxy in Proxies:
                    Proxy = Proxy.split(':')
                    Raid = Thread(target=Generator,args=(Chat, Proxy))
                    Raid.daemon = True
                    try:
                        Raid.start()
                    except: 
                        print("Protocol Error")
obj = init()
while True:
    obj.Start()

     
