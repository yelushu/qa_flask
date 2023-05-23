import os
import pymysql

"配置文件"


class Config(object):
    "项目的配置文件"
    #数据库连接uri
    SQLALCHEMY_DATABASE_URI= 'mysql://root:yelushu7758258@localhost/qa_flask'  # 配置数据库
    #flash，wtf cast保护
    SECRET_KEY = 'abc123abc'
    SESSION_TYPE = 'filesystem'

    #文件上传的根目录
    MEDIA_ROOT=os.path.join(os.path.dirname(__file__),'medias')