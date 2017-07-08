# -*- coding: utf-8 -*-
"""Sample settings file. Customize values to your needs."""
import configparser


"""Files"""
FILE_DATABASE = ""
FILE_CONFIG = "config.ini"

config = configparser.SafeConfigParser()
config.read(FILE_CONFIG)


"""Settings from config file"""
BOT_ID = config.get("info", "id")
OWNER_ID = config.get("info", "owner-id")
SECRET = config.get("info", "secret")
TOKEN = config.get("info", "token")

"""Other bot settings"""
BOT_PREFIX = "!"
BOT_STATUS = f"{BOT_PREFIX}help"

"""Placeholders for variables in phrases"""
BOT_DISPLAY_NAME = "%botnick%"
BOT_NAME = "%bot%"
CHANNEL_NAME = "%channel%"
DISPLAY_NAME = "%nick%"
EMOTE = "%ACT"
MENTION = "%mention%"
SERVER_NAME = "%server%"
USER_NAME = "%name%"
