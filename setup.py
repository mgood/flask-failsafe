import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

try:
  README = open(os.path.join(here, 'README.rst')).read()
  CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except:
  README = ''
  CHANGES = ''


setup(
  name='Flask-Failsafe',
  version='0.1',
  url='http://github.com/mgood/flask-failsafe',
  license='BSD',
  author='Matt Good',
  author_email='matt@matt-good.net',
  description='A failsafe for the Flask reloader',
  long_description=README + '\n\n' + CHANGES,
  zip_safe=True,
  platforms='any',
  py_modules=['flask_failsafe'],
  install_requires=[
    'Flask>=0.8',
  ],
)
