import nextcord
from nextcord.ext import commands, application_checks
from nextcord.ext.commands import commands
import youtube_dl
import json
import os

# This Is A Personal Hosted Bot Or You Can Use A VPS
# I Would Recommend Using This For Yourself But You Can Allow Others To use It 

if os.path.exists(os.getcwd() + "/config.json"):
    
    with open("./config.json") as f:
        configData = json.load(f)

token = configData["token"]
precense = configData["precense"]
status1 = configData["status"]

intents = nextcord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged In As {bot.user.name}")
    await bot.change_presence(status=nextcord.Status[status1], activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f"{precense}"))

@bot.slash_command(name="ban", description="bans a user")
async def ban(ctx, user : nextcord.Member, reason : str):
    await user.ban(reason=reason)
    await ctx.channel.send("User Banned Successfully <:yes:992060148573024307>")
    await user.send(f"You Was Banned For {reason}")

@bot.slash_command(name="kick", description="kicks a user")
async def kick(ctx, user : nextcord.Member, reason : str):
    await user.kick(reason=reason)
    await user.send(f"You Was Kicked For {reason}")
    await ctx.channel.send(f"User Kicked Successfully <:yes:992060148573024307>")

@bot.slash_command(name="clear", description="clears the chat")
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
    await ctx.channel.send(f"Cleared {amount} Successfully <:yes:992060148573024307>")

@bot.slash_command(name="warn", description="warns a user")
async def warn(ctx, user : nextcord.Member, reason : str):
    await user.warn(reason=reason)
    await ctx.channel.send(f"Warned {user.mention}, Successfully")

bot.run(token)