# -*- coding: utf-8 -*-
from distutils.core import setup

setup(name="discordion",
      version="0.1.1",
      description="",
      author="Angelica Catalan",
      packages=["discordion"],
      install_requires=[
          "pyliner==1.0",
          "sqlitereader==1.0",
          ]
      dependency_links=[
          "git+https://github.com/Tumthe3/Pyliner.git#egg=pyliner-1.0",
          "git+https://github.com/Tumthe3/SQLite-Reader.git#egg=sqlitereader-1.0",
          ],
      license="MIT"
     )
