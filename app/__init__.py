"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpqql8rddl9mmogtj20-a.oregon-postgres.render.com",
        database="todo_jg13",
        user="todo_jg13_user",
        password="BiZdxk3x4wGxtfDg2b3OqWylb0ATPN6S")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
