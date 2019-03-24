from flask import Flask,render_template,request,redirect,session,flash
import re
import time
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
from datetime import datetime
app=Flask(__name__)
app.secret_key="hello"
bcrypt=Bcrypt(app)
email_regex=re.compile(r'^[a-zA-Z0_9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex=re.compile(r'^[a-zA-Z]')
pw_regex=re.compile('\d.*[A-Z]|[A-Z].*\d')
#db name: private_wall

@app.route('/')
def loginpage():
    if not 'fn' in session.keys():
        session['fn']=" "
        session['ln']=" "
        session['em']=" "
        session['emlog']=" "
    return render_template('index.html',fn=session['fn'],ln=session['ln'],em=session['em'],emlog=session['emlog'])

@app.route('/check',methods=['POST'])
def check():
    #first name regex check
    if len(request.form['fn'])<2 or not name_regex.match(request.form['fn']):
        flash('Not valid','fn')
    #last name regex check
    if len(request.form['ln'])<2 or not name_regex.match(request.form['ln']):
        flash('Not valid','ln')
    #email regex check
    if not email_regex.match(request.form['em']):
        flash('Not valid','em')
    #after email regex check pass then check does that email exist?
    if email_regex.match(request.form['em']):
        mysql=connectToMySQL('private_wall')
        query='SELECT* FROM infos'
        result=mysql.query_db(query)
        for one in result:
            if one['email']==request.form['em']:
                flash("this email already exist",'em')
    #password lenth check
    if len(request.form['pw'])<8:
        flash('at least 8 characters','pw')
    #password regex check
    if not pw_regex.match(request.form['pw']):
        flash('at least one capital letter and one number','pw')
    #confirm email regex check
    if request.form['cpw']!=request.form['pw']:
        flash('does not match','cpw')
    
    if not '_flashes' in session.keys():
        session['fn']=request.form['fn']
        session['ln']=request.form['ln']
        session['em']=request.form['em']
        flash('You are successful logined!','reg')
        mysql=connectToMySQL('private_wall')
        query='INSERT INTO infos (first_name,last_name,email,password,creat_at,update_at)VALUES(%(fn)s,%(ln)s,%(em)s,%(pw)s,now(),now())'
        pw_ge=bcrypt.generate_password_hash(request.form['pw'])
        data={'fn':request.form['fn'],'ln':request.form['ln'],'em':request.form['em'],'pw':pw_ge}
        result=mysql.query_db(query,data)
        session['username']=request.form['fn']
        
        mysql=connectToMySQL('private_wall')
        query='SELECT id FROM infos WHERE first_name=%(fn)s'
        data={'fn':request.form['fn']}
        result=mysql.query_db(query,data)
        session['id']=result[0]['id']
        return redirect('/wall')
    return redirect("/")


@app.route('/wall')
def wall():
    #prevent directly type route with using email and pw
    if 'username' in session.keys() and 'id' in session.keys():
        #get table-infos infomation from db
        mysql=connectToMySQL('private_wall')
        query='SELECT id, first_name FROM infos ORDER BY first_name'
        info=mysql.query_db(query)
        print(info)

        # count how many comments sent by users who logged in
        mysql=connectToMySQL('private_wall')
        query='SELECT commet,info_creator_id FROM comments WHERE info_creator_id = %(info_creator_id)s '
        data={'info_creator_id':session['id']}
        send_num=len(mysql.query_db(query,data))
        print('send num',send_num)

        # comments received
        mysql=connectToMySQL('private_wall')
        query='SELECT infos.first_name,comments.commet,comments.creat_at,comments.info_receiver_id,comments.info_creator_id FROM comments join infos on comments.info_creator_id =infos.id WHERE comments.info_receiver_id = %(info_creator_id)s '
        data={'info_creator_id':session['id']}
        receive=mysql.query_db(query,data)
        rec_num=len(receive)
        for one in receive:
            one['creat_at']=(datetime.now()-one['creat_at'])
        print(receive)
        print('receive num',rec_num)

        #GET IP ADDRESS
        ip=request.remote_addr


        return render_template('wall.html',info=info,send_num=send_num,receive=receive,rec_num=rec_num,ip=ip)
    flash('you are not login, please login first!','us')
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('username')
    session.pop('id')
    return redirect('/')


@app.route('/login',methods=['POST'])
def login():
    mysql=connectToMySQL('private_wall')
    query='SELECT * FROM infos WHERE email=%(em)s'
    data={'em':request.form['em']}
    result=mysql.query_db(query,data)
    if result:
        #if result(email) exsit

        if bcrypt.check_password_hash(result[0]['password'],request.form['pw']):
            session['username']=result[0]['first_name']
            session['id']=result[0]['id']
            session['emlog']=request.form['em']
            return redirect('/wall')
    flash('Not valid','log')
    return redirect('/')

@app.route('/comment' ,methods=['POST'])
def commet():
    #insert comments into db
    mysql=connectToMySQL('private_wall')
    query='INSERT INTO comments(commet,creat_at,info_receiver_id,info_creator_id) VALUES(%(msg)s,NOW(),%(info_receiver_id)s,%(info_creator_id)s)'
    data={'msg':request.form['msg'],'info_receiver_id':request.form['receiver'],'info_creator_id':request.form['creator']}
    result=mysql.query_db(query,data)
    return redirect('/wall')


@app.route('/delete/<creatorid>')
def delete(creatorid):
    mysql=connectToMySQL('private_wall')
    query='DELETE FROM comments WHERE info_creator_id=%(creatorid)s'
    data={'creatorid':creatorid}
    result=mysql.query_db(query,data)
    return redirect('/wall')


# AJAX
@app.route('/username',methods=['POST'])
def usernamecheck():
    namecheck=False
    mysql=connectToMySQL('private_wall')
    query='SELECT * FROM infos WHERE first_name=%(fn)s'
    data={'fn':request.form['fn']}
    result=mysql.query_db(query,data)
   
    if result:
        if result[0]['first_name']==request.form['fn']:
            namecheck=True
    print(namecheck)
    return render_template('/partial/username.html',namecheck=namecheck)


@app.route('/usersearch',methods=['POST'])
def search():
    mysql=connectToMySQL('private_wall')
    query='SELETE * FROM info WHERE first_name LIKE %(search)s'
    print(query)
    data={
        'search':request.form('jscode')+'%'
    }
    result=mysql.query_db(query,data)
    print('serach',result)
  
    return render_template('search.html',answer=result)


if __name__ =="__main__":
    app.run(debug=True)