# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:18:21 2024

@author: Prasad
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)