# -*- coding: utf-8 -*-
"""Settings used for the bot. Values are set in chatbot.Bot"""

"""Files"""
DATABASE_MANUAL = ""  # Records are typically set by bot owner
DATABASE_AUTO = "bot.db"    # Records are automatically set by bot

"""Private settings"""
BOT_ID = ""
OWNER_ID = ""
SECRET = ""
TOKEN = ""

"""Other bot settings"""
BOT_PREFIX = "!"
BOT_STATUS = f"{BOT_PREFIX}help"

"""Placeholders for variables in phrases"""
BOT_DISPLAY_NAME = "%botnick%"
BOT_NAME = "%bot%"
CHANNEL_NAME = "%channel%"
DISPLAY_NAME = "%display%"
EMOTE = "%ACT"
MENTION = "%mention%"
SERVER_NAME = "%server%"
USER_NAME = "%name%"

"""Database tables and headers"""
TABLE_PHRASES = "phrases"
HEADER_PHRASES_PHRASE = "phrase"
HEADER_PHRASES_CATEGORY = "category_id"
