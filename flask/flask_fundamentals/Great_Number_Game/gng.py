from flask import Flask, render_template, request,redirect,session
import random
app=Flask(__name__)
app.secret_key='hello'
@app.route('/')
def randomnum():
    # if session['answer']==None:
    session['nameofclass']='empty'
    session['playagain']='empty'
    session['randomnum']=random.randint(1,100)
    print(session['answer'])
    print(session['nameofclass'])
    print(session['playagain'])
    return render_template('gng.html',answer=session['answer'],nameofclass=session['nameofclass'],playa=session['playagain'])

@app.route('/game',methods=['POST','GET'])
def game():
    if session['randomnum']>int(request.form['guessnum']):
        session['answer']='Not right, try a larger one!'
        session['nameofclass']='wrong'
        session['playagain']='empty'
    elif session['randomnum']<int(request.form['guessnum']):
        session['answer']='Not right, try a smaller one!'
        session['nameofclass']='wrong'
        session['playagain']='empty'
    elif session['randomnum']==int(request.form['guessnum']):
        session['answer']='You get it!'
        session['nameofclass']='right'
        session['playagain']='show'
    print(session['answer'])
    print(session['nameofclass'])
    print(session['playagain'])
    return redirect('/game2')

@app.route('/game2')
def games():
    return render_template('gng.html',answer=session['answer'],nameofclass=session['nameofclass'],playa=session['playagain'])



@app.route('/clear')
def clear():
    session.clear()
    session['answer']=None
    session['nameofclass']='empty'
    session['playagain']='empty'
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)



