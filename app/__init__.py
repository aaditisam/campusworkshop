"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi81jt269vf5qbd4kpg-a.oregon-postgres.render.com",
        database="todo_x6y8",
        user="root",
        password="nltrEe5eFeTcae5QFaW4bpHzV0Kq9A2Z")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
