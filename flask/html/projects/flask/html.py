'''
Author: souldream
Date: 2023-03-10 21:26:06
LastEditTime: 2023-03-10 23:57:15
LastEditors: souldream
Description: 
可以输入预定的版权声明、个性签名、空行等
'''
from flask import Flask, render_template, request


app = Flask(__name__)


# 页面上的数据，想要提交到后台
# form标签包裹要提交的数据标签
#     提交方式：method='get'
#     提交的地址： action="xx/xxx/xx/"
#     在form标签中必须要有一个submit标签
# 在form中的一些标签：input/select/Textarea
#     一定要写name属性

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

# @app.route('/do/reg', methods=['GET'])
# def do_reg():
#     # 1.接收到的数据
#     print(request.args)
#     return '注册成功'

# @app.route('/register',methods=['GET',])
# def register():
#     return render_template('register.html')

# @app.route('/post/reg', methods=["POST"])
# def post_reg():
#     # 1.接收到的数据
#     print(request.form)

#     # 2.获取数据
#     user = request.form.get('user')
#     psd = request.form.get('psd')
#     print(user)
#     print(psd)

#     # 3.将用户信息写入文件中实现注册，写入到excel表中实现注册，写入数据库中实现注册
#     return '注册成功'

if __name__ == '__main__':
    app.run()
