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

    @commands.command(description="Tells you your user ID.", pass_context=True)
    async def getid(self, context):
        user_id = context.message.author.id
        user_name = context.message.author.mention
        
        await self.bot.client.send_message(context.message.channel,
                                           f"{user_name}, your ID is {user_id}")


class Owner(object):
    """Commands usable only by the owner."""

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

    @commands.command(pass_context=True)
    async def changegame(self, context):
        async def change_status(context):
            g = discord.Game(name=context.message)
            await self.bot.client.change_presence(game=g)

        await validate_owner(context, change_status)

    async def validate_owner(self, context, function_pass, function_fail=None):
        """ Check if the owner issued the command.

        Args:
            context (discord.Context): Context of the command.
            function_pass (func): Function to call if check passes.
                Must be a coroutine.
            function_fail (func, optional): Function to call if check fails.
                Must be a coroutine. If none provided, bot will give a stock
                warning to the user.

        """
        context = GeneralContext(context=context)
        if context.user.id == config.get("bot", "owner_id"):
            await function_pass()
        else:
            try:
                function_fail()
            except Exception:
                response = "Don't tell me what to do."
                await self.bot.say(context.channel, message)
    
