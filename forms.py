from flask_wtf import FlaskForm
from wtforms import fields, validators
from wtforms_alchemy import ModelForm
from models import GuestBook


class GuestBookForm(ModelForm):
    class Meta:
        model = GuestBook

