from setuptools import setup, find_packages

setup(
    name='brain',
    version='0.1.0',
    author='Bar Aschner',
    description='Project for advanced system design course.',
    packages=find_packages(),
    install_requires=['pymongo', 'flask_restful', 'flask-cors', 'fire', 'requests', 'protobuf', 'numpy', 'matplotlib',
                      'furl', 'Pillow', 'pika'],
    tests_require=['pytest', 'pytest-cov', 'mongomock', 'codecov', 'requests-mock'],
)
