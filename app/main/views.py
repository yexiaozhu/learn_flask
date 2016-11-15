#!/usr/bin/env python3
#coding=utf-8
#author="yexiaozhu"
from flask import abort
from flask import render_template
from ..models import User
from . import main


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)