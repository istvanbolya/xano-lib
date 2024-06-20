from setuptools import setup

from xano_echo import __version__

setup(
    name='xano-lib',
    version=__version__,

    url='https://github.com/istvanbolya/xano-lib',
    author='Istvan Bolya',
    author_email='istvan.bolya84@gmail.com',

    py_modules=['xano_echo'],
)
