from setuptools import setup

from enigma_sigma import __version__

setup(
    name='enigma_sigma',
    version=__version__,

    url='https://github.com/marchettomarcelo/Enigma-Sigma',
    author='Marcelo Marchetto e João Alfredo Lamy',
    author_email='marchetto.marcelo@gmail.com',

    py_modules=['enigma_sigma'],
    install_requires=[
        'numpy',
    ],

    
)