# -*- coding: utf-8 -*-
import sqlite3
from enum import Enum

import pyliner
from sqlitehouse import Database, TableColumn

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

    def setup(self):
        """Initializes database if there is none."""
        tbl_servers = config.get("tables", "servers")
        head_serverid = config.get("headers", "servers_id")
        head_server = config.get("headers", "servers_server")
        col_servers = [
            TableColumn(head_serverid, "INTEGER", primary_key=True),
            TableColumn(head_server, "TEXT")
            ]
        self.create_table(tbl_servers, col_servers)

        tbl_users = config.get("tables", "users")
        head_userid = config.get("headers", "users_id")
        head_user = config.get("headers", "users_user")
        col_users = [
            TableColumn(head_userid, "INTEGER", primary_key=True),
            TableColumn(head_user, "TEXT")
            ]
        self.create_table(tbl_users, col_users)

    def add_server(self, server):
        """Adds a server record to the database.

        Args:
            server (discord.Server): Server to add.

        """
        table = config.get("tables", "servers")
        head_id = config.get("headers", "servers_id")
        head_name = config.get("headers", "servers_server")
        
        cols = [head_id, head_name]
        vals = [server.id, server.name]
        self.insert(table, vals, cols)

    def remove_server(self, server):
        """Removes a server from the database.

        Args:
            server (discord.Server): Server to remove.

        """
        pass

    def add_user(self, user):
        """Adds a user record to the database.

        Args:
            user (discord.User): User to add.
            
        """
        pass

    def remove_user(self, user):
        """Removes a user from the database.

        Args:
            user (discord.User): User to remove.
            
        """
        pass


class BotDatabase(DiscordDatabase):
    """An extension of DiscordDatabase for functions specific to the bot."""

    def add_song(self, url):
        """Adds a song to the database.

        Args:
            url (str): URL of the song.

        """
        pass

    def add_playlist(self, name, user):
        """Adds a playlist to the database.

        Playlists are bound to one user across all servers.

        Args:
            name (str): Name of the playlist.
            user (discord.Member/User): User who made the playlist.

        """
        pass

    def add_playlist_song(self, song, playlist):
        """Adds a song to a playlist.

        Args:
            song(): Song to add.
            playlist(): The target playlist.

        """
        pass
    
