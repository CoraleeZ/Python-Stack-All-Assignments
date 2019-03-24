from flask import Flask,render_template,request,redirect,session,flash
import re
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
app=Flask(__name__)
app.secret_key="hello"
bcrypt=Bcrypt(app)
email_regex=re.compile(r'^[a-zA-Z0_9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex=re.compile(r'^[a-zA-Z]')
pw_regex=re.compile('\d.*[A-Z]|[A-Z].*\d')
# login_and_registration

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
    if len(request.form['fn'])<2 or not name_regex.match(request.form['fn']):
        flash('Not valid','fn')
    if len(request.form['ln'])<2 or not name_regex.match(request.form['ln']):
        flash('Not valid','ln')
    if not email_regex.match(request.form['em']):
        flash('Not valid','em')
    if email_regex.match(request.form['em']):
        mysql=connectToMySQL('login_and_registration')
        query='SELECT* FROM lr'
        result=mysql.query_db(query)
        for one in result:
            if one['email']==request.form['em']:
                flash("this email already exist",'em')
    if len(request.form['pw'])<8:
        flash('at least 8 characters','pw')
    if not pw_regex.match(request.form['pw']):
        flash('at least one capital letter and one number','pw')
    if request.form['cpw']!=request.form['pw']:
        flash('does not match','cpw')
    
    if not '_flashes' in session.keys():
        session['fn']=request.form['fn']
        session['ln']=request.form['ln']
        session['em']=request.form['em']
        flash('You are successful registered!','reg')
        mysql=connectToMySQL('login_and_registration')
        query='INSERT INTO lr (first_name,last_name,email,password,creat_at,update_at)VALUES(%(fn)s,%(ln)s,%(em)s,%(pw)s,now(),now())'
        pw_ge=bcrypt.generate_password_hash(request.form['pw'])
        data={'fn':request.form['fn'],'ln':request.form['ln'],'em':request.form['em'],'pw':pw_ge}
        result=mysql.query_db(query,data)
        session['username']=request.form['fn']
        return redirect('/success')
    return redirect("/")


@app.route('/success')
def success():
    if 'username' in session.keys():
        return render_template('success.html')
    flash('you are not login, please login first!','us')
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')


@app.route('/register',methods=['POST'])
def register():
    mysql=connectToMySQL('login_and_registration')
    query='SELECT * FROM lr WHERE email=%(em)s'
    data={'em':request.form['em']}
    result=mysql.query_db(query,data)
    if result:

        if bcrypt.check_password_hash(result[0]['password'],request.form['pw']):
            session['username']=result[0]['first_name']
            session['emlog']=request.form['em']
            return redirect('/success')
    flash('Not valid','log')
    return redirect('/')



if __name__ =="__main__":
    app.run(debug=True)