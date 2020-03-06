import discord
import os
import time
import random
import asyncio

from tokens import token
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

bots = commands.Bot(command_prefix='|')

wendString = ["Cala a boca Wendell", 
            "Wendell fica quieto pelo amor de jesus",
            "CALA A BOCA WENDELL", 
            "boa wendell", 
            "Agora você foi longe demais, Wendell.",
            "Silêncio, cristão da putaria", 
            "calor da porra", 
            "Oii Wendell...chama pvt?"]

channel = bots.get_channel(490286224754475008) #ID
game = discord.Game("Chaser!!")

@bots.event
async def on_ready():

    print(f"Misaka Misaka is turning on!")
    print(f"Please wait...")
    print(f".")
    time.sleep(0.1)
    print(f".")
    time.sleep(0.3)
    print(f".")
    time.sleep(0.6)
    print(f"Misaka Misaka is on!")

    await bots.change_presence(status=discord.Status.idle, activity=game)
    #await channel.send("Misaka TV, on!")
    pass

@bots.command(pass_context=True)
async def load(ctx, arg1):

    voiceConnect = discord.utils.get(bots.voice_clients, guild=ctx.guild)

    try:
        authorVoice = ctx.author.voice.channel
    except AttributeError:
        await ctx.send("Entra numa call desgraça")
        return

    if (arg1 == "carnaval"):

        if (voiceConnect and voiceConnect.is_connected()):
            await voiceConnect.move_to(channel)

        voiceConnect = await authorVoice.connect()

        await ctx.send("      " + 
        "<:cd:684755845891883032>*AGORA TOCANDO NA RÁDIO*<:cd:684755845891883032>" 
        + '\n' + "<:fire:684755845891883032>CARNAVAL PROFUNDO<:fire:684755845891883032>"
        + '\n'  
        + "<:bee:684756689907351589>BY SINGA DESGRAÇADÃO<:bee:684756689907351589>")

        time.sleep(3)
        voiceConnect.play(discord.FFmpegPCMAudio('files/deep_carnival.mp3'))
        voiceConnect.source = discord.PCMVolumeTransformer(voiceConnect.source)
        voiceConnect.source.volume = 0.5
        time.sleep(3)
    
    if (arg1 == "exit"):
        if (voiceConnect and voiceConnect.is_connected()):
            await voiceConnect.disconnect()
        else:
            await ctx.send("Entra numa call primeiro porra")
    

@bots.command(pass_context=True)
async def wendinha(ctx):

    atenaCommand = bots.get_guild(413013924515151873)
    atenaTroll = await atenaCommand.fetch_emoji(600942067472007195)

    await ctx.send("Le BRIGADEIRINHO has arrived")
    await ctx.message.add_reaction(atenaTroll) 
    return

@bots.event
async def on_message(message):

    await bots.process_commands(message)
    ranInt = random.randint(0, 100)
    print(str(ranInt))
        
    if (message.author.id == 148907545262555136 and ranInt <= 5 
    and message.channel != 683879107280371774):
        await message.channel.send(random.choice(wendString)) 
    
    if (message.content.lower() == "vishnu-flynn"):
        await message.channel.send("https://youtu.be/GonRGr9fp40")

bots.run(token)

