# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, Length


# max_length=20
class TodoForm(FlaskForm):
    content = StringField('content', validators=[DataRequired('* 请输入备忘内容'), Length(1, 20, '* 请检查你输入内容,保持在20字节内')])
    time = DateTimeField('time')
    status = IntegerField('status')
