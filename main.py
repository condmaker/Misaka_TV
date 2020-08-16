import discord
import os
import time
import random
import requests
import asyncio

from pso2 import pso2_sched
from datetime import datetime
from bs4 import BeautifulSoup
from pygelbooru import Gelbooru
from tokens import token
from discord.ext import commands
from pytz import timezone

bots = commands.Bot(command_prefix='|')

gelbooru = Gelbooru()

global forbidden
forbidden = False

jao_string = [discord.File("files/jao1.png"), 
            discord.File("files/jao2.png")]

channel = bots.get_channel(490286224754475008) #ID
game = discord.Game("Chaser!!")

pso2 = pso2_sched()

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
            await voiceConnect.move_to(authorVoice)

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
            await ctx.send.img("Entra numa call primeiro porra")

@bots.event
async def on_message(message):

    global forbidden

    await bots.process_commands(message)
    ranInt = random.randint(0, 1000)
    atenaTest = bots.get_guild(413013924515151873)

    # Observes the current number
    print(str(message.author) + ": " + str(ranInt))

    if ("vishnu-flynn" in message.content.lower()):
        await message.channel.send("https://youtu.be/GonRGr9fp40")
    elif ("cold steel" in message.content.lower() and ranInt >= 50):
        await message.add_reaction("🤢")
        await message.channel.send("Cala a boca, CSfag")
    elif ("singa" in message.content.lower() and message.author.id != 635128664144609281):
        await message.add_reaction("🐝")
        await message.channel.send("YourVinished escreveu: \n" +
            "LOL imagine liking singa ")
    elif ("test" in message.content.lower() and message.author.id == 151487135201886209):
        pso2.get_current_schedule()
        pso2.read_current_schedule()
        pso2.read_schedule_table()
        await message.channel.send(embed=pso2_embed("Portugal"))
        
    #if (message.content.lower() == "aoi"):
    #    await message.channel.send("TOKI EGAKU KISEKI TADORI")
    #if (message.content.lower() == "kotae sagasu"):
    #    await message.channel.send("ONAJI SORA MIAGENAAAAGARA")
    #if (message.content.lower() == "kotae sagasu"):
    #    await message.channel.send("ONAJI SORA MIAGENAAAAGARA")
    #if (message.content.lower() == "mune ni"):
    #    await message.channel.send("HIMETA OMOI AFUUUUREDASHI")
    #if (message.content.lower() == "sora o kakete"):
    #    await message.channel.send("GIIIN IRO NO YA NI KAWAAAARU")
    #if (message.content.lower() == "motomeau"):
    #    await message.channel.send("KOKORO GA")
    #if (message.content.lower() == "tagau"):
    #    await message.channel.send("ITAMI WA")
    #if (message.content.lower() == "shinjitsu no"):
    #    await message.channel.send("MICHI KASUMASERUUUUUU KEREDOOOOO")
    #if (message.content.lower() == "kousa suru gin no ya"):
    #    await message.channel.send("MITSUMEAU HITOMI NI")  
    #if (message.content.lower() == "onaji yume"):
    #    await message.channel.send("TASHIKA NI, UTSUSHITA")
    #if (message.content.lower() == "tatoe tsumazuite mo"):
    #    await message.channel.send("TATOE KIZU TSUITE MOOOOOOOOOOOO")
    #if (message.content.lower() == "tobitatou"):
    #    await message.channel.send("KAZE TSUBASA NIIIIIIII SHITEEEEEEEE")
    #if (message.content.lower() == "hi o ukete kagayaku"):
    #    await message.channel.send("KIN IRO NO TSUBASA WAAAAAA")
    #if (message.content.lower() == "sora ni egaku"):
    #    await message.channel.send("INOCHI NO, KISEKI OOOOOO")  

    if (ranInt == random.randint(0, 1000) and message.guild.id == 413013924515151873 and not forbidden):
        forbidden = True
        await message.channel.send("<:trollface_insano_psicopata:685671384109940737> time to take a Piss")
        await doNotUseThisFunction(atenaTest)
        forbidden = False

async def doNotUseThisFunction(guild):
    allMembers = guild.members

    for mem in allMembers:

        if mem.id == 635128664144609281:
            continue

        try:
            memChannel = await mem.create_dm()
        except:
            print("\n--SERVERWIDE_IMG ~ Could not create a DM with " + mem + ".\n")
            continue

        result = await gelbooru.random_post(tags=['futanari'])

        generateImage(result)

        if (random.randint(1, 10) >= 5):
            imgChoice = "files/ben.png"
        else: 
            imgChoice = "files/image.jpg"

        try:
            await memChannel.send(file=discord.File(imgChoice, spoiler=True))
        except:
            print("\n--SERVERWIDE_IMG ~ Could not send image to " + mem + ".\n")
            continue

        print("\n--SERVERWIDE_IMG ~ Sent random image to " + mem + ".\n")

def pso2_embed(current_timezone):

    times = [
        (00, 00), (00, 30), (1, 00), (1, 30), (2, 00), (4, 30), (5, 00), (5, 30),
        (6, 00), (6, 30), (10, 00), (10, 30), (11, 00), (11, 30), (12, 00), (12, 30),
        (14, 00), (14, 30), (15, 00), (15, 30), (16, 00), (16, 30), (19, 00), (19, 30),
        (20, 00), (20, 30), (21, 00), (21, 30), (22, 00), (22, 30)
        ]

    updated_times = []

    for time in times:
        updated_times.append(datetime(2020, 1, 1, time[0], time[1], tzinfo=timezone('PST8PDT')).astimezone(timezone(current_timezone)).strftime("%H:%M"))

    embed=discord.Embed(title="August 2020", description= current_timezone + " Timezone (Times may 'overflow' the date.)", color=0x00b3ff)
    embed.set_author(name="Current Month's Schedule for PSO2's Events", icon_url="https://www.trueachievements.com/achievementimages/8339/294405.jpg")
    embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1205616012478971904/xJO1qWcf.jpg")
    embed.add_field(name="\n**Week 1**", value="\u200b", inline=False)
    #embed.set_image()
    embed.set_footer(text="I fucking HATE you.")

    return embed

def generateImage(link):

    with requests.get(link) as jeff:
        imageData = jeff.content

    with open("./files/image.jpg", "wb") as handler:
        handler.write(imageData)
            
bots.run(token)