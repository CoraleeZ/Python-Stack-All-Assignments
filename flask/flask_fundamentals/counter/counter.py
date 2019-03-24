from flask import Flask,render_template,redirect, session,request
app=Flask(__name__)
app.secret_key='counter'
@app.route('/')
def counter():
    if ('visit_time' in session):
        session['visit_time']+=1
        session['acvisit']+=1
    else:
        session['visit_time']=1
        session['acvisit']=1
    print(session)
    return render_template("index.html",acvist=session['acvisit'])

@app.route('/addtow')
def addtow():
    session['visit_time']+=1
    return redirect('/')

@app.route('/number',methods=['POST'])
def number():
    session['visit_time']+=int(request.form['number'])-1
    return redirect('/')




@app.route('/reset')
def rreset():
    session['visit_time']=0
    session['acvisit']=0
    return redirect('/')

@app.route('/destroy_session')
def clear():
    session.clear()
    return render_template('clear.html')


if __name__=='__main__':
    app.run(debug=True)