#Pythons Flask Web development Framework with Bootstrap
#Milktea

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    try:
	return render_template('index.html')
    except Exception as e:
	return (str(e))

@app.route('/about/')
def about():
    try:        
	return render_template('about.html')
    except Exception as e:
	return (str(e))

@app.route('/versions/')
def versions():
    try:
        lang = "Python"
        versions = ["2.5","2.7","3.1","3.4"]
	return render_template('versions.html',lang = lang, versions = versions)
    except Exception as e:
	return (str(e))

@app.errorhandler(404)
def four_oh_four(e):
    return render_template("404.html")

if __name__ == '__main__':
   app.run()


