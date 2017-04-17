# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, Length


class TodoForm(FlaskForm):
    content = StringField('content', validators=[DataRequired('* 请输入备忘内容'), Length(1, 40, '* 请检查你输入内容,保持在40字节内')])
    time = DateTimeField('time', )
    status = IntegerField('status', default=0)
