#!/usr/bin/env python3
#coding=utf-8
#author="yexiaozhu"

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
