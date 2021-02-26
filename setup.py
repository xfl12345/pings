# -*- coding:utf-8 -*-

try:
  import setuptools
  from setuptools import setup
except ImportError:
  print("Please install setuptools.")

setup_options = dict(
    name        = "pings",
    description = "Simple ping client in Python 3 by using icmp packet via low level socket.",
    author      = ["satoshi03" , "xfl12345"],
    author_email = "innamisatoshi@gmail.com",
    license     = "GPL",
    url         = "https://github.com/satoshi03/pings",
    classifiers = [
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.6",
      'License :: OSI Approved :: GNU Affero General Public License v3.0 (AGPL-3.0)'
    ]
)
setup_options["version"] = "0.0.1"
setup_options.update(dict(
  packages         = ['pings'],
))

setup(**setup_options)
