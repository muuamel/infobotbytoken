from infobotbytoken import bot #to import the lib

bot = bot()

token = "Paste here the bot token you can extract from the @botfather" 

print(bot.ok(token)) #Shows the status of the bot

print(bot.token(token)) #to check the token

print(bot.id(token)) #to know the id

print(bot.first_name(token)) #to know the first name

print(bot.user_name(token)) #to know the first name

print(bot.is_bot(token)) #To find out if the token is for a bot or not

print(bot.can_join_groups(token)) #To see if the bot can join groups or not

print(bot.can_read_all_group_messages(token)) #To see if the bot can read group messages

print(bot.supports_inline_queries(token)) #To see if the bot can Supports inline querie

