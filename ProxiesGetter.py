from requests import get
from json import loads
import re
import os

def save_proxies(url):
    try:
        http = get(url).text
    except Exception as e:
        print(f"Proxies Get With Error from {url}: {e}")
        return

    if not http:
        print(f"No proxies retrieved from {url}")
        return

    # 正则表达式用于提取 IP 地址
    ips = re.findall(r'\d+\.\d+\.\d+\.\d+', http)

    if not ips:
        print(f"No proxies found in the response from {url}")
        return

    try:
        with open("proxies.getter.txt", 'w') as file:
            for ip in ips:
                file.write(ip + '\n')
        print(f"Proxies retrieved from {url} successfully")
    except Exception as e:
        print(f"Error writing proxies from {url} to file: {e}")

def main():
    urls = [
        "https://www.89ip.cn/tqdl.html?api=1&num=9999",
        "https://www.docip.net/data/free.json",
        "http://www.69ip.cn/php.69ip.cn.php?quantity=9999",
        "http://pubproxy.com/api/proxy?limit=5",
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "https://spys.me/proxy.txt"
    ]

    # 删除旧的文件
    try:
        os.remove("proxies.getter.txt")
        print("Old file deleted successfully")
    except Exception as e:
        print(f"Error deleting old file: {e}")

    for url in urls:
        save_proxies(url)

if __name__ == "__main__":
    main()
