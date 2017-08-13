# -*- coding: utf-8 -*-
from discord.ext import commands

from ..database import DiscordDatabase


def test_init_database():
    db = DiscordDatabase(":memory:")
    assert db is not None

