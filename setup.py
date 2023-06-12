from setuptools import setup, find_packages

REQUIRES = [
    'requests',
    'allure-pytest',
    'pydantic'
]

setup(
    name='dm_api_account',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/surovp/dm_api_account.git',
    license='MIT',
    author='Pavel Surov',
    author_email='-',
    install_requires=REQUIRES,
    description='library with apis and models'
)
