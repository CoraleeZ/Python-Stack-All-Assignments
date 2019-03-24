from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    s_html=request.form['strawberry']
    r_html=request.form['raspberry']
    a_html=request.form['apple']
    fn_html=request.form['first_name']
    ln_html=request.form['last_name']
    si_html=request.form['student_id']
    num=int(s_html)+int(r_html)+int(a_html)
    return render_template("checkout.html",num=num,s_html=int(s_html),r_html=int(r_html),a_html=int(a_html),fn_html=fn_html,ln_html=ln_html,si_html=si_html)

@app.route('/fruits')         
def fruits():
    
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    