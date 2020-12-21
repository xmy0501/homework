# 使用rewrite方式更改雪球内股票名称
import json
import os

from mitmproxy import http


def response(flow: http.HTTPFlow):
    # 添加要更改的股票的筛选条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 获取响应数据并转化为python对象
        data = json.loads(flow.response.content)
        # 找到对应字段并修改
        data["data"]["items"][0]["quote"]["name"] *= 1
        data["data"]["items"][1]["quote"]["name"] *= 2
        data["data"]["items"][2]["quote"]["name"] = " "
        data["data"]["items"][-1]["quote"]["name"] *= 2
        # 把修改后的数据转化为字符串，赋值给原始响应数据
        flow.response.text = json.dumps(data)

if __name__ == '__main__':
    os.system(r"mitmdump -p 8999 -s /Users/a10369/PycharmProjects/homework/test_mitmproxy/test_rewrite_xueqiu.py")