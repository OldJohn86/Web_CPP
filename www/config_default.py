#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

# config_default.py
__author__ = 'Johnny Chen'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '1q2w3e4R',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}
