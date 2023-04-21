"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch138rj3cv203buj58lg-a.oregon-postgres.render.com",
        database="todo_2cb0",
        user="todo_2cb0_user",
        password="cANnXCYnr2ZqG9gDD9R84q5qt753Gzh8")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
