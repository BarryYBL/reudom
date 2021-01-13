# coding=utf-8
import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('reudom/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

try:
    with open("description.rst", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = 'Automated testing framework based on requests and unittest interface.'


setup(
    name='reudom',
    version=version,
    url='https://github.com/SeldomQA/reudom/',
    license='BSD',
    author='Barry',
    author_email='YBL2652612315@126.com',
    description='Automated testing framework based on requests and unittest interface.',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests',
        'xlrd',
        'parameterized==0.7.0',
        'jinja2>=2.11.2'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        "Topic :: Software Development :: Testing",
    ],
    entry_points='''
        [console_scripts]
        reudom=reudom.cli:main
    ''',
    py_modules=['whyteboard'],
    scripts=[
        'reudom/TestRunner/html/charts_script.html',
        'reudom/TestRunner/html/heading.html',
        'reudom/TestRunner/html/mail.html',
        'reudom/TestRunner/html/report.html',
        'reudom/TestRunner/html/stylesheet.html',
        'reudom/TestRunner/html/template.html',
    ],
)
