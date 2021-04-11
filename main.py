import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "m!")

pointsls={}

@client.event
async def on_ready():
    print("Takeoff!")

#Simple Ping command, returns latency too
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency*1000)}ms")
    

#This adds the player name and points to a dict
@client.command(aliases=["add"])
@commands.has_permissions(manage_messages=True)
async def addpoints(ctx, pos, player):
    
    points = (51-int(pos))*2
    player = str(player)
    player = player.lower()
    
    if player not in pointsls:
       pointsls.update({player: points})
       await ctx.send(f"Added {player}.")
    else:
        pointsls.update({player: int(pointsls[player]) + points})
        await ctx.send(f"Updated {player}.")
#Returns message if there's a missing argument     
@addpoints.error
async def addpoints_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You're missing an argument.")
#Returns message if there's a missing permission      
@addpoints.error
async def addpoints_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions to use this command.")
        
        
#Fetches a Player's points
@client.command(aliases=["get"])
async def fetch(ctx, player):
    player = str(player)
    player = player.lower()
    await ctx.send(f"{player} has {pointsls[player]} points.")
    
#Returns message if there's an invalid player
@fetch.error 
async def fetch_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Please provide a valid player. Use m!players to list players.")

#Lists all players and their points
@client.command(aliases=["list"])
async def players(ctx):
    
    playersls = ""
    
    for player in pointsls:
        playersls += f"{player}: {pointsls[player]}\n"
    await ctx.send(playersls)
    

#Helps with syntax
@client.command()
async def syntax(ctx):
    await ctx.send("Command stucture for addpoints is: m!addpoints [pos of challenge beaten] [player] \nCommand Structure for fetch is: m!fetch [player] \nMake sure to fetch an existing player or the bot will give an error")
 
#uwu   
@client.command()
async def info(ctx):
    await ctx.send("Made with Love by Abendregen.\nProgrammed with Python using GNOME Builder.\nOpakue is my daddy~")



client.run("Not Gonna post this here lol")
