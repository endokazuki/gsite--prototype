import os
from flask_blog import application,db
import unittest
import tempfile
from flask_blog.scripts.db import InitDB,DropDB

class TestFlaskBlog(unittest.TestCase):

    def setUp(self):
    #テスト用のデータベース削除
        self.db_fd, self.db_path = tempfile.mkstemp()
        self.app = application({
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///{}'.format(self.db_path)
        })
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        InitDB().run()

    def tearDown(self):
    #テスト用のデータベース削除
        DropDB().run
        self.app_context.pop()
        os.unlink(self.db_path)

    def login(self,username,password):
    #ログイン
        return self.client.post('/login',data=dict(
            username=username,
            password=password
        ),follow_redirects=True)
    
    def logout(self):
    #ログアウト
        return self.client.get('/logout',follow_redirects=True)

    def test_login_logout(self):
        rv=self.login('john','due123')
        assert 'ログインしました'.encode() in rv.data
        rv=self.logout()
        assert 'ログアウトしました'.encode() in rv.data
        rv=self.login('admin','default')
        assert 'ユーザ名が異なります'.encode() in rv.data
        rv=self.login('john','default')
        assert 'パスワードが異なります'.encode() in rv.data

if __name__=='__main__':
    unittest.main()