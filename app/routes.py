from app import myobj
from flask import render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

name = "Alex"
city_names = ["New York", "Paris", "Milano", "London"]


@myobj.route("/", methods=["GET", "POST"])
def home():
    form = Form()
    if form.validate_on_submit():
        flash(form.city.data)
    return render_template("home.html", name=name, city_names=city_names, form=form)


class Form(FlaskForm):
    city = StringField("City Name", validators=[DataRequired(), Length(max=32)])
    submit = SubmitField()
