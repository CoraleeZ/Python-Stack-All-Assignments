from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<name>')
def say_name(name):
    return 'Hi '+str(name)

@app.route('/repeat/<ints>/<name>')
def repeat(ints,name):
    return str(name)*int(ints)



if __name__ =='__main__':
    app.run(debug=True)