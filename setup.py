from setuptools import setup, find_packages


with open('README.rst') as f:
    description = f.read()


setup(
    name='bridson',
    url='http://github.com/emulbreh/bridson/',
    version='0.1.0',
    packages=find_packages(),
    license=u'BSD License',
    author=u'Johannes Dollinger',
    description=u'poisson disc sampling of 2-dimensional',
    long_description=description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ]
)
