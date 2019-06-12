# -*- coding: utf-8 -*-
import random

import discord
from discord.ext import commands

from .context import GeneralContext
from . import database
from . import settings
from .settings import config


class General(object):
    """General commands."""

    def __init__(self, bot):
        """
        Args:
            bot(chatbot.Bot): Bot instance.
            
        """
        self.bot = bot

    @commands.command(description="Tells you your user ID.")
    async def getid(self, context):
        user_id = context.author.id
        user_name = context.author.mention        
        await self.bot.say(context.channel, f"{user_name}, your ID is {user_id}")


class Owner(object):
    """Commands usable only by the owner."""

    def __init__(self, bot):
        """
        Args:
            bot(chatbot.Bot): Bot instance.
            
        """
        self.bot = bot

    @commands.command()
    async def shutdown(self, context):
        async def log_out(context):
            try:
                response = self.bot.get_phrase(database.Category.SHUTDOWN.value)
                await self.bot.say(context.channel, response, context)
            finally:
                await self.bot.client.logout()

        async def sass(context):
            response = "Don't tell me what to do."
            await self.bot.say(context.channel, response)

        await self.validate_owner(context, log_out, sass)

    @commands.command()
    async def reconfig(self, context):
        async def read_config(context):
            settings.read_config(self.bot.file_config)
            await self.bot.say(context.channel, "Settings updated.")

        await self.validate_owner(context, read_config)

    async def validate_owner(self, context, function_pass, function_fail=None):
        """ Check if the owner issued the command.

        Args:
            context (discord.Context): Context of the command.
            function_pass (func): Function to call if check passes.
                Must be a coroutine that accepts a GeneralContext object
                as an argument.
            function_fail (func, optional): Function to call if check fails.
                Must be a coroutine that accepts a GeneralContext object
                as an argument. If none provided, bot will give a stock
                warning to the user.

        """
        if context.author.id == config.get("bot", "owner_id"):
            await function_pass(context)
        else:
            try:
                await function_fail(context)
            except TypeError:
                response = "Don't tell me what to do."
                await self.bot.say(context.channel, response)
    
