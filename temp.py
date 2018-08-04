
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}