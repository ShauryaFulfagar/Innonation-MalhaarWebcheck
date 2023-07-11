from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
import pandas as pd
import csv

from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
@app.route('/')
def hello():
    return render_template('Scanner.html')

# Load the CSV file and store the data
with open(
        'D:\PycharmProjects\Innonation-MalhaarWebcheck\Event Registration (Responses) - Form Responses 1.csv') as icsv:
    heading = next(icsv)
    reader = csv.reader(icsv)
    entries = list(reader)


# Define the form
class SchoolForm(FlaskForm):
    school_name = StringField('School Name')
    teacher_name = StringField('Name of Teacher in Charge')
    teacher_contact = StringField('Contact Number (+91) of Teacher in Charge')
    student_name = StringField('Name of Student in Charge')
    student_contact = StringField('Contact Number (+91) of Student in Charge')
    participate1 = BooleanField('Are you participating?')
    student1 = StringField('Student 1')
    student2 = StringField('Student 2')
    student3 = StringField('Student 3')
    participate2 = BooleanField('Are you participating?')
    student4 = StringField('Student 1')
    student5 = StringField('Student 2')
    student6 = StringField('Student 3')
    participate3 = BooleanField('Are you participating?')
    student7 = StringField('Student 1')
    student8 = StringField('Student 2')
    student9 = StringField('Student 3')
    submit = SubmitField('Submit')


# Route to display the form
@app.route('/form/<school_code>', methods=['GET', 'POST'])
def form(school_code):
    # Find the corresponding entry based on the school code
    entry = next((entry for entry in entries if entry[0] == school_code), None)
    print(entry)
    # Pre-populate the form with the entry data
    form = SchoolForm(school_name=entry[1], teacher_name=entry[2], teacher_contact=entry[3], student_name=entry[4],student_contact=entry[5],student1=entry[7],student2=entry[8],student3=entry[9],student4=entry[11],student5=entry[12],student6=entry[13],student7=entry[15],student8=entry[16],student9=entry[17])

    # Assign entry values to form fields

    # form.school_name.default = entry[1]
    # form.teacher_name.default = entry[2]
    # form.teacher_contact.default = entry[3]
    # form.student_name.default = entry[4]
    # form.student_contact.default = entry[5]
    # form.participate1.default = entry[6] == 'Yes'
    # form.student1.default = entry[7]
    # form.student2.default = entry[8]
    # form.student3.default = entry[9]
    # form.participate2.default = entry[10] == 'Yes'
    # form.student4.default = entry[11]
    # form.student5.default = entry[12]
    # form.student6.default = entry[13]
    # form.participate3.default = entry[14] == 'Yes'
    # form.student7.default = entry[15]
    # form.student8.default = entry[16]
    # form.student9.default = entry[17]
    # form.process()
    # If the form is submitted and valid, add the data to a new csv file named "output.csv"

    if form.validate_on_submit():

        with open('D:\PycharmProjects\Innonation-MalhaarWebcheck\output.csv', 'a') as ocsv:

            formData = [school_code, form.school_name.data, form.teacher_name.data,
                                 form.teacher_contact.data, form.student_name.data, form.student_contact.data,
                                 form.participate1.data, form.student1.data, form.student2.data, form.student3.data,
                                 form.participate2.data, form.student4.data, form.student5.data, form.student6.data,
                                 form.participate3.data, form.student7.data, form.student8.data, form.student9.data]

            print(formData)
            writer = csv.writer(ocsv)
            writer.writerow(formData)

        return render_template('thank_you.html')
    return render_template('form.html', form=form, display1="block" if entry[6] == 'Yes' else "none",
                           display2="block" if entry[10] == 'Yes' else "none",
                           display3="block" if entry[14] == 'Yes' else "none")


if __name__ == '__main__':
    app.run(debug=False)
