# -*- coding: utf-8 -*-
import random

import discord
from discord.ext import commands

from .context import GeneralContext
from . import database
from .settings import config


class General(object):
    """General commands."""

    def __init__(self, bot):
        """
        Args:
            bot(chatbot.Bot): Bot instance.
        """
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def shutdown(self, context):
        context = GeneralContext(context=context)
        if context.user.id == config.get("bot", "owner_id"):
            try:
                response = self.bot.get_phrase(database.Category.SHUTDOWN.value)
                
                await self.bot.say(context.channel, response, context)
            finally:
                await self.bot.client.logout()
        else:
            response = "Don't tell me what to do."
            await self.bot.say(context.channel, message)


class Debugging(object):
    """Commands for debugging and testing."""

    def __init__(self, bot):
        """
        Args:
            bot(chatbot.Bot): Bot instance.
        """
        self.bot = bot

    @commands.command(description="Tells you your user ID.", pass_context=True)
    async def getid(self, context):
        user_id = context.message.author.id
        user_name = context.message.author.mention
        
        await self.bot.client.send_message(context.message.channel,
                                           f"{user_name}, your ID is {user_id}")

