from discord.ext import commands
import discord

import random
import string
import json

client = commands.Bot(command_prefix="!")
client.remove_command(name="help")

@client.event
async def on_ready():

    data = read_json("keys")
    client.available_keys = data["availableKeys"]

    print("Bot is ready.")

def read_json(filename):
    with open(f"{filename}.json","r") as file:
        data = json.load(file)
    return data

def write_json(data, filename):
    with open(f"{filename}.json", "w") as file:
        json.dump(data, file, indent=4)

@client.command()
async def buy(ctx,catagory=None):
    if catagory == None:
        embed=discord.Embed(title="Buy List",description="Below are available items to buy. Use `!buy [item]` to make a purchase.")
        embed.add_field(name="Test",value="Test Item.")
        embed.set_footer(text="Made by CatNinja#0001")
        await ctx.send(embed=embed)
    elif catagory == "Test" or catagory == "test":
        try:
            key = ("".join(random.choice(string.ascii_letters + string.digits)for i in range(random.randint(56, 60))))
            
            client.available_keys.append(key)
            data = read_json("keys")
            data["availableKeys"].append(key)
            write_json(data,"keys")

            embed=discord.Embed(title="Item Bought!",description="Successfully bought item: `Test`",color=discord.Colour.green())
            embed.add_field(name="Redeem Key",value=key)
            embed.set_footer(text="Made by CatNinja#0001")
            await ctx.send(embed=embed)
        except:
            embed=discord.Embed(title="Error!",description="Error has occured while buying item: `Test`",color=discord.Colour.red())
            embed.set_footer(text="Made by CatNinja#0001")
            await ctx.send(embed=embed)

@client.command()
async def redeem(ctx,catagory=None):
    if catagory == None:
        embed=discord.Embed(title="Redeem a key",description="To redeem a key type `!redeem [key]` if your key does not work it's invalid.")
        embed.set_footer(text="Made by CatNinja#0001")
        await ctx.send(embed=embed)
    else:
        if catagory in client.available_keys:
            embed=discord.Embed(title="Item Redeemed!",description="Successfully redeemed item: `Test`",color=discord.Colour.green())
            embed.set_footer(text="Made by CatNinja#0001")
            await ctx.send(embed=embed)

            client.available_keys.remove(catagory)
            data = read_json("keys")
            data["availableKeys"].remove(catagory)
            write_json(data,"keys")

        else:
            embed=discord.Embed(title="Invalid Key!",description="This key is invalid or has already been redeemed.",color=discord.Colour.red())
            embed.set_footer(text="Made by CatNinja#0001")
            await ctx.send(embed=embed)


client.run("")
    
