import os
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))

try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except:
    README = ''
    CHANGES = ''


setup(
    name='Flask-Failsafe',
    version='0.2',
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
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
