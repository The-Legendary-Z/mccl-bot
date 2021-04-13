import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "m!")

pointsls={}

@client.event
async def on_ready():
    print("Takeoff!")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency*1000)}ms")
    
    
    
@client.command(aliases=["add"])
@commands.has_permissions(manage_messages=True)
async def addpoints(ctx, player, pos):
    
    points = (51-int(pos))*2
    player = str(player)
    player = player.lower()
    
    if player not in pointsls:
       pointsls.update({player: points})
       await ctx.send(f"Added {player}.")
    else:
        pointsls.update({player: int(pointsls[player]) + points})
        await ctx.send(f"Updated {player}.")
        
@addpoints.error
async def addpoints_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You're missing an argument.")
        
@addpoints.error
async def addpoints_error2(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions to use this command.")
        
        
        
        
@client.command(aliases=["madd"])
@commands.has_permissions(manage_messages=True)        
async def massadd(ctx, player, points):
    
    player = str(player)
    player = player.lower()
    
    if player not in pointsls:
        pointsls.update({player: points})
        await ctx.send(f"Initialized {player} to {points} points.")
    else:
        pointsls.update({player: int(pointsls[player]) + points})
        await ctx.send(f"Added {points} points to {player}.")


@massadd.error
async def massadd_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You're missing an argument.")
        
@massadd.error
async def massadd_error2(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions to use this command.")




@client.command(aliases=["rem", "remove"])
async def removepoints(ctx, player, points):
    if player in pointsls:
        pointsls.update({player, int(pointsls[player])-points})
        await ctx.send(f"Updated {player}.")
    else:
        await ctx.send(f"Player {player} does not exist.")



@client.command(aliases=["get"])
async def fetch(ctx, player):
    player = str(player)
    player = player.lower()
    await ctx.send(f"{player} has {pointsls[player]} points.")
    

@fetch.error 
async def fetch_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Please provide a valid player. Use m!players to list players.")


@client.command(aliases=["list"])
async def players(ctx):
    
    playersls = ""
    
    for player in pointsls:
        playersls += f"{player}: {pointsls[player]}\n"
    await ctx.send(playersls)
    


@client.command()
async def syntax(ctx):
    await ctx.send("Command stucture for addpoints is: m!addpoints [pos of challenge beaten] [player] \nCommand Structure for fetch is: m!fetch [player] \nMake sure to fetch an existing player or the bot will give an error")
    
@client.command()
async def info(ctx):
    await ctx.send("Made with Love by Abendregen.\nProgrammed with Python using GNOME Builder.\nOpakue is my daddy~")



client.run("Nope lols")
#Test
