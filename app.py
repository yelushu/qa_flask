from flask import Flask, render_template

from models import db
from accounts.views import accounts#引用对应模块的蓝图实例
from qa.views import qa
from tools.filers import number_split
import pymysql

pymysql.install_as_MySQLdb()



app = Flask(__name__, static_folder='assets')

#从配置文件中配置
app.config.from_object('config.Config')
#数据库初始化
db.init_app(app)
app.debug=True
#注册蓝图
app.register_blueprint(accounts,url_prefix='/account')
app.register_blueprint(qa,url_prefix='/qa')

#注册过滤器
app.jinja_env.filters['number_split']=number_split

if __name__ == '__main__':
    app.run()