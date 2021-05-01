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

    
  if message.content.startswith('$victoryRoyale'):
    await message.channel.send("""[Verse 1: All]
We got a number one victory royale
Yeah, Fortnite, we 'bout to get down (Get down)
Ten kills on the board right now
Just wiped out Tomato Town
My friend just got downed
I revived him, now we're heading south-bound
Now we're in the Pleasant Park streets
Look at the map, go to the marked sheet

[Chorus: All]
Take me to your Xbox to play Fortnite today
You can take me to Moisty Mire, but not Loot Lake
I really love to chug jug with you
We can be pro Fortnite gamers

[Verse 2: All]
He said
"Hey broski, you got some heals and a shield pot?
I need healing and I am only at 1 HP"
Hey dude, sorry, I found nothing on this safari
I checked the upstairs of that house but not the underneath yet
There's a chest that's just down there
The storm is coming fast and you need heals to prepare
I've got V-Bucks that I'll spend
More than you can contend
I'm a cool pro Fortnite gamer (Cool pro Fortnite—)

[Chorus: All]
Take me to your Xbox to play Fortnite today
You can take me to Moisty Mire, but not Loot Lake
I really love to chug jug with you
We can be pro-Fortnite gamers

[Water Break: bogwandyy & Chief Beef]
Bro my jaw hurts so much
Water break

[Bridge: All]
La-la-la-la-la-e-ya
La-la-la-la-la-e-ya
La-la-la-la-la-e-ya
Will you be my pro Fortnite gamer? (Pro Fortnite gamer)

[Verse 3: All]
Can we get a win this weekend?
Take me to Loot Lake
Let's change the game mode and we can Disco Dominate
Let's hop in an ATK
Take me to the zone
I'm running kind of low on mats, I need to break some stone
Dressed in all his fancy clothes
He's got Renegade Raider and he's probably a pro
He just shot my back
I turn back and I attack
I just got a victory royale
A victory royale

[Chorus: All]
Take me to your Xbox to play Fortnite today
You can take me to Moisty Mire, but not Loot Lake
I really love to chug jug with you
We can be pro Fortnite gamers""")
    
  if message.attachments :
    emoji = discord.utils.get(client.emojis, name='this_guy')
    await message.add_reaction(emoji)

keep_alive()
client.run(my_secret)