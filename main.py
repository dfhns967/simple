import discord

Token = "NzM4MDA4ODc3MjAyODAwNjUw.XyFqUw.zXDmjxwJ-Fj5CrV9yjTZxPKHEag"
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f' Hi {member.name} welcome to ok anem and have fun')

client.run(Token)
