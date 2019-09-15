# -*- coding: utf-8 -*-
from setuptools import setup

setup(name="discordion",
      version="0.1.21",
      description="A simple framework for discord chatbots",
      author="LeicaSimile",
      author_email="leicasimile@gmail.com",
      url="https://github.com/LeicaSimile/discordion",
      install_requires=[
          "sqlitehouse==1.2",
          ],
      packages=["discordion"],
      license="MIT"
     )
