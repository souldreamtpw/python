'''
Author: souldream
Date: 2023-03-08 15:38:11
LastEditTime: 2023-03-08 16:34:35
LastEditors: souldream
Description: 超链接
可以输入预定的版权声明、个性签名、空行等
'''

# div: 占一整行(块级标签)
# span: 用多少占多少(行内标签/内联标签)
# 两个 span 标签不在同一行,页面显示时会在同一行,中间以一个空格分隔
# 两个 span 标签在同一行,页面显示时会在同一行,中间没有空格,连着

from flask import Flask, render_template


app = Flask(__name__, template_folder="html")

@app.route("/show/info")
def test():
    return  render_template("test2.html")

@app.route("/get/news")
def get_news():
    return  render_template("get_news.html")

@app.route("/goods/list")
def goods_list():
    return  render_template("goods_list.html")

@app.route("/user/list")
def user_list():
    return  render_template("user_list.html")

if __name__ == '__main__':
    app.run()
