# -*- coding: utf-8 -*-
import configparser
import logging

import discord
import discord.ext.commands
import pyliner
import sqlitehouse

from .context import GeneralContext
from . import commands
from . import settings
from .settings import config


class Bot(object):
    """
    Args:
        bot (discord.Bot): The bot instance.
        file_config (str): Filepath of config file with bot's settings.
        
    Attributes:
        db (BotDatabase): The bot's database.
        
    """
    
    def __init__(self, file_config, logger=None, **options):
        self.logger = logger or logging.getLogger(__name__)
        self.file_config = file_config
        settings.read_settings(self.file_config)
        command_prefix = config.get("bot", "prefix")
        description = config.get("bot", "description")

        self.client = discord.ext.commands.Bot(command_prefix=command_prefix, description=description, **options)
        self.db_manual = sqlitehouse.Database(config.get("files", "database_manual"))
        self.db_auto = sqlitehouse.Database(config.get("files", "database_auto"))

    def run(self):
        self.set_events()
        self.set_commands()
        self.client.run(config.get("bot", "token"))

    def event_ready(self):
        """Override on_ready"""
        async def on_ready():
            prefix = config.get("bot", "prefix")
            self.logger.info(f"{self.client.user.name} is now online.")
            self.logger.info(f"ID: {self.client.user.id}")
            self.logger.info(f"Command prefix: {prefix}")

            status = config.get("bot", "status")
            await self.client.change_presence(activity=discord.Game(name=status))

        return on_ready

    def get_phrase(self, category):
        """ Shortcut for getting a random phrase from the database.

        Args:
            category(unicode): The phrase category - see enum 'Category' in phrases.py.

        """
        header_phrase = config.get("headers", "phrases_phrase")
        header_category = config.get("headers", "phrases_category")
        table = config.get("tables", "phrases")
        
        return self.db_manual.random_line(header_phrase, table, {header_category: category})

    def parse(self, text, context=None, substitutions=None):
        """ Interprets a string and formats accordingly, substitutes values, etc.

        Args:
            text(unicode): String to parse.
            context(GeneralContext, optional): Current context of the message.
            substitutions(dict, optional): Other substitutions to perform.
                Replaces key with corresponding value.

        Returns:
            text(unicode): Parsed string.

        """
        if not substitutions: substitutions = {}
        text = pyliner.parse_all(text)

        ph_bot_name = config.get("placeholders", "bot_name")
        ph_bot_display = config.get("placeholders", "bot_display")
        ph_emote = config.get("placeholders", "emote")
        ph_channel = config.get("placeholders", "channel_name")
        ph_user_display = config.get("placeholders", "user_display")
        ph_mention = config.get("placeholders", "mention")
        ph_user_name = config.get("placeholders", "user_name")
        ph_server = config.get("placeholders", "server_name")

        ## Add context variables to substitutions.
        substitutions[ph_bot_name] = self.client.user.name
        substitutions[ph_bot_display] = self.client.user.display_name
        substitutions[ph_emote] = "/me"

        try:
            ## Channel variables
            substitutions[ph_channel] = context.channel.name
        except AttributeError:
            substitutions[ph_channel] = ""
            
        try:
            ## User (author) variables
            substitutions[ph_user_display] = context.user.display_name
            substitutions[ph_mention] = context.user.mention
            substitutions[ph_user_name] = context.user.name
        except AttributeError:
            substitutions[ph_user_display] = ""
            substitutions[ph_mention] = ""
            substitutions[ph_user_name] = ""
            
        try:
            ## Server variables
            substitutions[ph_server] = context.guild.name
        except AttributeError:
            substitutions[ph_server] = ""

        for s in substitutions:
            if not substitutions[s]:
                substitutions[s] = ""
                
            text = text.replace(s, substitutions[s])
            self.logger.debug(f"parse(): {text} (replaced '{s}' with '{substitutions[s]}')")
        
        return text

    async def say(self, message, context=None):
        msg = self.parse(message, context)
        await message.channel.send(content=msg)
    
    def set_commands(self, *cmds):
        for c in cmds:
            self.client.add_cog(c)
        
    def set_events(self, *events):
        self.client.event(self.event_ready())

        for e in events:
            self.client.event(e)
            
