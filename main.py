import os
import discord
import asyncio
from keep_alive import keep_alive

my_secret = os.environ['TOKEN']

hams = False;

client = discord.Client()

@client.event 
async def on_ready():
  print('we have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):

  
  this_guy_emoji = discord.utils.get(client.emojis, name='this_guy')
  thisguyID =f'<@!{client.user.id}>'


  if message.author == client.user:
    return
  
  if message.content.startswith('$hello'):
    await message.channel.send('Hello there')

  if thisguyID in message.content:
    await message.channel.send("Get a load of " + str(this_guy_emoji))

  if message.attachments :
    await message.add_reaction(this_guy_emoji)

  if message.content.startswith("i'm") or message.content.startswith("I'm") :
    await message.channel.send("Hi, " + message.content[4:] + " I'm " + str(this_guy_emoji))

  if "69" in message.content:
    await message.channel.send("nice")

  if ("Watcher"in message.content or "watcher" in message.content) and ("Knight"in message.content or "knight"in message.content or "Kinghts"in message.content or "kinghts"in message.content):
    await message.channel.send("Watcher Knights, more like wrath inducing fight, amirite, gamers??")

  if "tried" in message.content:
    await message("We've tried nothing, and we're all out of ideas!")
  

  if message.content.startswith("ham") or message.content.startswith("clam")  :
    await message.channel.send("Well, Seymour, I made it... Despite your directions.")

    i = 0 
    while i < 18:
      if await getResponse(message,i) == False:
        break
      i += 1





#dumb music lyrics section

   
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


#operation steamed clams
async def getResponse(message, i):
  expectedResult = {
      0: ["chalmers", "prepared", "lunch"],
      1: ["roast", "ruined", "fast", ],
      2: ["superintendent", "stretch", "exercise"],
      3: ["smoke", "steam", "clams"],
      4: ["whew"],
      5: ["superintendent", "ready", "hamburgers"],
      6: ["steam", "call", "hamburgers"],
      7: ["yes", "regional", "dialect"],
      8: ["upstate", "new", "york"],
      9: ["utica", "albany"],
      10: ["patented", "skinner"],
      11: ["yes"],
      12: ["know", "one", "second"],
      13: ["wonderful", "good", "all"],
      14: ["aurora", "borealis"],
      15: ["yes"],
      16: ["no"],
      17: ["no", "mother", "lights"]
    }

  line = {
    0: """Nyeh...
(Principal Skinner exits into the kitchen)""",
    1: """(Principal Skinner takes off his apron and opens the window. He puts his leg over the window, attempting to step outside. Before he can leave, Superintendent Chalmers enters the kitchen)
Uh--


*Skinner, with his crazy explanations,
The Superintendent's gonna need his medication.
When he hears Skinner's lame exaggerations,
There'll be trouble in town - tonight.*


SEYMOUR!!!!!!!""",
    2: "Why is there smoke coming out of your oven, Seymour?",
    3: "(Superintendent Chalmers exits the kitchen)",
    4: "(Principal Skinner leaves the kitchen from the windowsill and runs across the road into Krusty Burger to purchase hamburgers)",
    5: "I thought we were having steamed clams.",
    6: "You call hamburgers 'steamed hams'?",
    7: "Uh-huh. What region?",
    8: "Really. Well, I'm from Utica and I've never heard anyone use the phrase 'steamed hams'.",
    9: """I see.

(Superintendent Chalmers takes a bite from the hamburger)

You know, these hamburgers are quite similar to the ones they have at Krusty Burger.
""",
    10: "For steamed hams?",
    11: "Yes, and you call them steamed hams, despite the fact that they are obviousl grilled.",
    12: """Of course. 

(Principal Skinner leaves the table and opens the kitchen door walking inside. As the door swings open, it is clear that the kitchen is on fire. He walks back out and yawns)""",
    13: """Yes, I should be---

(Superintendent Chalmers notices the fire through the swinging kitchen door)

GOOD LORD! What is happening in there?""",
    14: "A---Aurora Borealis? At this time of year! At this time of day! In this part of the country! Localized entirely within your kitchen?!?",
    15: "May I see it?",
    16: """(Principal Skinner leads Superintendent Chalmers outside)

[SKINNER'S MOTHER]
Seymour! The house is on fire!""",
    17: """Well, Seymour, you are an odd fellow, but I must say - you steam a good ham.

(Superintendent Chalmers starts to walk away. Principal Skinner stands in front of his burning house)

[SKINNER'S MOTHER]
Heeeeelp! HEEEEEEEELP!!!""",
  }

  def check(m):
    return m.author == message.author and is_correct(m)

  def is_correct(m):
    match = True
    for w in expectedResult.get(i):
      if not w in m.content.lower():
        match = False

    return match

  while True:
    try:
        response = await client.wait_for('message', check=check, timeout=60.0)
        if is_correct(response):
          break
    except asyncio.TimeoutError:
      await message.channel.send("This has been a terrible luncheon, Seymour, i'm leaving ")
      return False

  await message.channel.send(line.get(i))


keep_alive()
client.run(my_secret)