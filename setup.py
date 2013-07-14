from distutils.core import setup

setup(name='satin',
      version='0.1.0',
      description='UI testing library for PyQt',
      author='Tuukka Turto',
      author_email='tuukka.turto@oktaeder.net',
      url='https://github.com/tuturto/satin-python/',
      packages=['satin', 'satin.test'],
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'Environment :: X11 Applications :: Qt',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Topic :: Software Development :: Testing'])
