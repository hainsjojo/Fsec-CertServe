from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import re


# App config.
#DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'YOURKEY'

IP = '127.0.0.1' # Change this
cert_file = "null"


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            name=request.form['name']
            print(name)
            ## ----- File search

            cname = name.replace(" ", "_")
            print("cname" + cname)

            pattern = re.compile(cname, re.IGNORECASE)
            for line in open("filename.txt"):
                for match in re.finditer(pattern, line):   
                    print(line)
                    cert_file = line

        if form.validate():
            try:
                print("Cert " + cert_file)
                flash('Download your cert here: ')
                download = 'http://'+IP+'/certs-file/' + cert_file

            except:
                download = ""
                flash('Not Found ')
        else:
            download = ""
            flash('All the form fields are required. ')
    
        return render_template('hello.html', form=form, value=download)

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
