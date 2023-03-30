
[![License: Mozilla Public License 2.0](https://img.shields.io/badge/License-Mozilla%20Public%20License%202.0-blueviolet.svg)](https://mozilla.org/en-US/MPL/2.0)
[![Linting: pylint](https://img.shields.io/badge/linting-pylint-success)](https://pylint.pycqa.org/en/latest/)
[![Author: NikitaBeloglazov](https://img.shields.io/badge/author-.%E2%80%A2%C2%B0%E2%97%8F%E2%9D%A4%EF%B8%8F%20NikitaBeloglazov%20Software%20Foundation%20%E2%9D%A4%EF%B8%8F%E2%97%8F%C2%B0%E2%80%A2.-informational)](https://github.com/NikitaBeloglazov)
[![Part of: Nebobot 💖](https://img.shields.io/badge/part%20of-Nebobot%20%F0%9F%92%96-orange)](https://github.com/Nebobot)

# Trello Telegram Bot
Telegram bot that regularly checks Trello and reports changes on the board.

# License
* [Mozilla Public License 2.0](/LICENSE)

# Features:
* Beautiful message design
* Easily expandable
* Completely open source
* Stable because self-hosted;)
* A free license that allows you to contribute without problems

# Language
The bot is currently distributed in Russian language:( 

If you need English or any other language, write an Issue and I will add support for other languages.

Writing Issue and Pull Requests is possible in these languages: English, Ukrainian, Russian.

# Install
Clone the repository to your local disk
```shell
git clone https://github.com/Nebobot/Trello-Telegram-Bot
```
### [!!] Use your distribution's package manager to install python 3.10, don't forget to install pip if it's not included

Install modules
```shell
pip3.10 install pprint colorama requests
```
### [!!] Then change configuration files, refer to section # Configuration

And then just run it!
```shell
python3.10 trellobot.py
```

# Configuration

### Notation
*NAME_OF_VARIABLE = DEFAULT_VALUE

`telegram_api_token = ""` — Telegram API token, received from [BotFather](https://t.me/BotFather)

`actions_api = "https://..."` — The URL that the bot will access to check for events. For help, see the section # Config # Trello API

`peer_id = 0` — ID of the chat where notifications will be sent. You can get this ID yourself if you have already worked with BotAPI. Otherwise, it is recommended to use third-party Telegram clients that have this functionality. For example, Kotogram. If you do not understand anything at all, write an Issue, I will try to explain to you, if needed

`set_logging = True` — Turns additional logs on and off.

### Trello API
For the bot to work, you need to compose the correct actions_api address. You can make it according to this template:
`https://api.trello.com/1/boards/{BOARD ID}/actions?key={API_KEY FROM APP}&token={TOKEN FROM USER}`

### Get BOARD ID
Go to the desired board in Trello, and look at the URL of the page. There is the value you need.

It looks like this:
```
https://trello.com/b/PfDq3BsL/name
                     ^ ^  ^ ^
                     Board ID
```

### Get API_KEY FROM APP
* Go to https://trello.com/power-ups/admin
* Make new app
* In the API key section, get the key in API Key field (NOT SECRET)
If you do not understand where the parameters you need are located, refer to the picture below.

### Get TOKEN FROM USER
On the same page where you received the API key, you need to click on the hyperlink "you can manually generate a TOKEN". 
This text is to the right of the API Key field. 
Follow the instructions and get a TOKEN.
If you do not understand where the parameters you need are located, refer to the picture below.

### Picture
< photo goes here lol >

# Contribution / Issues
* Any changes are welcome!
* If you want to make a change, please make your code readable and describe your changes. Nobody likes lazy Pull Requests, right? :)
* To speed up the process, write to [maintainer](https://github.com/NikitaBeloglazov)

# Changelog

* 1.0:
  * Initial version
