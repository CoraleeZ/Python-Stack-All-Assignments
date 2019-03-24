from flask import Flask,render_template,request,redirect,session,flash
import re
from mysqlconnection import connectToMySQL
app=Flask(__name__)
app.secret_key='hello'
email_regex=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/' )
def index():
   return render_template('index.html')

@app.route('/check',methods=['POST'])
def check():
    
    if not email_regex.match(request.form['email']):
        flash('Email is not valid!')
        
    else:
        mysql=connectToMySQL('emailvalidation')
        query='SELECT *FROM email'
        result=mysql.query_db(query)
        for one in result:
            if one['email']==request.form['email']:
                flash('Email is exist')
                return redirect('/')
        flash(request.form['email'])
        mysql=connectToMySQL('emailvalidation')
        query='INSERT INTO email(email,creat_at,update_at) VALUES(%(em)s,now(),now())'
        data={'em':request.form['email']}
        result=mysql.query_db(query,data)
        return redirect('/success')
    return redirect('/')



@app.route('/success')
def show():
    mysql=connectToMySQL('emailvalidation')
    query='SELECT * FROM email'
    result=mysql.query_db(query)
    return render_template('success.html',result=result)


@app.route('/delete/<emailid>')
def delete(emailid):
    mysql=connectToMySQL('emailvalidation')
    query='DELETE FROM email WHERE id=%(id)s'
    data={'id':emailid}
    result=mysql.query_db(query,data)
    return redirect('/success')




if __name__ == "__main__":
    app.run(debug=True)