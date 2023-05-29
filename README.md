<h1 align="center">infpbot</h1>
<p align="center">With This Package Can You Find Out Get Info Any Token Telegram Bot from https://api.telegram.org</p>


</p>

## Installation :
```bash
pip install infobot  
```
### Example
```python
from infobot import bot #to import the lib

bot = bot()

token = "Paste here the bot token you can extract from the @botfather" 

print(bot.ok(token)) #Shows the status of the bot

print(bot.token(token)) #to check the token

print(bot.id(token)) #to know the id

print(bot.first_name(token)) #to know the first name

print(bot.is_bot(token)) #To find out if the token is for a bot or not

print(bot.can_join_groups(token)) #To see if the bot can join groups or not

print(bot.can_read_all_group_messages(token)) #To see if the bot can read group messages

print(bot.supports_inline_queries(token)) #To see if the bot can Supports inline querie


```
#
### Follow us on social media accounts

* telegram : @s_y_e
* github : https://github.com/MuamleAmeer
