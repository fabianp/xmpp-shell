__version__ = '0.1'

from distutils.core import setup

CLASSIFIERS = """\
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved
Programming Language :: Python
Programming Language :: Python :: 3
Topic :: Software Development
Operating System :: POSIX
Operating System :: Unix

"""

setup(
    name='xmpp-shell',
    description='A module for monitoring memory usage of a python program',
    long_description=open('README.rst').read(),
    version=__version__,
    author='Fabian Pedregosa',
    author_email='fabian@fseoane.net',
    scripts='xmpp-shell',
    url='http://pypi.python.org/pypi/xmpp-shell',
    classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],

)