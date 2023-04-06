#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 * Copyright (C) 2023 Nikita Beloglazov <nnikita.beloglazov@gmail.com>
 *
 * This file is part of Nebobot/Trello-Telegram-Bot.
 *
 * Nebobot/Trello-Telegram-Bot is free software; you can redistribute it and/or
 * modify it under the terms of the Mozilla Public License 2.0
 * published by the Mozilla Foundation.
 *
 * Nebobot/Trello-Telegram-Bot is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY.
 *
 * You should have received a copy of the Mozilla Public License 2.0
 * along with Nebobot/Trello-Telegram-Bot.
 * If not, see https://mozilla.org/en-US/MPL/2.0.
 *
 * Description:
 * Configuration values that are required for the bot to work.
 * If the name of this file is "template_config.py", it should be renamed to
 * "config.py"
"""

telegram_api_token = ""
actions_api = "https://..."
peer_id = 0 # make sure you change this value, using 0 is not allowed!
set_logging = True # after a successful launch, it is recommended to set False
delay = 5