from setuptools import setup, find_packages

setup(
    name='Phagebook',
    version='1.0',
    ppackages=find_packages(),

    install_requires=[
        'Click',
        'colorama',
        'biopython',
    ],
    entry_points='''
        [console_scripts]
        phagebook=phagebook:cli
    '''
)
