from distutils.core import setup
setup(
  name = 'c3covid19',
  packages = ['c3covid19'],
  version = '0.2',
  license='MIT',
  description = 'Python wrapper for easy use of the C3 COVID 19 Data Lake',
  author = 'Connor Makowski',
  author_email = 'connor.m.makowski@gmail.com',
  url = 'https://github.com/connor-makowski/c3covid19',
  download_url = 'https://github.com/connor-makowski/c3covid19/dist/c3covid19-0.1.tar.gz',
  keywords = ['data', 'lake', 'covid19', 'c3', 'c3covid19'],
  install_requires=[
        'requests>=2',
        'pandas>=1'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)
