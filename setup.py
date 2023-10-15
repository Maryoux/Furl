"""Setup for Furl"""
from setuptools import setup, find_packages
with open('README.md', encoding='utf-8') as f:
    desc = f.read()
setup(
    name='furl',
    version='1.0.2',
    author='Maryoux',
    description='Mining URLs parameter from Wayback',
    packages=find_packages(),
    install_requires=[
        'colorama',
        'pyfiglet',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'furl = furl.furl:main'
        ]
    },
    license='MIT',
    long_description=desc,
    long_description_content_type='text/plain'  # Change to 'text/markdown' if using Markdown
)
