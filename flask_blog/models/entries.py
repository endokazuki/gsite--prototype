from flask_blog import db
from datetime import datetime

class Entry(db.Model):
    __tablename__ = 'entries'
    #テーブル定義
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    text = db.Column(db.Text)
    category=db.Column(db.Integer)
    initial=db.Column(db.Integer)
    created_at = db.Column(db.DateTime)

    def __init__(self, title=None, text=None,category=None,initial=None):
        self.title = title
        self.text = text
        self.category=category
        self.initial=initial
        self.created_at = datetime.utcnow()
        #モデルの標準設定（デフォルト値）

    def __repr__(self):
        return '<Entry id:{} title:{} text:{} category:{} initial:{}>'.format(self.id, self.title, self.text,self.category,self.initial)
        #コンソール出力
