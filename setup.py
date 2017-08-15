# -*- coding: utf-8 -*-
from setuptools import setup

setup(name="discordion",
      version="0.1.1",
      description="A simple framework for discord chatbots",
      author="Tumthe3",
      author_email="tumthe3@gmail.com",
      url="https://github.com/Tumthe3/Discordion",
      install_requires=[
          "pyliner==1.0",
          "sqlitehouse==1.1",
          ],
      packages=["discordion"],
      license="MIT"
     )
