from setuptools import setup

setup(name='chirospython',
      version='0.2',
      description='Chiros api for Alfred',
      url='none',
      author='Sebastien Lubineau',
      author_email='non',
      license='MIT',
      packages=['chirospython'],
      install_requires=[
          'Flask',
          'requests'
      ],
      zip_safe=False)