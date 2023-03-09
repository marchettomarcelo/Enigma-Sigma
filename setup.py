from setuptools import setup

from my_pip_package import __version__

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/marchettomarcelo/Enigma-Sigma',
    author='Marcelo Marchetto e João Alfredo Lamy',
    author_email='marchetto.marcelo@gmail.com',

    py_modules=['my_pip_package'],
)