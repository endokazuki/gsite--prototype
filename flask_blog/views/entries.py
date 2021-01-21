from flask import request,redirect,url_for,render_template,flash,session
#必要なパッケージ
from flask_blog import application
#アプリケーションとして機能しているものを参照する
from flask_blog import db
#データベース内の処理
from flask_blog.models.entries import Entry
#データベースへの入力処理
from flask_blog.views.views import login_required
#ログインセッションの簡略化
from flask import Blueprint
#functional(関数)単位でアプリケーションを分割


entry=Blueprint('entry',__name__)


#管理者の項目

@entry.route('/')
@login_required
#デフォルトの場合ローカルホストにリクエストがあった時（初期状態）、アクションする
def show_entries():
    entries=Entry.query.order_by(Entry.id.desc()).all()
    #Entryモデル（テーブル）のidの降べき(最新)の順で全て出力する
    return render_template('entries/index.html',entries=entries,val="manage")
    #（sessionが存在する場合）templateフォルダ直下にあるentries/index.htmlを返し（レンダリング）
    #データベース内に保存してある記事を出力する

@entry.route('/entries',methods=['POST'])
@login_required
#記事の作成ボタンを押したとき、アクションする
def add_entry():

    entry=Entry(
            title=request.form['title'],
            text=request.form['text'],
            category=request.form['category'],
            initial=request.form['initial']
            )
    db.session.add(entry)
    db.session.commit()
    #データベースにデータ保存
    flash('新しい記事が作成されました')
    return redirect(url_for('entry.show_entries',val="manage"))
    #（sessionが存在する場合）データベースにデータを保存し、show_entriesメソッドを返す

@entry.route('/entries/new',methods=['GET'])
@login_required
#新規投稿ボタンを押したとき、アクションする
def new_entry():
    return render_template('entries/new.html',val="manage")
    #新規記事作成画面に移動

@entry.route('/entries/searchmanage',methods=['GET'])
@login_required
#@application.route('URL')
#http://127.0.0.1:5000/searchのリクエストがあった時（検索項目を押したとき）、アクションする
def searchmanage():
    flash('検索ページに移動します')
    #ブラウザにメッセージを引き渡す
    return render_template('entries/searchmanage.html',val="manage")

@entry.route('/entries/searchmanageresult',methods=['POST'])
@login_required
#@application.route('URL')
#http://127.0.0.1:5000/searchのリクエストがあった時（検索ボタンを押したとき）、アクションする
def searchmanageresult():
    target_title=request.form['title']
    search_target_title="%{}%".format(target_title)
    #検索ワード

    if search_target_title=="%%":
        flash('検索ワードを入力してください')
        return render_template('entries/searchmanageresult.html',val="manage")
    else:
        result_title = Entry.query.filter(Entry.title.like(search_target_title)).all()
        flash('検索結果です')
        #ブラウザにメッセージを引き渡す
        return render_template('entries/searchmanageresult.html',entries=result_title,val="manage")

@entry.route('/entries/<int:id>',methods=['GET'])
@login_required
#記事ごとの「続きを見る」ボタンを押したとき、アクションする
def show_entry(id):
    entry= Entry.query.get(id)
    #引き渡されたidの記事を取得
    return render_template('entries/show.html',entry=entry,val="manage")
    #作成した記事の閲覧画面に移動


@entry.route('/entries/<int:id>/edit',methods=['GET'])
@login_required
#編集ボタンを押したとき、アクションする
def edit_entry(id):
    entry= Entry.query.get(id)
    #引き渡されたidの記事を取得
    return render_template('entries/edit.html',entry=entry)
    #記事の編集画面に移動

@entry.route('/entries/<int:id>/update',methods=['POST'])
@login_required
#編集ボタンを押したとき、アクションする
def update_entry(id):
    entry= Entry.query.get(id)
    entry.title=request.form['title']
    entry.text=request.form['text']
    entry.category=request.form['category']
    entry.initial=request.form['initial']
    db.session.merge(entry)
    db.session.commit()
    flash('記事が更新されました')
    #引き渡されたidの記事を更新
    return redirect(url_for('entry.show_entries'))
    #（sessionが存在する場合）データベースにデータを保存し、show_entriesメソッドを返す

@entry.route('/entries/<int:id>/delete',methods=['POST'])
@login_required
#編集ボタンを押したとき、アクションする
def delete_entry(id):
    entry= Entry.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    flash('記事が削除されました')
    #引き渡されたidの記事を更新
    return redirect(url_for('entry.show_entries'))
    #（sessionが存在する場合）データベースにデータを保存し、show_entriesメソッドを返す


#ユーザーの項目

@entry.route('/entries',methods=['GET'])
@login_required
def show_guest_entries():
    entries=Entry.query.order_by(Entry.id.desc()).all()
    #Entryモデル（テーブル）のidの降べき(最新)の順で全て出力する
    return render_template('entries/guestindex.html',entries=entries,val='guest')
    #（sessionが存在する場合）templateフォルダ直下にあるentries/index.htmlを返し（レンダリング）
    #データベース内に保存してある記事を出力する

@entry.route('/entries/<int:id>/guestshow',methods=['GET'])
@login_required
#記事ごとの「続きを見る」ボタンを押したとき、アクションする
def guestshow_entry(id):
    entry= Entry.query.get(id)
    #引き渡されたidの記事を取得
    return render_template('entries/guestshow.html',entry=entry)
    #記事の閲覧画面に移動

@entry.route('/entries/search',methods=['GET'])
@login_required
#@application.route('URL')
#http://127.0.0.1:5000/searchのリクエストがあった時（検索項目を押したとき）、アクションする
def search():
    flash('検索ページに移動します')
    #ブラウザにメッセージを引き渡す
    return render_template('entries/search.html',val='guest')

@entry.route('/entries/result',methods=['POST'])
@login_required
#@application.route('URL')
#http://127.0.0.1:5000/searchのリクエストがあった時（検索ボタンを押したとき）、アクションする
def searchresult():
    target_title=request.form['title']
    search_target_title="%{}%".format(target_title)
    #検索ワード
    
    result_title = Entry.query.filter(Entry.title.like(search_target_title)).all()
    flash('検索結果です')
    #ブラウザにメッセージを引き渡す
    return render_template('entries/result.html',entries=result_title,val='guest')

@entry.route('/entries/textresult',methods=['POST'])
@login_required
#@application.route('URL')
#http://127.0.0.1:5000/searchのリクエストがあった時（検索ボタンを押したとき）、アクションする
def searchtext_result():
    target_text=request.form['text']
    search_target_text="%{}%".format(target_text)
    #検索ワード
    
    result_text = Entry.query.filter(Entry.text.like(search_target_text)).all()
    flash('検索結果です')
    #ブラウザにメッセージを引き渡す
    return render_template('entries/textresult.html',entries=result_text,val='guest')

@entry.route('/entries/categoryresult',methods=['POST'])
@login_required
#@application.route('URL')
#http://127.0.0.1:5000/searchのリクエストがあった時（検索ボタンを押したとき）、アクションする
def searchcategory_result():
    target_category=request.form['category']
    search_target_category="%{}%".format(target_category)
    #分類項目

    result_category = Entry.query.filter(Entry.category.like(search_target_category)).all()
    flash('分類項目一覧です')
    #ブラウザにメッセージを引き渡す
    return render_template('entries/categoryresult.html',entries=result_category,val='guest')

@entry.route('/entries/initialresult',methods=['POST'])
@login_required
#@application.route('URL')
#http://127.0.0.1:5000/searchのリクエストがあった時（検索ボタンを押したとき）、アクションする
def searchinitial_result():
    target_initial=request.form['initial']
    search_target_initial="%{}%".format(target_initial)
    #イニシャル
    
    result_initial = Entry.query.filter(Entry.initial.like(search_target_initial)).all()
    flash('分類項目一覧です')
    #ブラウザにメッセージを引き渡す
    return render_template('entries/initialresult.html',entries=result_initial,val='guest')
