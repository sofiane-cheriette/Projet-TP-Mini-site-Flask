"""
Package de l'application Flask - Mini catalogue de jeux vidéo
"""
from flask import Flask

app = Flask(__name__)

from app import routes
