"""dxh_py distutils configuration."""

from pathlib import Path

from setuptools import setup


def _get_version() -> str:
    """Read dxh_py/VERSION.txt and return its contents."""
    path = Path("dxh_py").resolve()
    version_file = path / "VERSION.txt"
    return version_file.read_text().strip()


version = _get_version()


with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()


requirements = [
    'binaryornot>=0.4.4',
    'Jinja2>=2.7,<4.0.0',
    'click>=7.0,<9.0.0',
    'pyyaml>=5.3.1',
    'python-slugify>=4.0.0',
    'requests>=2.23.0',
    'arrow',
    'rich',
]

setup(
    name='dxh_py',
    version=version,
    description='A Python CLI tool to generate PyPI packages effortlessly.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='DEVxHUB',
    author_email='tech@devxhub.com',
    url='https://github.com/devxhub/dxh-py',
    packages=['dxh_py'],
    package_dir={'dxh_py': 'dxh_py'},
    entry_points={
        'console_scripts': [
            'dxh_py = dxh_py.__main__:main'
            ]
        },
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=requirements,
    license='MIT',
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
    keywords=[
        "dxh_py",
        "Python",
        "projects",
        "project templates",
        "Jinja2",
        "skeleton",
        "scaffolding",
        "project directory",
        "package",
        "packaging",
    ],
)
