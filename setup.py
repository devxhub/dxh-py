from setuptools import setup, find_packages

setup(
    name='devxhub_python',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'cookiecutter>=1.7.0'
    ],
    entry_points={
        'console_scripts': [
            'devxhub_python=devxhub_python.cli:main',
        ],
    },
    author='Jamil Rayhan',
    author_email='jamil.rayhan.bsmrstu@gmail.com',
    description='A custom CLI for generating Django projects with Cookiecutter templates',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/git-jamil/devxhub_python',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license='MIT',
    python_requires='>=3.6',
)
