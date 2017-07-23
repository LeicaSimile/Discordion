# -*- coding: utf-8 -*-
from setuptools import setup

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
          "git+ssh://git@github.com/Tumthe3/Pyliner.git@master#egg=pyliner-1.0",
          "git+ssh://git@github.com/Tumthe3/SQLite-Reader.git@master#egg=sqlitereader-1.0",
          ],
      license="MIT"
     )
