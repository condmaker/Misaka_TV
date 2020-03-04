import discord
import os
import time
import random
import asyncio

from dotenv import load_dotenv

load_dotenv()
token = os.getenv("NjM1MTI4NjY0MTQ0NjA5Mjgx.Xlm1yw.wOY9Sskp_F-wONPkhPIgL3nLg4o")

client = discord.Client()
#discord.opus.load_opus()

wendString = ["Cala a boca Wendell", "Wendell fica quieto pelo amor de jesus",
            "CALA A BOCA WENDELL"]

@client.event
async def on_ready():

    global channel
    global game

    channel = client.get_channel(490286224754475008) #ID
    game = discord.Game("com o Cu do Wendell") 

    print(f"Misaka Misaka is turning on!")
    print(f"Please wait...")
    print(f".")
    time.sleep(0.1)
    print(f".")
    time.sleep(0.3)
    print(f".")
    time.sleep(0.6)
    print(f"Misaka Misaka is on!")

    await client.change_presence(status=discord.Status.idle, activity=game)
    await channel.send("Misaka TV, on!")
    discord.Game("Comendo a mãe do Wendell")
    pass

@client.event
async def on_message(message):

    mesLen = len(message.content)
    ranInt = random.randint(1, 100)

    voiceConnect = discord.utils.get(client.voice_clients, guild=message.guild)

    if (mesLen > 0):
        if (message.content[0] == "|" and (mesLen >= 3)):
            if (message.content[2:5].lower() == "ban"):
                await channel.send("num que nao")
            elif (message.content[2:mesLen].lower() == "wendinha"):
                await channel.send("Le BRIGADEIRINHO has arrived")
            elif (message.content[2:6].lower() == "load"):
                print("test0")
                authorVoice = message.author.voice.channel
                if (message.content[7:mesLen].lower() == "carnaval"
                and authorVoice is not None):
                    print("test1")
                    voiceConnect = await authorVoice.connect()
                    print("test2")

                    await channel.send("AGORA TOCANDO NA RÁDIO:")
                    await channel.send("CARNAVAL PROFUNDO by SINGA DESGRAÇADÃO")

                    time.sleep(3)
                    voiceConnect.play(discord.FFmpegPCMAudio('files/deep_carnival.mp3'))
                    print("test3")
                    voiceConnect.source = discord.PCMVolumeTransformer(voiceConnect.source)
                    print("test4")
                    voiceConnect.source.volume = 1
                    time.sleep(3)

                    if voiceConnect and not voiceConnect.is_playing():
                        await voiceConnect.disconnect()

            else:
                await channel.send("The hell do you want?")
        
        if (message.author.id == 148907545262555136 and ranInt <= 15 and 
        message.channel == 490286224754475008):
            print(str(ranInt))
            await channel.send(random.choice(wendString)) 

client.run("NjM1MTI4NjY0MTQ0NjA5Mjgx.Xlm1yw.wOY9Sskp_F-wONPkhPIgL3nLg4o")

