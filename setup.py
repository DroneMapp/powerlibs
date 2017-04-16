try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.0.2'

with open('requirements/production.txt') as requirements_file:
    requires = [line for line in requirements_file]

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='powerlibs',
    version=version,
    description="Python libraries with great power but great simplicity",
    long_description=readme,
    author='Cléber Zavadniak',
    author_email='cleberman@gmail.com',
    url='https://github.com/Dronemapp/powerlibs',
    license=license,
    packages=['powerlibs'],
    package_data={'': ['LICENSE', 'README.md']},
    package_dir={'powerlibs': 'powerlibs'},
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    keywords='generic libraries',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)
