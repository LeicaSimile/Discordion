# -*- coding: utf-8 -*-
import configparser
import logging

import discord
import pyliner
import sqlitereader

from context import GeneralContext
import commands
import settings

logger = logging.getLogger(__name__)


class Bot(object):
    """
    Args:
        bot (discord.Bot): The bot instance.

    Kwargs:
        db_manual (str): Filepath of the main database file. Records here are
            managed by the owner, containing the bot's phrases and other settings.
        bot_id (str): Bot's client ID.
        owner_id (str): Owner's ID.
        token (str): Bot's token.
        db_auto (str): Filepath of the database file managed by the bot.
            All records here are managed automatically.
        secret (str, optional): Bot's client secret.
        prefix (str, optional): The command prefix.
        status (str, optional): The bot's "Playing" status message.
        placeholder_bot_display (str, optional): Placeholder for bot's
            display name.
        placeholder_bot (str, optional): Placeholder for bot's username.
        placeholder_channel (str, optional): Placeholder for current
            channel's name.
        placeholder_display (str, optional): Placeholder for user's display name.
        placeholder_emote (str, optional): Placeholder for "/me".
        placeholder_mention (str, optional): Placeholder for user mention.
        placeholder_server (str, optional): Placeholder for current
            server's name.
        placeholder_user (str, optional): Placeholder for the user's name.
        
    Attributes:
        db (BotDatabase): The bot's database.
        
    """
    
    def __init__(self, bot, **kwargs):
        self.client = bot
        self.set_settings(**kwargs)
        self.db_manual = sqlitereader.Database(settings.DATABASE_MANUAL)
        self.db_auto = sqlitereader.Database(settings.DATABASE_AUTO)

    def run(self, token):
        self.set_events()
        self.set_commands()
        self.client.run(token)

    def set_settings(**kwargs):
        ## Mandatory arguments
        settings.DATABASE_MANUAL = kwargs["db_manual"]
        settings.BOT_ID = kwargs["bot_id"]
        settings.OWNER_ID = kwargs["owner_id"]
        settings.TOKEN = kwargs["token"]

        ## Optional arguments
        settings.DATABASE_AUTO = kwargs.get("db_auto", "bot.db")
        settings.BOT_PREFIX = kwargs.get("prefix", "!")
        settings.BOT_STATUS = kwargs.get("status", f"{settings.BOT_PREFIX}help")
        settings.BOT_DISPLAY_NAME = kwargs.get("placeholder_bot_display",
                                               "%botnick%")
        settings.BOT_NAME = kwargs.get("placeholder_bot", "%bot%")
        settings.CHANNEL_NAME = kwargs.get("placeholder_channel", "%channel%")
        settings.DISPLAY_NAME = kwargs.get("placeholder_display", "%display%")
        settings.EMOTE = kwargs.get("placeholder_emote", "%ACT")
        settings.MENTION = kwargs.get("placeholder_mention", "%mention%")
        settings.SERVER_NAME = kwargs.get("placeholder_server", "%server%")
        settings.USER_NAME = kwargs.get("placeholder_user", "%name%")

    def event_member_join(self):
        async def on_member_join(member):
            server = member.server
            response = self.get_phrase(phrases.Category.GREET.value)
            ctx = GeneralContext(server=server, user=member)
            
            response = self.parse(response, context=ctx)
            await self.client.send_message(server, response)

        return on_member_join

    def event_ready(self):
        async def on_ready():
            logger.info(f"{self.client.user.name} is now online.")
            logger.info(f"ID: {self.client.user.id}")
            logger.info(f"Command prefix: {settings.BOT_PREFIX}")

            status = settings.BOT_STATUS
            await self.client.change_presence(game=discord.Game(name=status))

        return on_ready

    def get_phrase(self, category):
        """ Shortcut for getting a random phrase from the database.

        Args:
            category(unicode): The phrase category - see enum 'Category' in phrases.py.
        """
        return self.db_manual.random_line("line", "phrases", {"category_id": category})

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
        text = phrases.parse_all(text)

        ## Add context variables to substitutions.
        substitutions[settings.BOT_DISPLAY_NAME] = self.client.user.name
        substitutions[settings.BOT_NAME] = self.client.user.display_name
        substitutions[settings.EMOTE] = "/me"

        try:
            ## Channel variables
            substitutions[settings.CHANNEL_NAME] = context.channel.name
        except AttributeError:
            substitutions[settings.CHANNEL_NAME] = ""
            
        try:
            ## User (author) variables
            substitutions[settings.DISPLAY_NAME] = context.user.display_name
            substitutions[settings.MENTION] = context.user.mention
            substitutions[settings.USER_NAME] = context.user.name
        except AttributeError:
            substitutions[settings.DISPLAY_NAME] = ""
            substitutions[settings.MENTION] = ""
            substitutions[settings.USER_NAME] = ""
            
        try:
            ## Server variables
            substitutions[settings.SERVER_NAME] = context.server.name
        except AttributeError:
            substitutions[settings.SERVER_NAME] = ""

        for s in substitutions:
            if not substitutions[s]:
                substitutions[s] = ""
                
            text = text.replace(s, substitutions[s])
            logger.debug(f"parse(): {text} (replaced '{s}' with '{substitutions[s]}')")
        
        return text

    async def say(self, destination, message, context=None):
        message = self.parse(message, context)
        await self.client.send_message(destination, message)
    
    def set_commands(self, *commands):
        self.client.add_cog(commands.General(self))
        self.client.add_cog(commands.Debugging(self))
        
        for c in commands:
            self.client.add_cog(c)
        
    def set_events(self, *events):
        self.client.event(self.event_ready())
        self.client.event(self.event_member_join())

        for e in events:
            self.client.event(e)
            
