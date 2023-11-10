from flask import render_template

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template("webpage.html")

@app.route('/')
@app.route('/<page_name>')
def dynamic_paging(page_name):
	return render_template(page_name)