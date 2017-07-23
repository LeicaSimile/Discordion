# -*- coding: utf-8 -*-
import sqlite3
from enum import Enum

import pyliner
from sqlitehouse import Database

from .settings import config

## === Classes === ##
class Category(Enum):
    """Categories in the database"""
    GREET = "3"
    LEFT_SERVER = "5"
    MENTION = "6,7"
    ONLINE = "8"
    SHUTDOWN = "9"


class DiscordDatabase(Database):
    """An extension of Database for Discord."""

    def add_server(self, server):
        """ Adds a server record to the database.

        Args:
            server(discord.Server): Server to add.

        """
        pass

    def remove_server(self, server):
        """ Removes a server from the database.

        Args:
            server(discord.Server): Server to remove.

        """
        pass


class BotDatabase(DiscordDatabase):
    """An extension of DiscordDatabase for functions specific to the bot."""

    def add_song(self, url):
        """ Adds a song to the database.

        Args:
            url(str): URL of the song.

        """
        pass

    def add_playlist(self, name, user):
        """ Adds a playlist to the database.

        Playlists are bound to one user across all servers.

        Args:
            name(str): Name of the playlist.
            user(discord.Member/User): User who made the playlist.

        """
        pass

    def add_playlist_song(self, song, playlist):
        """ Adds a song to a playlist.

        Args:
            song(): Song to add.
            playlist(): The target playlist.

        """
        pass
    
