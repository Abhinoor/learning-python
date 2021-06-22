# Import Discord Package
import discord
import random
from discord.ext import commands

# Client (Out Bot)
client = commands.Bot(command_prefix='!')

#For When the Bot Boots Up
@client.event
async def on_ready():
    #Execute these commands upon launch...(States the bot is ready in command line and also sends a hello message in channel)
    print("Bot is ready.")
    general_channel = client.get_channel(Channel Id Here)
    await general_channel.send('Whats Good In The Hood')

#Status and Activity for the bot
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Unraveling the Multiverse'))

#For when user types the command !fate delete their message and send a random answer to their question.
@client.command()
async def fate(ctx, *, question, amount=1):
    await ctx.channel.purge(limit=amount)
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes, definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful.",
                ]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")
    
# Run the client on the server
client.run('Discord Token For Server')
