from flask_script import Manager
from flask_blog import application
#アプリケーション実行中に起動するため、アプリケーションをスクリプト内に置く必要がある

from flask_blog.scripts.db import InitDB,DropDB


if __name__ == "__main__":
    manager = Manager(application)
    manager.add_command('init_db', InitDB())
    #データベース作成のコマンド登録
    manager.add_command('drop_db', DropDB())
    #データベース削除のコマンド登録
    manager.run()
   