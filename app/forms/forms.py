from json import loads
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField, RadioField, EmailField, PasswordField)
from wtforms.validators import InputRequired, Length, Email, EqualTo, Regexp, ValidationError

# def read_file(filename, mode="rt"):
#     with open(filename, mode, encoding='utf-8') as fin:
#         return fin.read()

# def check_repeat_name(form, field):
#     data = read_file("app/data/users.json")
#     users = loads(data)
#     repeat = False
#     for user in users:
#         if user["username"] == field.data:
#             repeat = True
#             break
#     if repeat:
#         raise ValidationError("Username already exists.")

# def check_repeat_email(form, field):
#     data = read_file("app/data/users.json")
#     users = loads(data)
#     repeat = False
#     for user in users:
#         if user["email"] == field.data:
#             repeat = True
#             break
#     if repeat:
#         raise ValidationError("Email already exists.")

class CourseForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(min=10, max=100)])
    description = TextAreaField('Course Description', validators=[InputRequired(), Length(max=200)])
    price = IntegerField('Price', validators=[InputRequired()])
    level = RadioField('Level', choices=['Beginner', 'Intermediate', 'Advanced'], validators=[InputRequired()])
    available = BooleanField('Available', default='checked')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=8, max=100)])
    # email = EmailField('Email', validators=[InputRequired(), Length(min=10, max=100), Email(message="Invalid Email."), check_repeat_email])
    email = EmailField('Email', validators=[InputRequired(), Length(min=10, max=100), Email(message="Invalid Email.")])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=100), Regexp("(?=.*\d)(?=.[a-zA-Z])", 0, "Password must contain at least one number")])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), Length(min=10, max=100), EqualTo("password")])