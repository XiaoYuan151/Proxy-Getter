from json import loads

from requests import get

file = open("../proxies.getter.txt", 'w')
http = get("https://www.89ip.cn/tqdl.html?api=1&num=9999").text
if http == "":
    print("[0] Proxies Get With Error!")
else:
    if not file.write(http.replace(
            "<a href=\"https://proxy.ip3366.net/\" target=\"_blank\" data-type=\"img\"><img src=\"img/hfad.png\"></a><br><script type=\"text/javascript\" src=\"js/jquery.min.js\"></script>\n<div id=\"adarea\"onclick=location.href='https://proxy.ip3366.net/' style=\"cursor: pointer;display: none;position: fixed;right:15px;bottom:15px;width: 285px;height: 250px;background: url(/img/fkad.png) no-repeat;\">\n<div id=\"adclose\" style=\"cursor: pointer; position: absolute;  top: 0px;  right: 0px;  display: block;  width: 20px;  height: 20px;font-family: cursive;background: url(img/close.png) no-repeat;\" title=\"点击关闭\"> </div>\n</div>\n<script type=\"text/javascript\">\n$(function(){\n$('#adarea').slideDown(500);\n$('#adclose').click(function(){\n$('#adarea').slideUp(500);\n});\n});\n</script>\n",
            "").replace("<br>", "\n").replace("\n更好用的代理ip请访问：https://proxy.ip3366.net/", "")) == 0:
        print("[0] Proxies Get Success!")
        file.close()
    else:
        print("[0] Proxies Get With Error!")
        file.close()
http = get("https://www.docip.net/data/free.json").text
if http == "":
    print("[1] Proxies Get With Error!")
else:
    js = loads(http)
    text = ""
    for txt in js["data"]:
        text = txt["ip"] + "\n"
    file = open("../proxies.getter.txt", 'a')
    if not file.write(text) == 0:
        print("[1] Proxies Get Success!")
        file.close()
    else:
        print("[1] Proxies Get With Error!")
        file.close()
http = get("http://www.69ip.cn/php.69ip.cn.php?quantity=9999").text
if http == "":
    print("[2] Proxies Get With Error!")
else:
    file = open("../proxies.getter.txt", 'a')
    if not file.write(http.replace(
            "<!DOCTYPE html>\n      <meta\"utf-8\"/>\n<meta http-equiv=\"Content-Type\" content=\"text/php; charset=utf-8\"/>\n<html>\n  <head>\n    <title>69ä»£çIPæåå·¥å·</title>\n  </head>\n  <body>\n      <body ondragstart=\"window.event.returnValue=false\" oncontextmenu=\"window.event.returnValue=false\" onselectstart=\"event.returnValue=false\">\n\n",
            "").replace("<br />", "")) == 0:
        print("[2] Proxies Get Success!")
        file.close()
    else:
        print("[2] Proxies Get With Error!")
        file.close()
http = get("http://pubproxy.com/api/proxy?limit=5").text
if http == "":
    print("[3] Proxies Get With Error!")
else:
    js = loads(http)
    for txt in js["data"]:
        text = txt["ipPort"] + "\n"
    file = open("../proxies.getter.txt", 'a')
    if not file.write(text) == 0:
        print("[3] Proxies Get Success!")
        file.close()
    else:
        print("[3] Proxies Get With Error!")
        file.close()
http = get(
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all").text
if http == "":
    print("[4] Proxies Get With Error!")
else:
    file = open("../proxies.getter.txt", 'a')
    if not file.write(http) == 0:
        print("[4] Proxies Get Success!")
        file.close()
    else:
        print("[4] Proxies Get With Error!")
        file.close()
http = get("https://spys.me/proxy.txt").text
if http == "":
    print("[5] Proxies Get With Error!")
else:
    txt = http.split()
    arg = 21
    text = ""
    while True:
        text = text + txt[arg] + "\n"
        arg = arg + 3
        if txt[arg] == "Free":
            break
    file = open("../proxies.getter.txt", 'a')
    if not file.write(text) == 0:
        print("[5] Proxies Get Success!")
        file.close()
    else:
        print("[5] Proxies Get With Error!")
        file.close()
