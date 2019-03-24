from flask import Flask, render_template,redirect,request,session
from mysqlconnection import connectToMySQL
app=Flask(__name__)
app.secret_key='hello'

@app.route('/users/new')
def addnew():

    return render_template('new.html')

@app.route('/users/creat', methods=['POST'])
def creat():
    mysql=connectToMySQL('semirestful')
    query='INSERT INTO users(first_name,last_name,email,creat_at, update_at,description) VALUES(%(fn)s,%(ln)s,%(email)s,now(),now(),%(de)s);'
    data={'fn':request.form['fname'],'ln':request.form['lname'],'email':request.form['email'],'de':request.form['de']}
    result=mysql.query_db(query,data)
    return redirect('/users/'+str(result))


@app.route('/users/<userid>')
def users(userid):
    mysql=connectToMySQL('semirestful')
    query='SELECT * FROM users WHERE id=%(id)s;'
    data={'id':userid}
    result=mysql.query_db(query,data)
    print(result)
    return render_template('user.html',userinfo=result)



@app.route('/users')
def home():
    mysql=connectToMySQL('semirestful')
    query='SELECT * FROM users'
    result=mysql.query_db(query)
    return render_template('home.html',userallinfo=result)


@app.route('/users/<userid>/edit')
def show_edit(userid):
    mysql=connectToMySQL('semirestful')
    query='SELECT * FROM users WHERE id=%(id)s'
    data={'id':userid}
    result=mysql.query_db(query,data)
    print(result)
    return render_template('edit.html' ,userid=userid,userinfo=result)

@app.route('/users/<userid>/update',methods=['POST'])
def edit_update(userid):
    mysql=connectToMySQL('semirestful')
    query='UPDATE users SET first_name=%(fn)s,last_name=%(ln)s,email=%(email)s,update_at=NOW(),description=%(de)s WHERE id=%(id)s'
    data={'fn':request.form['fname'],'ln':request.form['lname'],'email':request.form['email'],'id':userid,'de':request.form['de']}
    result=mysql.query_db(query,data)
    print(userid)
    return redirect('/users/'+userid)

@app.route('/users/<userid>/destroy')
def deleteuser(userid):
    mysql=connectToMySQL('semirestful')
    query='DELETE FROM users WHERE id=%(id)s;'
    data={'id':userid}
    result=mysql.query_db(query,data)
    return redirect('/users')



if __name__ == "__main__":
    app.run(debug=True)