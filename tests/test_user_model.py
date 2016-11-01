#!/usr/bin/env python3
#coding=utf-8
#author="yexiaozhu"

import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):
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