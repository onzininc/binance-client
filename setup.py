from setuptools import setup, find_namespace_packages, find_packages

setup(
    name='binance-client',
    version='0.0',
    package_dir={
        'src',
    },
    packages=['binance'],
    include_package_data=True,
    install_requires=[],
)