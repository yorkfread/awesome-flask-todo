# -*- coding: utf-8 -*-

from app import app
from flask import render_template, request, redirect, url_for
from app.forms import TodoForm
from app.models import Todo


@app.route('/')
def index():
    todos = Todo.objects.all()
    return render_template('index.html', todos=todos, form=TodoForm())


@app.route('/add/', methods=['POST', ])
def add():
    form = TodoForm()
    if form.validate_on_submit():
        content = request.form.get('content')
        if content:
            todo = Todo(content=content)
            todo.save()
    todos = Todo.objects.all()
    return render_template('index.html', todos=todos, form=form)


def is_done(isdone, todo_id):
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.status = 1 if isdone else 0
    todo.save()


@app.route('/done/<string:todo_id>/')
def done(todo_id):
    is_done(True, todo_id)
    return redirect(url_for('index'))


@app.route('/undone/<string:todo_id>/')
def undone(todo_id):
    is_done(False, todo_id)
    return redirect(url_for('index'))


@app.route('/delete/<string:todo_id>/')
def delete(todo_id):
    todo = Todo.objects.get_or_404(id=todo_id)
    todo.delete()
    return redirect(url_for('index'))
