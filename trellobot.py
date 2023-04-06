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
 * Description: Main program. Regularly checks trello and reports events.
 * Version: 1.1
"""

import sys
if "".join(sys.version.split(".")[0:2]) != "310":
	print("[FATAL] Python 3.10 is requered!")
	sys.exit(1)
# # # #
import time
import traceback
import pprint
import json # for exceptions:/
# # # #
import requests
from colorama import init, Fore
init()
# # # #
try:
	from config import telegram_api_token, actions_api, peer_id, set_logging, delay
except ModuleNotFoundError:
	print(traceback.format_exc())
	print("= = =\nMaybe config.py is missing?")
	sys.exit(1)
# # # #

def printraw(printraw_msg):
	""" Outputs pretty-print json if set_logging == True"""
	if set_logging:
		print(Fore.CYAN)
		pprint.pprint(printraw_msg)
		print(Fore.RESET)

def say(my_message, peer_id):
	""" A imprortant feature for sending messages to telegram by a bot """
	my_message = my_message.replace("	","")
	printraw(my_message)
	result = requests.post(f"https://api.telegram.org/bot{telegram_api_token}/sendMessage",
		data={
		"chat_id": peer_id,
		"text": my_message,
		"parse_mode": "HTML",
		"disable_web_page_preview": "true",
		}, timeout=30).text
	printraw(result)
	return result

# # # #

result_old = requests.get(actions_api, timeout=60).json()
while True: # remove position change events
	try:
		if "pos" in result_old[0]["data"]["old"]:
			del result_old[0]
		else:
			break
	except (IndexError, KeyError):
		break
if "old" not in result_old[0]["data"]:
	result_old[0]["data"]["old"] = {} # if not exists
# # # # # # # # # # # #

print("[#] Trello bot started..")
print("Delay: " + str(delay) + " sec")
while True:
	# # # # # # # # # #
	while True: # make error catching, retry request if error occurs
		try:
			result_new = requests.get(actions_api, timeout=60).json()
			break
		except (json.decoder.JSONDecodeError, requests.exceptions.RequestException):
			print("=== Exception caught!")
			print(traceback.format_exc())
			time.sleep(5)
	# # # # # # # # # #
	printraw(result_new)
	while True: # remove position change events
		try:
			if "pos" in result_new[0]["data"]["old"]:
				del result_new[0]
			else:
				break
		except (IndexError, KeyError):
			break
	# # # # # # # # # #
	if "old" not in result_new[0]["data"]:
		result_new[0]["data"]["old"] = {} # if not exists
	printraw(result_new)
	# # # # # # # # # # # #
	if result_old[0] != result_new[0]:
		printraw(result_new)
		event_data = result_new[0]["data"]
		# # # # # # # # # # # # # # # # # # # # # # # # # # #
		if "card" not in event_data:
			pass
		elif "listBefore" in event_data and "listAfter" in event_data:
			temp1 = event_data['card']['name'].replace("<", "&lt;").replace(">", "&gt;") # capitalize first letter
			temp1 = temp1[0].upper() + temp1[1:] # capitalize first letter
			say(f"""🗄️ <b>{temp1}</b>

				<code>{event_data['listBefore']['name']}</code> <b>-></b> <code>{event_data['listAfter']['name']}</code>""", peer_id)
		elif "name" in event_data["old"]:
			temp1 = event_data['old']['name'].replace("<", "&lt;").replace(">", "&gt;") # capitalize first letter
			temp1 = temp1[0].upper() + temp1[1:] # capitalize first letter

			temp2 = event_data['card']['name'].replace("<", "&lt;").replace(">", "&gt;") # capitalize first letter
			temp2 = temp2[0].upper() + temp2[1:] # capitalize first letter
			say(f"""🗄️ Переименование карточки с состоянием <a href="http://www.example.com/">{event_data['list']['name']}</a>!

				<i>{temp1}</i>

				<code>-= 🔽 🔽 🔽 =-</code>
				
				<b>{temp2}</b>""", peer_id)
		elif result_new[0]["type"] == "createCard":
			temp1 = event_data['card']['name'].replace("<", "&lt;").replace(">", "&gt;")  # capitalize first letter
			temp1 = temp1[0].upper() + temp1[1:] # capitalize first letter
			say(f"""🗄️ Новая карточка!
				📍 Статус: <code>{event_data['list']['name']}</code>

				<b>{temp1}</b>""", peer_id)
		else:
			say("❗ Новое событие на Trello.\nНо мне не удалось отобразить изменения.\n\n📃 Дополнительная инфомация была записана в unknown_events.log", peer_id)
			with open("unknown_events.log", "w", encoding="utf-8") as f:
				f.write("\n\n" + str(result_new[0]))
		# # # # # # # # # # # # # # # # # # # # # # # # # # #
		# .replace("<", "&lt;").replace(">", "&gt;") FOR AVOID "Bad Request: can't parse entities: Unsupported start tag \"module\" at byte offset 140"
	result_old = result_new
	time.sleep(delay)
