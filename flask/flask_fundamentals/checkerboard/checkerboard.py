from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def checker():
    class_name1="red"
    class_name2="black"
    return render_template('index.html',num_rows=8,color1=class_name1,color2=class_name2)

@app.route('/<x>')
def checkernum(x):
    class_name1="green"
    class_name2="yellow"
    return render_template('index.html',num_rows=int(x),color1=class_name1,color2=class_name2)

@app.route('/<x>/<y>')
def checkernumcol(x,y):
    class_name1="green"
    class_name2="yellow"
    return render_template('index.html',num_rows=int(x),num_col=int(y),color1=class_name1,color2=class_name2)    

@app.route('/<x>/<y>/<color1>/<color2>')
def checkernumcolcolor(x,y,color1='red',color2='black'):
    class_name1=color1
    class_name2=color2
    return render_template('index.html',num_rows=int(x),num_col=int(y),color1=class_name1,color2=class_name2)    



if __name__=='__main__':
    app.run(debug=True)