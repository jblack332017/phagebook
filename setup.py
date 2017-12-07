from setuptools import setup

setup(
    name='Phagebook',
    version='1.0',
    py_modules=['Phagebook'],

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
