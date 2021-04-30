import os
import discord
from keep_alive import keep_alive

my_secret = os.environ['TOKEN']

client = discord.Client()

@client.event 
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$hello'):
    await message.channel.send('Hello there')
    
  if message.attachments :
    emoji = discord.utils.get(client.emojis, name='this_guy')
    await message.add_reaction(emoji)

keep_alive()
client.run(my_secret)