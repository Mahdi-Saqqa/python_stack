from flask import Flask, render_template
app = Flask(__name__, template_folder='templates', static_url_path='/static')
@app.route('/')
def home():
    var='Hello World!'
    return render_template('index.html',head=var)
@app.route('/dojo')
def dojo():
        return render_template('index.html',head='Dojo')

@app.route('/say/<word>')
def say(word):
    var='Hi '+word+'!'
    return render_template('index.html',head=var)
@app.route('/repeat/<int:num>/<word>')
def repeat(num,word):
    return render_template('repeat.html',num=int(num),word=word)

@app.route('/<path:path>')
def catch_all(path):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)

