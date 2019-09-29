from discord.ext.commands import Bot
import discord
import asyncio
from BotFileHandler import BotFileHandler
from tictactoe import tictactoe

#insert token:
TOKEN = ''
BOT_PREFIX = '&'
DEFAULT_ACTIVITY = discord.Game(name="around with humans")
client = Bot(BOT_PREFIX)

point_handler = BotFileHandler("tunak_greetings_counter.txt")
ttt_game = tictactoe()


@client.command(pass_context=True)
async def hello(context):
    await client.say('Hello to you too, ' + context.message.author.mention)
    point_handler.add_points(context.message.author.name, 1)
    print("Bot: said hi to " + context.message.author.name)


@client.command()
async def topfriends():
    await client.say(point_handler.get_top_friends_str())
    print("Bot: revealed his best friends")


@client.command()
async def ttt(tag, x, y):
    ls = ttt_game.make_move(tag, x, y)
    await client.say(ls[0])
    await client.say(ls[1])


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=DEFAULT_ACTIVITY)
client.run(TOKEN)
