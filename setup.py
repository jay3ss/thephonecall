from setuptools import setup, find_packages


description = 'Contains the text from the memorandum ',
              'of the July 25, 2019 phone call'

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='The Phone Call',
    version='0.0.1',
    description=description,
    long_description=readme,
    author='Jay Ess',
    include_package_data=True,
    license='MIT',
    license_file=license,
    url='https://github.com/jay3ss/thephonecall'
)
