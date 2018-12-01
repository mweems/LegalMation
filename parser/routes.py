from parser import app
from flask import render_template, url_for, request
from parser.forms import FileForm
from fileParser import ParseFile


@app.route('/', methods=['GET', 'POST'])
def index():
	form = FileForm()
	if form.validate_on_submit():
		data = ParseFile(request.files['file'])
		return render_template('data.html', data=data)
	return render_template('index.html', form=form)