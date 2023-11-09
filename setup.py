
from setuptools import setup

setup(
    name='pswitch',
    version='0.1.0',    
    description='A projects switcher',
    url='',
    author='Stephen Hudson',
    author_email='guillaume.luc.wagner@gmail.com',
    license='BSD 2-clause',
    packages=['pswitch'],
    entry_points={
    'console_scripts': ['pswitch = pswitch.console:main'],
    }
)