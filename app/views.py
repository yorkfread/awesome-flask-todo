# -*- coding: utf-8 -*-

from app import app
from flask import render_template, request, redirect, url_for
from app.models import Todo


@app.route('/')
def index():
    from app.models import Todo
    todos = Todo.objects.all()
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST', ])
def add():
    content = request.form.get('content')
    if content:
        todo = Todo(content=content)
        todo.save()
        return redirect(url_for('index'))
