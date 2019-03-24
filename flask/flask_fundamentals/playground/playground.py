from flask import Flask, render_template
app=Flask(__name__)
@app.route("/play")
def welcome():
    classname='one'
    return render_template('index.html',num_times=3,class_name=classname)
@app.route("/play/<times>")
def timebox(times):
    classname='two'
    return render_template('index.html',num_times=int(times),class_name=classname)
@app.route("/play/<times>/<color>")
def timeboxcolor(times='None',color='None'):

    classname='three'
    return render_template('index.html',num_times=int(times),class_name=classname,box_color=color)

@app.errorhandler(404)
def alert(g):
    return 'wrong page'

if __name__=='__main__':
    app.run(debug=True)
