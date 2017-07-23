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
          ],
      dependency_links=[
          "https://github.com/Tumthe3/Pyliner/archive/master.zip#egg=pyliner-1.0",
          "https://github.com/Tumthe3/SQLite-Reader/archive/master.zip#egg=sqlitereader-1.0",
          ],
      license="MIT"
     )
