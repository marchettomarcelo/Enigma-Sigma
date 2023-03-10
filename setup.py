from setuptools import setup, find_packages

from enigma_sigma import __version__

setup(
    name='enigma_sigma',
    version=__version__,

    url='https://github.com/marchettomarcelo/Enigma-Sigma',
    author='Marcelo Marchetto e João Alfredo Lamy',
    author_email='marchetto.marcelo@gmail.com',
    packages=find_packages(),
    install_requires=['numpy>=1.21.5'] 

)