from flask import Flask, render_template, jsonify
# from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField, TimeField
from wtforms import StringField
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'
# app.config['RECAPTCHA_PUBLIC_KEY'] = 'XX'
# app.config['RECAPTCHA_PRIVATE_KEY'] = 'XX'
Bootstrap(app)


class dateForm(FlaskForm):
    DateForm = DateField('Expired Date', format='%Y-%m-%d',
                         validators=[InputRequired(message='Expired date has Required')])
    Username = StringField('Username', validators=[
                           InputRequired('A Username has Required')])
    Time = TimeField('time') 
    # recaptcha = RecaptchaField()


@app.route('/form', methods=['GET', 'POST'])
def index():
    form = dateForm()
    if form.validate_on_submit():
        ret = {
            'username': form.Username.data,
            'unixTime': form.DateForm.data.strftime('%s'),
            'time': str(form.Time.data),
            'ldapTime': (int(form.DateForm.data.strftime('%s')) + 11644473600) * 10000000
        }
        return jsonify({'data': ret})
    return render_template('form.html', form=form)

