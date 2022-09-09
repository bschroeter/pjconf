from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='pjconf',
    version='0.1.0',
    author='Ben Schroeter',
    description='A super simple JSON based configuration system.',
    long_description=long_description,
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6',
    py_modules='pjconf',
    install_requires=[],
    keywords=['configuration', 'config', 'json'],
    url='https://github.com/bschroeter/pjconf'
)