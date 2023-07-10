from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Load the CSV file and store the data
df = pd.read_csv('path/to/your/csv/file.csv')

# Define the form
class SchoolForm(FlaskForm):
    school_name = StringField('School Name')
    teacher_name = StringField('Name of Teacher in Charge')
    teacher_contact = StringField('Contact Number (+91) of Teacher in Charge')
    student_name = StringField('Name of Student in Charge')
    student_contact = StringField('Contact Number (+91) of Student in Charge')
    student1 = StringField('Student 1')
    student2 = StringField('Student 2')
    student3 = StringField('Student 3')
    submit = SubmitField('Submit')

# Route to display the form
@app.route('/form/<school_code>', methods=['GET', 'POST'])
def form(school_code):
    # Find the corresponding entry based on the school code
    entry = df.loc[df['School Code'] == school_code].squeeze()

    # Pre-populate the form with the entry data
    form = SchoolForm(obj=entry)

    if form.validate_on_submit():
        # Add the entry to another CSV file
        entry.to_csv('path/to/your/new/csv/file.csv', mode='a', header=False, index=False)

        return 'Form submitted successfully!'

    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
