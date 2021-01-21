#flaskコマンドで起動する場合、このファイルは使用しない

#from flask import current_app as app
#アプリケーションとして機能しているものを参照する
from flask_blog import application
#flask_blogフォルダ直下にある（__init__.py内にある変数）appをインポート

if __name__=='__main__':
    application.run()
    #applicationの起動（アプリケーション起動）
    