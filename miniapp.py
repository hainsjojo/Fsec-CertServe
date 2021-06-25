from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import re


# App config.
#DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


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

            #def lines_that_contain(string, fp):
            #    return [line for line in fp if string in line]
            #with open("filename.txt", "r") as fp:
            #    for line in lines_that_contain(cname, fp):
            #        print(line)

            
        if form.validate():
            # Save the comment here.
            # flash('Hello ' + name)
            try:
                print("Cert " + cert_file)
                flash('Download your cert here: ')
                download = 'http://207.148.72.97/certs-file/' + cert_file

            except:
                download = ""
                flash('Not Found ')
        else:
            download = ""
            flash('All the form fields are required. ')
    
        return render_template('hello.html', form=form, value=download)

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
