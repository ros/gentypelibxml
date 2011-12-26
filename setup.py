#!/usr/bin/env python

from setuptools import setup

# from gencpp import __version__

setup(name='gentypelibxml',
#      version=__version__, FIXME
      version="1.0",
      packages=['gentypelibxml'],
      package_dir={'':'src'},
      install_requires=['genmsg'],
      scripts = ['scripts/gen_typelibxml.py'],
      author = "Troy Straszheim",
      author_email = "straszheim@willowgarage.com",
      url = "http://www.ros.org/wiki/gentypelibxml",
      download_url = "http://pr.willowgarage.com/downloads/gentypelibxml/",
      keywords = ["ROS"],
      classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License" ],
      description = "ROS msg/srv C++ generation",
      long_description = """\
Library and scripts for generating typelib xml from ros messages.
""",
      license = "BSD"
      )
