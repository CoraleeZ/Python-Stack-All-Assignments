from flask import Flask, render_template,request,redirect,session,flash
from mysqlconnection import connectToMySQL
app=Flask(__name__)
app.secret_key='hello'
@app.route('/', methods=['GET'])
def froms():
    return render_template('form.html')

@app.route('/result',methods=['POST'])
def results():
    if len(request.form['name'])<1:
        flash('please enter name!')
    if request.form['location']=='0':
        flash('please select a location!')
    if request.form['lan']=='0':
        flash('please select a language!')
    if len(request.form['comment'])>120:
        flash('comments should not exceed 120 characters!')
    if not '_flashes' in session.keys():
        mysql=connectToMySQL('dojosurvey')
        query='INSERT INTO surveys(Name,comment,location_id,lan_id)VALUES(%(n)s,%(c)s,%(lo)s,%(lan)s)'
        # SET FOREIGN_KEY_CHECKS=0;
        data={'n':request.form['name'],'c':request.form['comment'],'lo':int(request.form['location']),'lan':int(request.form['lan'])}
        row_n=mysql.query_db(query,data)
        print(row_n)
        flash("Friend successfully added!")
        return redirect('/results/'+str(row_n))
    return redirect('/')

@app.route('/results/<ids>')
def showresult(ids):
    mysql=connectToMySQL('dojosurvey')
    query='select surveys.Name, surveys.comment,lan.lan,location2.location from surveys join lan on surveys.lan_id=lan.id join location2 on surveys.location_id=location2.id where surveys.id=%(id)s;'
    data={'id':ids}
    result=mysql.query_db(query,data)
    print(result)
    return render_template('result.html',result=result)

        

if __name__=='__main__':
    app.run(debug=True)
