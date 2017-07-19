# -*- coding: utf-8 -*-
from .. import settings


def test_read_settings_with_default_file():
    FILENAME = "settings.ini"
    settings.read_settings(FILENAME)
    assert False
