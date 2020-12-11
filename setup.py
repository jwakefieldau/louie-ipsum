import setuptools

setuptools.setup(
    name="louie-ipsum",
    version="0.0.1",
    author="James Wakefield",
    author_email="jmw1982@gmail.com",
    description="If you have to ask...",
    url="https://github.com/jwakefieldau/louie-ipsum",
    packages=setuptools.find_packages(),
    #TODO - figure out why this searches pypi instead
    #install_requires = [
    #    'generic_ipsum @ git+https://github.com/jwakefieldau/generic-ipsum#egg=generic_ipsum',
    #]
)
