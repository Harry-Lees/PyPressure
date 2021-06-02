import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()

setup(
    name='PyPressure',
    version='1.0.0',
    description='Simple Pressure conversion library',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/Harry-Lees/PyPressure',
    author='Harry Lees',
    author_email='harry.lees@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    packages=['pypressure'],
    include_package_data=True,
)