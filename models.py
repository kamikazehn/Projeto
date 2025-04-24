# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(128), nullable=False)
    api_key = db.Column(db.String(128), default="", nullable=True)
    api_secret = db.Column(db.String(128), default="", nullable=True)
    symbols = db.Column(db.String(256), default="", nullable=True)
    capital = db.Column(db.Float, default=0.0, nullable=True)
    lucro_percentual = db.Column(db.Float, default=1.0, nullable=True)
