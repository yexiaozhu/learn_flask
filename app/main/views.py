#!/usr/bin/env python3
#coding=utf-8
#author="yexiaozhu"
from flask import render_template

from . import main


@main.route('/')
def index():
    return render_template('index.html')