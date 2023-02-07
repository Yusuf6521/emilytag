# -*- coding: utf-8 -*-

# (c) @aylak-github (Github) | https://t.me/ayIak | @BasicBots (Telegram)

#==============================================================================
#
# Project: CallToneBot
# Copyright (C) 2021-2022 by aylak-github@Github, < https://github.com/aylak-github >.
#
# This file is part of < https://github.com/aylak-github/CallTone > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/aylak-github/CallTone/blob/master/LICENSE >
#
# All rights reserved.
# 
#==============================================================================
#
# Proje: CallToneBot
# Telif Hakkı (C) 2021-2022 aylak-Github@Github, <https://github.com/aylak-github>.
#
# Bu dosya <https://github.com/aylak-github/CallTone> projesinin bir parçası,
# ve "GNU V3.0 Lisans Sözleşmesi" kapsamında yayınlanır.
# Lütfen bkz. < https://github.com/aylak-github/CallTone/blob/master/LICENSE >
#
# Her hakkı saklıdır.
#
#========================================================================

from .mongo.database import (
    SUDO,
    CHATS,
    USERS,
    BAKIM,
    bakim,
    keydb,
    get_count,
    set_count,
    get_duration,
    set_duration,
    lang_set,
    is_lang_exist,
    get_lang,
    delcmd_is_on,
    delcmd_off,
    delcmd_on,
    dbsud,
)
