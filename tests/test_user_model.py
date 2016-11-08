#!/usr/bin/env python3
#coding=utf-8
#author="yexiaozhu"

import unittest
import time
from app import create_app, db
from app.models import User

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        u = User(password = 'yezi')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password = 'yezi')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password = 'yezi')
        self.assertTrue(u.verify_password('yezi'))
        self.assertFalse(u.verify_password('yezi10'))

    def test_password_salts_are_random(self):
        u = User(password='yezi')
        u2 = User(password='yezi')
        self.assertTrue(u.password_hash != u2.password_hash)

    def test_valid_confirmation_token(self):
        u = User(password='yezi')
        db.session.add(u)
        db.session.commit()
        token = u.generate_confirmation_token()
        self.assertTrue(u.confirm(token))

    def test_invalid_confirmation_token(self):
        u1 = User(password='yezi')
        u2 = User(password='yezi1')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        token = u1.generate_confirmation_token()
        self.assertTrue(u2.confirm(token))

    def test_expired_confirmation_token(self):
        u = User(password='yezi')
        db.session.add(u)
        db.session.commit()
        token = u.generate_confirmation_token()
        time.sleep(2)
        self.assertTrue(u.confirm(token))
