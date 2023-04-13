"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrqb4g2qv2dcb94bmc0-a.oregon-postgres.render.com",
        database="todo_ywgw",
        user="todo_ywgw_user",
        password="IYoQSEfmEc7TPZftXmycq74RQQ23cKJN")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
