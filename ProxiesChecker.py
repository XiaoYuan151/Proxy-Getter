from threading import Thread
from requests import get
from time import sleep

class CheckThread(Thread):
    def __init__(self, num, proxy, url, headers):
        super().__init__()
        self.num = num
        self.proxy = proxy
        self.url = url
        self.headers = headers

    def run(self):
        proxies = {'http': f"http://{self.proxy}", 'https': f"http://{self.proxy}"}
        try:
            response = get(self.url, headers=self.headers, proxies=proxies, timeout=5)
            if response.ok:
                print(f"[{self.num}] Proxy {self.proxy} Alive!")
                self.write_to_file()
        except Exception as e:
            print(f"[{self.num}] Proxy {self.proxy} Dead! Error: {e}")
        finally:
            sleep(5)

    def write_to_file(self):
        with open("proxies.txt", 'a') as file:
            file.write(self.proxy + "\n")
        print(f"[{self.num}] Proxy {self.proxy} Written to File!")

def main():
    try:
        with open("proxies.getter.txt", "r") as file:
            proxies = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("No Proxies Found For Check!")
        return

    url = input("URL for Check (default: https://bing.com): ").strip() or "https://bing.com"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/69.0.3497.100 Safari/537.36'
    }

    print("Creating files...")
    open("proxies.txt", 'w').close()

    threads = []
    alive_proxies = 0

    for num, proxy in enumerate(proxies):
        thread = CheckThread(str(num), proxy, url, headers)
        threads.append(thread)
        thread.start()
        sleep(0.3)

    for thread in threads:
        thread.join()
        if thread.is_alive():
            alive_proxies += 1

    print(f"Discovered Alive Proxies: {alive_proxies}")

if __name__ == '__main__':
    main()
