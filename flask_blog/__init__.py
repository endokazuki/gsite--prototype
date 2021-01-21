from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

application=Flask(__name__)
application.config.from_object('flask_blog.config')
    #flask_blog直下にあるconfig.pyをコンフィグの有効化をapplicationに適用

#if test_config:
# application.config.from_mapping('test_config')

db.init_app(application)
    #db(データベース)の作成

from flask_blog.views.entries import entry
application.register_blueprint(entry,url_prefix='/users')
    #flask_blogのentryアプリケーションをインポート

from flask_blog.views.views import view
application.register_blueprint(view)
    #flask_blogのviewsアプリケーションをインポート

from flask_blog.views.infomations import infomation
application.register_blueprint(infomation)
    #flask_blogのinfomationsアプリケーションをインポート
