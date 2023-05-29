from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'With This Package Can You Find Out Get Info Any Token Telegram Bot from https://api.telegram.org'
LONG_DESCRIPTION = 'With This Package Can You Find Out Get Info Any Token Telegram Bot from https://api.telegram.org'

# Setting up
setup(
    name="infobot",
    version=VERSION,
    author="Muamel Ameer",
    author_email="amowallet@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['telegramapi','info','bot','telegram bots'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    url='https://github.com/muamelAmeer/infobot/',
    project_urls={
        'Source': 'https://github.com/muamelAmeer/infobot',
        'Dev Lib': 'https://github.com/muamelAmeer',
        'Documentation': 'https://github.com/muamelAmeer/infobot'
    },
)
