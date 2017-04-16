# -*- coding: utf-8 -*-
# 初始化app包

from flask import Flask
from flask_mongoengine import MongoEngine
from xcore.db.xredis import XRedis

app = Flask(__name__)
app.config.from_object('config')

db = MongoEngine(app)

redis = XRedis()
redis.init_app(app)

from app import views, models
