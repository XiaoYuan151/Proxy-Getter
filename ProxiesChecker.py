from threading import Thread
from time import sleep

from requests import get


class CheckThread(Thread):
    def __init__(self, num, proxy):
        Thread.__init__(self)
        self.num = num
        self.proxy = proxy

    def run(self):
        proxies = {'http': "http://" + self.proxy, 'https': "http://" + self.proxy}
        try:
            get(url, headers=headers, proxies=proxies)
        except:
            print(f"[{self.num}] Proxy Dead!")
            sleep(5)
        else:
            global alive
            print(f"[{self.num}] Proxy Alive!")
            print(f"[{self.num}] Writing into files...")
            file = open("proxies.txt", 'a')
            if not file.write(self.proxy) == 0:
                print(f"[{self.num}] Proxy Write Success!")
                file.close()
            else:
                print(f"[{self.num}] Proxy Write With Error!")
                file.close()
            alive = alive + 1
            sleep(5)


if __name__ == '__main__':
    try:
        txt = open("proxies.getter.txt").readlines()
    except:
        print("No Proxies Found For Check!")
    else:
        num = 0
        alive = 0
        url = input("Url For Check (https://bing.com):")
        if url == "":
            url = "https://bing.com"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/69.0.3497.100'
                          'Safari/537.36'
        }
        print("Creating files...")
        file = open("proxies.txt", 'w')
        file.close()
        for proxy in txt:
            thread = CheckThread(str(num), proxy)
            thread.start()
            num = num + 1
            sleep(0.3)
        print(f"Discovered Alive Proxy {alive}")
