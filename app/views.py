# -*- coding: utf-8 -*-

from app import app
from flask import render_template


@app.route('/')
def index():
    from app.models import Todo
    todos = Todo.objects.all()
    return render_template('index.html', todos=todos)
