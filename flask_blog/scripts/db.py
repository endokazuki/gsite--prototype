from flask_script import Command
from flask_blog import db

class InitDB(Command):
    "create database"
    #コメント
    def run(self):
        db.create_all()
    #実行スクリプト

class DropDB(Command):
    "drop database"
    #コメント
    def run(self):
        db.drop_all()
    #実行スクリプト