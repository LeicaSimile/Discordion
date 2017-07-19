# -*- coding: utf-8 -*-
"""For retrieving settings for the bot. Values are set in a config file."""
from configparser import ConfigParser, ExtendedInterpolation


config = ConfigParser(allow_no_value=True, interpolation=ExtendedInterpolation)

def read_settings(filename):
    config.read(filename)
