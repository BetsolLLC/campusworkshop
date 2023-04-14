"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpqlm0u9tun42u47qkg-a.oregon-postgres.render.com",
        database="task_7rwk",
        user="task_7rwk_user",
        password="wAvXf8B4goveJdJ0fjCq32I1c3UaQOTq")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
