import os

from mitmproxy import http

# 该方法相当于charles的maplocal：request方法名不可修改
def request(flow: http.HTTPFlow):
    # 发起请求，判断url是否是预期值
    if "quote.json" in flow.request.pretty_url:
        # 打开一个保存在本地的数据文件
        with open("/Users/a10369/Desktop/homework.json") as f:
            # 创造response
            flow.response = http.HTTPResponse.make(
                # 响应状态码
                200,  # (optional) status code
                # 读取文件中的数据作为返回内容
                f.read(),  # (optional) content
                # 指定头信息
                {"Content-Type": "application/json"}  # (optional) headers
            )



if __name__ == '__main__':
    os.system(r'mitmdump -p 8999 -s /Users/a10369/PycharmProjects/homework/test_mitmproxy/test_maplocal_xueqiu.py')