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
        table = config.get("tables", "servers")
        header = config.get("headers", "servers_id")
        self.delete(table, conditions={header: server.id})

    def add_user(self, user):
        """Adds a user record to the database.

        Args:
            user (discord.User): User to add.
            
        """
        table = config.get("tables", "users")
        head_id = config.get("headers", "users_id")
        head_name = config.get("headers", "users_user")
        
        cols = [head_id, head_name]
        vals = [user.id, user.name]
        self.insert(table, vals, cols)

    def remove_user(self, user):
        """Removes a user from the database.

        Args:
            user (discord.User): User to remove.
            
        """
        table = config.get("tables", "users")
        header = config.get("headers", "users_id")
        self.delete(table, conditions={header: user.id})


class BotDatabase(DiscordDatabase):
    """An extension of DiscordDatabase for functions specific to the bot."""

    def setup(self):
        super(type(self), self).setup()
        tbl_songs = config.get("tables", "songs")
        head_songid = config.get("headers", "songs_id")
        head_song = config.get("headers", "songs_song")
        head_songurl = config.get("headers", "songs_url")
        head_songplays = config.get("headers", "songs_plays")
        head_songskips = config.get("headers", "songs_skips")
        col_songs = [
            TableColumn(head_songid, "INTEGER", primary_key=True),
            TableColumn(head_song, "TEXT"),
            TableColumn(head_songurl, "TEXT"),
            TableColumn(head_songplays, "INTEGER"),
            TableColumn(head_songskips, "INTEGER"),
            ]
        self.create_table(tbl_songs, col_songs)

        tbl_playlists = config.get("tables", "playlists")
        head_playlistsid = config.get("headers", "playlists_id")
        head_playlist = config.get("headers", "playlists_playlist")
        head_playlistcreator = config.get("headers", "playlists_creator")
        col_playlists = [
            TableColumn(head_playlistsid, "INTEGER", primary_key=True),
            TableColumn(head_playlist, "TEXT"),
            TableColumn(head_playlistcreator, "INTEGER"),
            ]
        self.create_table(tbl_playlists, col_playlists)

        tbl_pls = config.get("tables", "playlistsongs")
        head_plsid = config.get("headers", "playlistsongs_id")
        head_plsplaylist = config.get("headers", "playlistsongs_playlistid")
        head_plssong = config.get("headers", "playlistsongs_songid")
        
        col_pls = [
            TableColumn(head_plsid, "INTEGER", primary_key=True),
            TableColumn(head_plsplaylist, "INTEGER"),
            TableColumn(head_plssong, "INTEGER"),
            ]
        self.create_table(tbl_pls, col_pls)

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

    def add_playlistsong(self, song, playlist):
        """Adds a song to a playlist.

        Args:
            song(): Song to add.
            playlist(): The target playlist.

        """
        pass
    
