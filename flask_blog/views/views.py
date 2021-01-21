from flask import request,redirect,url_for,render_template,flash,session
#必要なパッケージ
from flask_blog import application
#アプリケーションとして機能しているものを参照する
from functools import wraps
#メソッド実行前に実行するメソッドの事
from flask import Blueprint
#functional(関数)単位でアプリケーションを分割

view=Blueprint('view',__name__)

def login_required(view):
    @wraps(view)
    def inner(*args,**kwarags):
        if not session.get('logged_in'):
            return redirect(url_for('view.guestlogin'))
        return view(*args,**kwarags)
    return inner

@view.app_errorhandler(404)
#初めてページにアクセスする時に行う処理
def non_existant_route(error):
    return redirect(url_for('view.guestlogin'))

@view.route('/login',methods=['GET','POST'])
#@application.route('URL')
#http://127.0.0.1:5000/loginのリクエストがあった時（ログインボタンを押したとき）、アクションする
#ページの取得はGETを使い、データ送信の場合はPOSTを使用する
def login():
    flash('ここは管理者ページです')
    if request.method =='POST':
        if request.form['username'] != application.config['USERNAME']:
            flash('ユーザ名が異なります')
            #ブラウザにメッセージを引き渡す
        elif request.form['password'] != application.config['PASSWORD']:
            flash('パスワードが異なります')
            #ブラウザにメッセージを引き渡す
        else:
            session['logged_in']=True
            flash('ログインしました')
            #session情報の取得
            
            return redirect(url_for('entry.show_entries'))
            #return redirect('/')
    return render_template('login.html')
    #ユーザ名・パスワード名が共に一致しない場合、login.htmlを返す（レンダリング）

@view.route('/guestlogin',methods=['GET','POST'])
#@application.route('URL')
#http://127.0.0.1:5000/loginのリクエストがあった時（ログインボタンを押したとき）、アクションする
#ページの取得はGETを使い、データ送信の場合はPOSTを使用する
def guestlogin():
    flash('ここはユーザーページです')
    if request.method =='POST':
        if request.form['username'] != application.config['GUESTNAME']:
            flash('ユーザ名が異なります')
            #ブラウザにメッセージを引き渡す
        elif request.form['password'] != application.config['GUESTPASSWORD']:
            flash('パスワードが異なります')
            #ブラウザにメッセージを引き渡す
        else:
            session['logged_in']=True
            flash('ユーザがログインしました')
            #session情報の取得
            
            return redirect(url_for('entry.show_guest_entries'))
            #return redirect('/')
    return render_template('guestlogin.html')
    #ユーザ名・パスワード名が共に一致しない場合、login.htmlを返す（レンダリング）


@view.route('/logout')
#@application.route('URL')
#http://127.0.0.1:5000/logoutのリクエストがあった時（ログアウトボタンを押したとき）、アクションする
def logout():
    session.pop('logged_in',None)
    #ログアウトすると、session情報は削除される
    flash('ログアウトします')
    #ブラウザにメッセージを引き渡す
    return redirect(url_for('entry.show_entries'))
