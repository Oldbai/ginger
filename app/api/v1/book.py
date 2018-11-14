# blueprint
from flask import Blueprint

from app.libs.redprint import Redprint

api = Redprint('book')


@api.route('/get')
def get_book():
    return 'I am book'
