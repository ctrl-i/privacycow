from setuptools import setup

setup(
    name='privacycow',
    version='0.0.5',
    packages=["privacycow"],
    include_package_data=True,
    install_requires=[
        'Click==8.0.1',
        'texttable==1.6.4',
        'requests==2.26.0',
    ],
    package_data={'privacycow': ['config.ini.example']},
    entry_points={
        'console_scripts': [
            'privacycow = privacycow.privacycow:cli',
        ],
    },
)
