from setuptools import setup, find_packages

setup(
    name='binance-client',
    version='0.0',
    package_dir={
        '': 'src',
    },
    packages=find_packages(where='src'),
    include_package_data=True,
    install_requires=[],
)