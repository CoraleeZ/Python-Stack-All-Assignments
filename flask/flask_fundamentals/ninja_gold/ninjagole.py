from flask import Flask,render_template,request,redirect,session
import random
import time
app=Flask(__name__)
app.secret_key='hello'
@app.route('/')
def render():
    if 'score' not in session:    
        session['score']=0
        session['act']=[]
        session['step']=0
    return render_template('ninjagole.html',act=session['act'],score=session['score'])
    

@app.route('/process_money', methods=['POST'])
def process():

    if request.form['gold']=='farm':
        session['rfarm']=random.randint(10,20)
        session['farm']=session['rfarm']
        farm_str='<p style="color:green;">Earned '+str(session['rfarm'])+' golds from the farm! ('+time.strftime('%Y/%m/%d %H:%M %p', time.localtime())+')</p>'
        session['act'].insert(0,farm_str)
    else:
        session['farm']=0

    if request.form['gold']=='cave':
        session['rcave']=random.randint(5,10)
        session['cave']=session['rcave']
        cave_str='<p style="color:green;">Earned '+str(session['rcave'])+' golds from the cave! ('+ time.strftime('%Y/%m/%d %H:%M %p', time.localtime())+')</p>'
        session['act'].insert(0,cave_str)
    else:
        session['cave']=0

    if request.form['gold']=='house':
        session['rhouse']=random.randint(2,5)
        session['house']=session['rhouse']
        house_str='<p style="color:green;">Earned '+str(session['rhouse'])+' golds from the house! ('+ time.strftime('%Y/%m/%d %H:%M %p', time.localtime())+')</p>'
        session['act'].insert(0,house_str)
    else:
        session['house']=0

    if request.form['gold']=='casino':
        session['rcasino']=random.randint(-50,50)
        session['casino']=session['rcasino']
        if session['rcasino']<0:
            casino_str='<p style="color:red;">Entered a casino and lost '+str(session['rcasino'])+' golds...Ouch.('+ time.strftime('%Y/%m/%d %H:%M %p', time.localtime())+')</p>'
            session['act'].insert(0,casino_str)
        else:
            casino_str='<p style="color:green;">Earned '+str(session['rcasino'])+' golds from the casino! ('+ time.strftime('%Y/%m/%d %H:%M %p', time.localtime())+')</p>'
            session['act'].insert(0,casino_str)
    else:
        session['casino']=0

    session['score']+=session['farm']+session['cave']+session['house']+session['casino']
    session['step']+=1
    if session['step']<=15 and session['score']>=150:
        return render_template('result.html',step='WIN')
    elif session['step']==15 and session['score']<150:
        return render_template('result.html',step='LOSE')

    return redirect('/')


@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)