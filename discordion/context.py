# -*- coding: utf-8 -*-
from discord.ext.commands import context

from . import settings


class GeneralContext(context.Context):
    """Expanded version of the Discord Context class.

    This class can be used outside of command functions, such as
    inside event handlers. It needs to be created manually.

    Attributes:
        channel(discord.Channel): The channel the event took place in.
        context(discord.Context): The Context object automatically created by Discord.
        server(discord.Server): The server the event took place in.
        user(discord.Member/User): The user associated with the event.
        argument(string): The part of the message that isn't the command or prefix.

    """

    def __init__(self, **attrs):
        attrs["prefix"] = settings.config.get("bot", "prefix")
        super().__init__(**attrs)
        self.context = attrs.pop("context", None)
        self.argument = ""

        self._extract_message()

    def _extract_message(self):
        """Assigns some of the message variables to this class's variables."""
        if self.context:
            self.args = self.context.args
            self.kwargs = self.context.kwargs
            self.prefix = self.context.prefix
            self.command = self.context.command
            self.view = self.context.view
            self.invoked_with = self.context.invoked_with
            self.invoked_subcommand = self.context.invoked_subcommand
            self.subcommand_passed = self.context.subcommand_passed

            split_message = self.message.content.split(self.invoked_with, 1)
            if self.invoked_with and len(split_message) > 1:
                self.argument = split_message[1].lstrip()
