# -*- coding: utf-8 -*-

from app import app, redis
from flask import render_template, request, redirect, url_for
from app.forms import TodoForm
from app.models import Todo
from datetime import datetime


@app.route('/')
def index():
    errors = redis.hget('user_id', 'errors')
    redis.hdel('user_id', 'errors')
    if errors:
        try:
            errors = eval(errors)
        except:
            print('转换表单校验errors出错')
    form = TodoForm()
    todos = Todo.objects.all().order_by('-time')
    return render_template('index.html', todos=todos, form=form, errors=errors)


@app.route('/add/', methods=['POST', ])
def add():
    form = TodoForm()
    if form.validate_on_submit():
        content = request.form.get('content')
        if content:
            todo = Todo(content=content, time=datetime.now())
            print(todo.time)
            todo.save()
    redis.hset('user_id', 'errors', form.content.errors)
    return redirect(url_for('index'))


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


@app.errorhandler(404)
def not_found(error):
    error = '很抱歉,没有找到你选择的页面...'
    return render_template('error.html', error=error)
