from flask import Flask
from flask_failsafe import failsafe
import pytest


def create_good_app():
  app = Flask(__name__)

  @app.route('/')
  def index():
    return 'Hello'

  return app


def test_good_app():
  app = failsafe(create_good_app)()
  rv = app.test_client().get('/')
  assert b'Hello' in rv.data


class MyException(Exception):
  pass


def create_bad_app():
  raise MyException()


def test_bad_app_without_failsafe():
  with pytest.raises(MyException):
    create_bad_app()


def test_bad_app_with_failsafe():
  # creating the app should not raise an exception
  app = failsafe(create_bad_app)()

  # but fetching the page should
  with pytest.raises(MyException):
    app.test_client().get('/')
