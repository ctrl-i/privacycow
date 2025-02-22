from setuptools import setup

setup(
    name='privacycow',
    version='0.1.0',
    packages=["privacycow"],
    include_package_data=True,
    install_requires=[
        'Click==8.0.1',
        'texttable==1.6.4',
        'requests==2.26.0',
        'Faker>=18.0.0',
        'Unidecode>=1.1.0',
        'questionary>=1.10.0'
    ],
    package_data={'privacycow': ['config.ini.example']},
    entry_points={
        'console_scripts': [
            'privacycow = privacycow.privacycow:cli',
        ],
    },
)
