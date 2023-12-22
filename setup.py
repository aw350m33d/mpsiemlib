from setuptools import setup, find_packages
from mpsiemlib.__metadata__ import __url__, __version__, __author__, __license__, __title__, __description__, __maintainer__

with open("requirements.txt", "r", encoding="utf-8") as fh:
    INSTALL_REQUIRES = fh.readlines()

def readme():
    with open('README.md', 'r') as f:
        return f.read()

setup(
    name=__title__,
    version=__version__,
    packages=find_packages(exclude=['tests']),
    url=__url__,
    license=__license__,
    author=__author__,
    maintainer=__maintainer__,
    author_email='',
    description=__description__,
    long_description=readme(),
    long_description_content_type='text/markdown',
    zip_safe=False,
    python_requires='>=3.7',
    install_requires=INSTALL_REQUIRES,

)
