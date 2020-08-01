import discord

Token = "NzM4OTA2NzI1MjU1NjEwMzY5.XySugw.fo0eL1ix5n36mpqGR5ixNOzCjik"
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f' Hi {member.name} welcome to ok anem and have fun')

client.run(Token)
