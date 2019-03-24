from flask import Flask,render_template,request,redirect,session
from mysqlconnectioncr import connectToMySQL
app=Flask(__name__)
app.secret_key='hello'

@app.route('/')
def show():
    mysql=connectToMySQL('c+r')
    query='SELECT*FROM pets;'
    result=mysql.query_db(query)
    print(result)
    return render_template('c+r.html',allpet=result)


@app.route('/add', methods=['POST'])
def add():
    mysql=connectToMySQL("c+r")
    query='INSERT INTO pets (name,type,created_at,updated_at) VALUES(%(pname)s,%(ptype)s,NOW(),NOW());'
    data={'pname':request.form['pname'],
          'ptype':request.form['ptype']}
    result=mysql.query_db(query,data)
    return redirect('/')






if __name__ == "__main__":
    app.run(debug=True)