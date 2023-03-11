'''
Author: souldream
Date: 2023-03-11 14:06:21
LastEditTime: 2023-03-11 14:25:06
LastEditors: souldream
Description: 
可以输入预定的版权声明、个性签名、空行等
'''
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register',methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # 1.接收到的数据
        print(request.form)

        # 2.获取数据
        user = request.form.get('user')
        psd = request.form.get('psd')
        print(user)
        print(psd)

        # 3.将用户信息写入文件中实现注册，写入到excel表中实现注册，写入数据库中实现注册
        return '注册成功'

if __name__ == '__main__':
    app.run()
