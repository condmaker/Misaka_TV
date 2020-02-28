import discord
import os
import time
import random

from dotenv import load_dotenv

load_dotenv()
token = os.getenv("NjM1MTI4NjY0MTQ0NjA5Mjgx.XiJ0VA.iq2atiCxZ3H3RHpsU5CYkmPqRtA")

client = discord.Client()
game = discord.Game("Comendo a mãe do Wendell")

@client.event
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
    channel = client.get_channel(490286224754475008) #ID
    await channel.send("Misaka TV, on!") 
    pass

# Battle Royale 
@client.event
async def on_message(message):

    channel = client.get_channel(490286224754475008)

    if message.content == "Battle Royale Start!":

        guild = client.get_guild(413013924515151873) #ID server
        possible_players = guild.members   

        for index in range(len(guild.members)-1):
            
            if message.content == "Battle Royale Stop!":
                break
            index = 0
            # Jogadores random do server
            
            active_players = [random.choice(possible_players), random.choice(possible_players)] # <-- Lista dos membros selecionados

            # Respostas do bot
            response = [(random.choice(active_players)), (random.choice(active_players))]
            response_1 = ("mata")
            response_2 = [(random.choice(active_players)), (random.choice(active_players))]
            response_3 = ["...", "..."]

            # Armas
            arma_1 = ["com uma cópia de Sen no Kiseki IV!", "com uma voadora!", "com بتسنيتصخ", "com uma corda!", "com shittaste!", "com godtaste!", "com um cão lonnbhá!"]

            # Eventos
            event_1 = random.choice(response) 
            message = await channel.send(event_1.name + " " + response_1)
            time.sleep(0.5)
            event_2 = random.choice(response_3)
            await message.edit(content = "{} {} {}".format(event_1.name, response_1, event_2))
            time.sleep(0.5)
            event_3 = random.choice(response_2)
            await message.edit(content = "{} {} {} {} {}".format(event_1.name, response_1, event_2, event_3.name, random.choice(arma_1)))
            possible_players.remove(event_3)
            time.sleep(1)

            if (len(possible_players) > 1):
                await channel.send(">" + str(event_3) + " foi removido!")
            else:
                await channel.send(str(possible_players.name) + " is the Winner!") #Para o vencedor no final
            index = index + 1

            #ID terminal 413131836827631627
            #ID Main-chat 490286224754475008
    if ("!ban @" in message.content):

        guild = client.get_guild(413013924515151873)
        user_id = message.author
        user_idID = message.author.id

        roles = user_id.roles
        rolesNamed = []

        for index in roles:
            rolesNamed.append(index.name)
        
        if ("Clã Atena" not in rolesNamed):
            await channel.send("COUNTER!")
            await channel.send("!ban " + str(user_id.mention))
            await channel.send("Se fodeu retarda")

    # Xingar o Wendell
    list1 = ["wendinha", "Wendinha", "brigadeirinho", "Brigadeirinho"]
    message.content = message.content.casefold()
    list2 = message.content.split()
    result = any(elem in list1 for elem in list2)
    if result:
        swear_box = ["Wendell viado", "Wendell boiola", "Caralho mano toda vez q o Wendell abre a boca eu quero me matar",
        "Um baiano da pesada...", "Brigadeirinho gostoso", "Alguém chamou o caminhão de merda?"]
        swear_jar = random.choice(swear_box)
        await message.channel.send(swear_jar)


client.run("NjM1MTI4NjY0MTQ0NjA5Mjgx.XiJ0VA.iq2atiCxZ3H3RHpsU5CYkmPqRtA")