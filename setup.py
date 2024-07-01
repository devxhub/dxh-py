import os
from setuptools import setup, find_packages

setup(
    name='dxh_py',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'cookiecutter>=2.0.0'
    ],
    entry_points={
        'console_scripts': [
            'dxh_py=dxh_py.cli:main',
        ],
    },
    author='DEVxHUB',
    author_email='tech@devxhub.com',
    description='A python CLI to generate pypi packages.',
    long_description=open('README.md').read() if os.path.exists('README.md') else '',
    long_description_content_type='text/markdown',
    url='https://github.com/devxhub/dxh-py',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license='MIT',
    python_requires='>=3.6',
    include_package_data=True,
    package_data={
        '': ['LICENSE.md'],
    },
)
