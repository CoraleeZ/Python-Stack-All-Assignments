from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/', methods=['POST','GET'])
def froms():
    return render_template('form.html')

@app.route('/result',methods=['POST'])
def results():
    name_form=request.form['name']
    location_form=request.form['location']
    lan_form=request.form['lan']
    comment_form=request.form['comment']
    gender_form=request.form['gender']
    check1_form=request.form['check1']
    check2_form=request.form['check2']
    check_form=[check1_form,check2_form]
    print(request.form['check1'])
    print(request.form['check2'])

    return render_template('result.html',name_html=name_form,location_html=location_form,lan_html=lan_form,comment_html=comment_form,gender_html=gender_form,check_html=check_form)
if __name__=='__main__':
    app.run(debug=True)
