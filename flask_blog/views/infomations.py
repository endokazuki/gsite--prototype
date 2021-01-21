from flask import request,redirect,url_for,render_template,flash,session
#必要なパッケージ
from flask_blog import application
#アプリケーションとして機能しているものを参照する
from flask import Blueprint
#functional(関数)単位でアプリケーションを分割

infomation=Blueprint('infomation',__name__)

@infomation.route('/infomations/showall',methods=['GET'])
def showall_infomation():
    return render_template('infomations/showall.html')
    #（infomationsフォルダ直下にあるshowall.htmlを返す