from parser import app
from flask import render_template, redirect, url_for, request
from parser.forms import FileForm
from fileParser import ParseFile

@app.route('/', methods=['GET', 'POST'])
def index():
	form = FileForm()
	if form.validate_on_submit():
		file = request.form['file']
		data = ParseFile(file)
		return redirect(url_for('data_view', data=data))
	return render_template('index.html', form=form)

@app.route('/data_view/<data>')
def data_view(data):
	return render_template('data.html', data=data)