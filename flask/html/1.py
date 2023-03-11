'''
Author: souldream
Date: 2023-03-07 14:40:20
LastEditTime: 2023-03-08 15:33:46
LastEditors: souldream
Description: 
可以输入预定的版权声明、个性签名、空行等
'''
'''
Author: souldream
Date: 2023-03-07 14:40:20
LastEditTime: 2023-03-07 16:16:19
LastEditors: souldream
Description: 
可以输入预定的版权声明、个性签名、空行等
'''
from flask import Flask, render_template


# app = Flask(__name__)
# 当然这个templates目录也可以自定义名称
# 例如目录名称为"xxx"
app = Flask(__name__, template_folder="temp")


# 创建了网址 /show/info 和函数 index 的对应关系
# 以后用户在浏览器上访问 /show/info， 网站自动执行 index
# @app.route("/show/info")
# def index():
#     # return '中国联通'
#     # return "中<h1>国</h1><span style='color:red; '>联通</span>"
#     # Flask内部会自动打开这个文件，并读取内容，将内容给用户返回。
#     # 默认:去当前项目目录的templates文件夹中找。|
#     # aa
#     return  render_template("index.html")

@app.route("/show/info/test")
def test():
    return  render_template("test.html")



    





if __name__ == '__main__':
    app.run()
