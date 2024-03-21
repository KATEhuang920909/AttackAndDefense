# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：
   Author :       huangkai
   date：          2024/2/22
-------------------------------------------------
"""
from flask import Flask, render_template, request, redirect, url_for
import json
from CrawlerDetect.detectmodel import DetectModel

# from scapy.all import *
app = Flask(__name__)



def data_load():
    data = json.load(open("chip2019.json", encoding="utf8"))
    data = [[k["sen1"], k["sen2"]] for k in data["data"]][:10]
    result = ""
    for k in data:
        result += "\t".join(k)
        result += "\n"
    return result


def crawler_detect():
    # crawler_detect = DetectModel()
    method = request.method
    url = request.url
    path = request.path
    headers = dict(request.headers)
    print("请求方法：", method)
    print("请求url：", url)
    print("请求路径：", path)
    print("请求头：", headers)
    # result = crawler_detect.isCrawler(user_agent=headers["User-Agent"])
    print("agent：", headers["User-Agent"])
    # print(result)




def icmp_request(packet):
    if packet[0][1].haslayer('TCP'):
        print("Received ICMP request")



@app.route('/')
def index():
    data = data_load()
    crawler_detect()
    return f'''
        
        <form action="/redirect" method="post">
            <input type="submit" value="Click me!" />
        </form>
        <body>{data}</body>
    '''


@app.route('/index2')
def index2():
    crawler_detect()

    return render_template('index.html')


@app.route('/redirect', methods=['POST'])
def redirect_page():
    # 这里可以根据业务需求进行其他操作或者重定向到不同的URL
    return redirect(url_for('index2'))


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 8888
    app.run(port=port)
